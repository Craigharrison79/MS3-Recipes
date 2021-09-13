import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
from functools import wraps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
#Database
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
#Email
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL__USE_TLS"] = True
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_DEBUG"] = False
app.config["MAIL_MAX_EMAILS"] = 5
app.config["MAIL_SUPPRESS_SEND"] = False
app.config["MAIL_ASCII_ATTACHMENTS"] = False
mail = Mail(app)


mongo = PyMongo(app)


# Code from mentor Felipe Souza Alarcon
# Decorators
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return test(*args, **kwargs)
        else:
            flash('You must log in first')
            return redirect(url_for("login"))
    return wrap


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Setup and login page
@app.route("/account", methods=["GET", "POST"])
def account():
    return render_template("account.html")


# Method to setup a new account
@app.route("/new_account", methods=["GET", "POST"])
def new_account():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("new_account"))

        register = {
            "first_name": request.form.get("first_name"),
            "lastt_name": request.form.get("last_name"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("account.html")


# method for user to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("account.html")


# Render profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    # grab the session user's usernname from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("account.html"))


# log user out of profile
@app.route("/logout")
@login_required
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Show all recipe on page
@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipe.find()
    return render_template("recipes.html", recipes=recipes,
                            page_title="Recipes")


# Search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipe.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes,
                            page_title="Recipes")


# Show recipe on page
@app.route("/show_recipe/<recipe_id>")
def show_recipe(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    courses = mongo.db.meal_courses.find().sort("meal_course", 1)
    return render_template("show_recipe.html", recipe=recipe, courses=courses)


# allow user to add recipe and post them on the site. (must be login)
@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    if request.method == "POST":
        meal = {
            "meal_course": request.form.get("meal_course"),
            "recipe_name": request.form.get("recipe_name"),
            "img": request.form.get("img"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "cooking_time": request.form.get("cooking_time"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings"),
            "create_by": request.form.get("create_by"),
            "added_by": session["user"],
            "day_added": request.form.get("day_added")
        }
        mongo.db.recipe.insert_one(meal)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    courses = mongo.db.meal_courses.find().sort("meal_course", 1)
    return render_template("add_recipe.html", courses=courses)


# render recipe to be selected to edit
@app.route("/edit_recipe", methods=["GET", "POST"])
@login_required
def edit_recipe():
    recipes = mongo.db.recipe.find()
    return render_template("edit_recipe.html", recipes=recipes)


@app.route("/recipe_update/<recipe_id>", methods=["GET", "POST"])
@login_required
def recipe_update(recipe_id):
    #{% if event.created_by == user._id %}
    if request.method == "POST":
        submit = {
            "meal_course": request.form.get("meal_course"),
            "recipe_name": request.form.get("recipe_name"),
            "img": request.form.get("img"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "cooking_time": request.form.get("cooking_time"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings"),
            "create_by": request.form.get("create_by"),
            "added_by": session["user"],
            "day_added": request.form.get("day_added")
        }
        mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe has been Updated Successfully")

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    courses = mongo.db.meal_courses.find().sort("meal_course", 1)
    return render_template("recipe_update.html", recipe=recipe,
                            courses=courses)


@app.route("/delete_recipe")
@login_required
def delete_recipe():
    recipes = mongo.db.recipe.find()
    return render_template("delete_recipe.html", recipes=recipes)


# Allow user to pick a particular recipe to be deleted
@app.route("/eliminate_recipe/<recipe_id>")
@login_required
def eliminate_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("delete_recipe"))


# https://pythonhosted.org/Flask-Mail/
# Pretty Printed https://www.youtube.com/watch?v=48Eb8JuFuUI&t=944s
@app.route("/contact_us", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        sender_name = request.form['name']
        sender_email = request.form['email']
        sender_phone = request.form['phone']
        sender_message = request.form['message']
        admin_email = os.environ.get("MAIL_DEFAULT_SENDER")
        recipients = [sender_email, admin_email]
        with mail.connect() as conn:
            for recipient in recipients:
                if recipient == admin_email:
                    message = (f"<h3>Hello here is a message from: {sender_name}</h3>"
                               "<p>Please find below message from:</p>"
                               f"<p><b>Email:</b> {sender_email}</p> "
                               f"<p><b>Phone:</b> {sender_phone}</p> "
                               f"<p><b>Message:</b> {sender_message} </p>")
                    subject = f"New query from: {sender_name}"

                elif recipient == sender_email:
                    message = (f"<h2>Welcome {sender_name},</h2>"
                               "<p>We would like to say Hello from the Team here "
                               "at MPT Recipe "
                               "Thanks for your message and aim"
                               " to respond within the next 1-2 working "
                               "days.</p>"
                               "<p>Kind regards</p>"
                               "<p>MPT Recipe Team</p>"
                               )
                    subject = 'Thank your for your message'

                msg = Message(recipients=[recipient],
                              html=message,
                              subject=subject)
                conn.send(msg)

        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))  
        return redirect(url_for('contact'))     
    return render_template("contact_us.html", page_title="Contact Us")


@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404


@app.errorhandler(403)
def error_403(error):
    flash("Sorry! Something went wrong.")
    return render_template("home.html")


@app.errorhandler(500)
def error_500(error):
    flash("Sorry! Something went wrong.")
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Change to False before submit the project
