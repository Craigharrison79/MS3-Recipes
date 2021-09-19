# Testing

## Code Validation

- #### W3C HTML

    Running each page throught the [W3C Markup Validation](https://validator.w3.org/) it come back with errors

    - All to do with Ginger programming language
    [Ginger](https://ginger.readthedocs.io/en/latest/)

#### Other code issues with W3C:

- Home Page:

    - Section lacks heading.
    - An img element must have an alt attribute
    - An img element must have an alt attribute

![Home](/documentation/testing/images/validator/w3-validator-1.png)

- Recipe Page

    - Missing a closing div.

- Show Recipe page

    - Had a "br" tag in the "ul" so remove it and use CSS class - gap-bottom: margin-bottom: 20px;

![Showrepcipe](/documentation/testing/images/validator/show-recipe.png)

- Account Page

    - Issue with empty heading but I want a icon here and not a heading. So change it to a div with a #icon-heading - font-size: 60px; 

![account](/documentation/testing/images/validator/account.png)

- Profile Page

    - Missing a closing div.

- Adding Recipe Page

    - Had "div" in the table so I remove them. 
    - patten not allowed, this was advice given to me by my mentor and I also ask him about it after.  He said it was fine to do this in the project.

![adding recipe](/documentation/testing/images/validator/addrecipe.png)
![adding recipe3](/documentation/testing/images/validator/addrecipe3.png)
![adding recipe4](/documentation/testing/images/validator/addrecipe4.png)

- Update Recipe Page

    - duplicate Id's which I just remove
    - Bad Id because I miss put the class attribute in after the Id tag.  Just add it.
    - Closed "td" which was then change to "tr"
    - Unclosed div element, again just add a 
    /div element to bottom of the page.

![update](/documentation/testing/images/validator/update1.png)
![update2](/documentation/testing/images/validator/update2.png)
![update3](/documentation/testing/images/validator/update3.png)
![update4](/documentation/testing/images/validator/update4.png)
![update5](/documentation/testing/images/validator/update5.png)

- Contact Us Page

    - No Validate which was messing up the form request.  So just remove it. (This form was taken for the thorin-and-company project with the code institute)
    [Code Institute](https://codeinstitute.net/)

![contact](/documentation/testing/images/validator/contact-us.png)

- Issue Still left

    - patten not allowed, again this was advice given to me by my mentor and I also ask him about it after.  He said it was fine to do this in the project.
    - Ginger programming language


#### W3C CSS Jigsaw Validator

- The CSS file was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

#### Wave Accesibility

- On each page I had contrast errors. It wanted me to be more black but I like the white and wanted to keep it like this.
- Link errors on the logo in the navbar I listen to a few developer and some say to do it and other not to.  I want to use it here as on mobile you can get to the home faster.
- Missing label and aria tag.
    - This I fix.
    - Some label / aria are the same because the program is looping over the same template. 

![wave1](/documentation/testing/images/validator/wave-home.png)
![wave2](/documentation/testing/images/validator/wave-recipe.png)
![wave3](/documentation/testing/images/validator/wave-account.png)

#### JSHint validator

- Javascript file was tested in [JSHint](https://jshint.com/) and came back all clear expect ES6 (use 'esversion: 6) code.

![JSHint](/documentation/testing/images/validator/jshint.png)

#### PEP 8

- I run the python file throught [PEP8 online](http://pep8online.com/) and returned 6 errors (E125, E127, E501).

    - I left them allow as fix it one way would just throw up a another code.

![PEP8](/documentation/testing/images/PEP8/PEP8-finish.png)

## Testing Performance

- ### Lighthouse

On running the whole site through lighthouse on chrome developer tools.  I got different results for each page.

- #### Home Page

![ligthhouse1](/documentation/testing/images/lighthouse/lighthouse-1.png)

- #### Recipes

![ligthhouse2](/documentation/testing/images/lighthouse/lighthouse-2.png)

- #### Show Single Recipe

![ligthhouse3](/documentation/testing/images/lighthouse/lighthouse-3.png)

- #### Login

![ligthhouse4](/documentation/testing/images/lighthouse/lighthouse-4.png)

- #### Profile

![ligthhouse5](/documentation/testing/images/lighthouse/lighthouse-5.png)

- #### Edit Recipe

![ligthhouse6](/documentation/testing/images/lighthouse/lighthouse-6.png)

- #### Home page Mobile

![ligthhouse7](/documentation/testing/images/lighthouse/lighthouse-m-1.png)

- #### Edit Recipe Mobile

![ligthhouse8](/documentation/testing/images/lighthouse/lighthouse-m-2.png)

### Fix to lighthouse report

- I was able to improve the overall scores but still different results for each page. On big issue was the url images affecting best pracitces score. Think next time I try something like this I want to maybe download the image to a file.

![lighthousenew](/documentation/testing/images/lighthouse/lighthouse-new-home.png)

![lighthousenew2](/documentation/testing/images/lighthouse/lighthouse-new-recipe.png)

-   Best Practices when down but I add more recipe to this page.  Again url images.

![lighthousenew3](/documentation/testing/images/lighthouse/lighthouse-new-account.png)

![lighthousenew4](/documentation/testing/images/lighthouse/lighthouse-new-editrecipe.png)

##  Intersesting bugs and Issues:

- ### Recipe Update

    - On the in ingredinents and Method section when add and delete extra, the input section was disappear if you delete all the input. Then went you click on the add button to restart adding inputs again the input box would not a appear.
        - To fix this I had to add:
            if (rowNumber > '1') and a alert to tell the user they couldn't remove the last row.

- ### Password show toggle 

    - The toggle on the create account page and the sign in page was affecting each other.  I have them as one function but I decided to split them up into two function which stop the problem from happening.
        - The is maybe a better way to do this and maybe I can come back to this in the future.

- ### Contact Us Mail

    - I had a issue with heroku and found it was a issue with flash mail.  It told me 2 days of trying to figure out the code and I adventure turn to the tutor at code institute.
        - I found the problem when talking with the tutor as I had put a extra M when enter the code: 
        app.config["MMAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER") instead of 
        app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

- ### Update Page Prevent Access

    - My mentor show me the was a issue that some on could still hack into the page even with the @login_required function. So I task my with the job of fix this issue.  I managed to do it after a frustrating few days.  But the code scene to be working backward.  I try this the other way but I will not work.  I ask my mentor and he mention it was working and sometimes we may not be able to explain why.

    if session["user"] == name:
        flash("Prevent Access.")
        return redirect(url_for("home"))

    this should be the other way around but I will not work if I change it to:

    if session["user"] != name:
        flash("Prevent Access.")
        return redirect(url_for("home"))

    As I don't understand why this is happen I left it knowing the function is doing the job.

- ### Form resizing Issue

    - When using the google dev tools to see how the performer is on responsive to changes in screen size the input field data from the database was not responsive.  But if you hit refresh the date field would correct it's self.
    - Think this is a issue with materialize.

![form1](/documentation/testing/images/validator/responsive-form-1.png)
![form2](/documentation/testing/images/validator/responsive-form-1.png)

- ### Resizing screen

    - Due to the information that is displayed on the screen with CRUD and input information into the database the resizing of the screen brake at  around 200px and less.  As most devices at this present time (19-9-2021) do not have screen less then 320px.

- [Read info on mobile screen size: From worship agency](https://worship.agency/mobile-screen-sizes-for-2021)
- [Read info on mobile screen size: From accessally.com](https://accessally.com/blog/mobile-responsive-screen-sizes/#:~:text=For%20example%2C%20the%20smallest%20screen,the%20Galaxy%20phones%20and%20tablets.)