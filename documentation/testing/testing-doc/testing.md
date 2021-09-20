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

    - Had a "br" tag in the "ul" so removed it and used CSS class - gap-bottom: margin-bottom: 20px;

![Showrepcipe](/documentation/testing/images/validator/show-recipe.png)

- Account Page

    - Issue with empty heading but I wanted an icon here and not a heading. So I changed it to a div with a #icon-heading - font-size: 60px;

![account](/documentation/testing/images/validator/account.png)

- Profile Page

    - Missing a closing div.

- Adding Recipe Page

    - Had "div" in the table so I removed them.
 
    - Patten not allowed, this was an advice given to me by my mentor and I also asked him about it afterwards. He said it was fine to do this in the project.

![adding recipe](/documentation/testing/images/validator/addrecipe.png)
![adding recipe3](/documentation/testing/images/validator/addrecipe3.png)
![adding recipe4](/documentation/testing/images/validator/addrecipe4.png)

- Update Recipe Page

    - duplicate Id's which I just removed.

    - Bad Id because I miss putting a class attribute in after the Id tag. Just added it.

    - Closed "td" which was then changed to "tr".

    - Unclosed div element, again just added a /div element to the bottom of the page.

![update](/documentation/testing/images/validator/update1.png)
![update2](/documentation/testing/images/validator/update2.png)
![update3](/documentation/testing/images/validator/update3.png)
![update4](/documentation/testing/images/validator/update4.png)
![update5](/documentation/testing/images/validator/update5.png)

- Contact Us Page

    - “No validate” which was messing up the form request. So I just removed it. (This form was taken from the thorin-and-company project with the code institute) [Code Institute](https://codeinstitute.net/)

![contact](/documentation/testing/images/validator/contact-us.png)

- Issue Still left

    - Patten not allowed; again this was advice given to me by my mentor and I also ask him about it after. He said it was fine to do this in the project.

    - Ginger programming language


#### W3C CSS Jigsaw Validator

- The CSS file was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

    - Everything was Ok with CSS

#### Wave Accessibility

- On each page I had contrast errors. It wanted me to have black text but I like the white text and wanted to keep it like this.

- Link errors on the logo in the navbar. I listened to a few developers and some say to do it and others not too. I want to use it here as on mobile you can get to the home faster.

- Missing label and aria tag.

    - This I fix.

    - Some label / aria are the same because the program is looping over the same template.


![wave1](/documentation/testing/images/validator/wave-home.png)
![wave2](/documentation/testing/images/validator/wave-recipe.png)
![wave3](/documentation/testing/images/validator/wave-account.png)

#### JSHint validator

- Javascript file was tested in JSHint and came back all clear expect ES6 (use 'esversion: 6) code.

![JSHint](/documentation/testing/images/validator/jshint.png)

#### PEP 8

- I run the python file through [PEP8 online](http://pep8online.com/) and returned 6 errors (E125, E127, E501).

    - I left them alone as if fixed it one way it would just throw up another code.

![PEP8](/documentation/testing/images/PEP8/PEP8-finish.png)

## Testing Performance

- ### Lighthouse

On running the whole site through lighthouse on chrome developer tools, I got different results for each page.

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

### Corrections to the lighthouse report

- I was able to improve the overall scores but still I got different results for each page. One big issue was the url images affecting best practices score. I think next time I will  try something like this but I might want to download the images to a file.


![lighthousenew](/documentation/testing/images/lighthouse/lighthouse-new-home.png)

![lighthousenew2](/documentation/testing/images/lighthouse/lighthouse-new-recipe.png)

-   Best Practices score went down but I added more recipe to this page. Again url images.


![lighthousenew3](/documentation/testing/images/lighthouse/lighthouse-new-account.png)

![lighthousenew4](/documentation/testing/images/lighthouse/lighthouse-new-editrecipe.png)

## Responsiveness and compatibility

- Testing the website through the following browsers.

![Responsiveness](/documentation/testing/images/validator/browser-test.png)



- Testing the website through the following devices.

![Compatibility](/documentation/testing/images/validator/device-test.png)

##  Intersesting bugs and Issues:

- ### Recipe Update

    - On the ingredients and method section, when adding and deleting extra details, the input section would disappear if you deleted all the inputs. Then when you click on the add button to restart adding inputs again the input box would not appear.

        - To fix this I had to add: if (rowNumber > '1') and an alert to tell the user they couldn't remove the last row.


- ### Password show toggle 

    - The toggle on the create account page and the sign in page was affecting each other. I have them as one function but I decided to split them into two functions which stops the problem from happening.

        - There is maybe a better way to do this and maybe I can come back to this in the future.


- ### Contact Us Mail

    - I had an issue with heroku and found it was an issue with the flash mail. It took me days to try to figure out the code and I eventually turned to the tutors at code institute for advise.

        - I found the problem when talking to the tutor as I had put a extra M when enter the code: app.config["MMAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER") instead of app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")


- ### Update Page Prevent Access

    - My mentor showed me that there was an issue that some one could still hack into the page even with the @login_required function. So I was tasked with the job of fixing this issue. I managed to do it after a frustrating few days. But the code seemed to be working backwards. I tried this the other way but it would not work. I asked my mentor and he mentioned it was working and sometimes we may not be able to explain why.

    if session["user"] == name:
        flash("Prevent Access.")
        return redirect(url_for("home"))

    - this should be the other way around but it will not work if I change it to:

    if session["user"] != name:
        flash("Prevent Access.")
        return redirect(url_for("home"))

    As I don't understand why this happen, I left it knowing the function is doing the job.

- ### Form resizing Issue

    - When using the google dev tools to see how the performance is on different screen sizes, the input field data from the database was not responsive. But if you hit refresh the date field would correct itself.

    - I think this is an issue with materialize.

![form1](/documentation/testing/images/validator/responsive-form-1.png)
![form2](/documentation/testing/images/validator/responsive-form-1.png)

- ### Resizing screen

    - Due to the information that is displayed on the screen with CRUD and the input information into the database the resizing of the screen brakes at around 200px or less. As most devices at this present time (19-9-2021) do not have screens less then 320px it was hard for me to show the data on the screen space with such little real estate to work with. This means that the website will break at less than 200px. 

- [Read info on mobile screen size: From worship agency](https://worship.agency/mobile-screen-sizes-for-2021)
- [Read info on mobile screen size: From accessally.com](https://accessally.com/blog/mobile-responsive-screen-sizes/#:~:text=For%20example%2C%20the%20smallest%20screen,the%20Galaxy%20phones%20and%20tablets.)

- ### Safari browser

    - One issue on the recipe_update page with the add ingredients / method button which being in the extra input boxes.  Is not showing up as a red colour but as a white / grey colour.

![safari](/documentation/testing/images/validator/safari-btn.png)


- ### Issue with the add_recipe and recipe_update page.

    - Day of handing in this project the website input fields crash. Something had been remove /change in the file and the input data was not being sent to the database. Also the additional field input boxes on the ingredients and method were not responding to the user clicking on the buttons.
        - I had to look back over old code to find the problem. I replace part of the js code (function addRow, deleteRow, addMethodRow and removeMethodRow).
        Remove the input type from url to text in the image input on both the add recipe and update recipe page. This fix the problem with sending data to the database and the additional input boxes working correctly but on the edit recipe page the is sometime a extra empty input boxes produce when saving the recipe.  This is something I will have to fix in the future as I ran out of time with this project.  As the user of the site will probably not see or pick up on this issue as the recipe card show no indication of a input or that the is some wrong. I hate that is issue is here but I not sure how to fix it and time is running out.