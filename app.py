import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/account", methods=["GET", "POST"])
def account():
    return render_template("account.html")


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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's usernname from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("account.html"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipe.find()
    return render_template("recipes.html", recipes=recipes,
                            page_title="Recipes")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        meal = {
            "meal_course": request.form.get("meal_course"),
            "recipe_name": request.form.get("recipe_name"),
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


@app.route("/delete_recipe")
def delete_recipe():
    recipes = mongo.db.recipe.find()
    return render_template("delete_recipe.html", recipes=recipes)


@app.route("/eliminate_recipe/<recipe_id>")
def eliminate_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("delete_recipe"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Change to False before submit the project

