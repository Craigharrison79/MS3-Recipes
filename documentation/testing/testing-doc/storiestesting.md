# Testing user Stories

## As a new user, I want a access to the website on different so I need to site to be responsive

 - ## Navbar menu

    - The content has to be optmized for the device I am using when I visit the site.
    - Due to lack of real estate in the navbar on tablet and mobile device the navbar menu need to collapsed. A toggle button on the right hand side will appear and when click a menu with display the menu option.
    - If toggle button click once menu will appear and click again will close and disappear.

- ## Did we achieve the result: Yes

![navbar](/documentation/storiestest-images/navbar.png)
![navbar2](/documentation/storiestest-images/navbar-small.png)
![navbar3](/documentation/storiestest-images/navbar-small-open.png)

## As a User, I want a easy and hassle free narigate through out the site for page to page.

- ## Navbar buttons

    - The button are response showing exactly which button you are on.  When click the correct action is taken without errors.
    - All buttons take you to the page or perform the exact action which is stated without errors.
    - All social media icons are link to the correct website or application without errors.
    - All buttons are easy to read and understand.

- ## Did we achieve the result: Yes

## As a new User, I want to see the recipe without register. I want to peru's the site to see if this is a site suitable for me to use before joining.

- ## Home Page

    - Have the ability to quickly search for a perticular ingredient, type of course or a particular name of a recipe.

- ## Recipes Page

    - Clear looking layout that is easy for my eye to follow and also to understand what to doing with the information and what to do/go next.
    - All buttons take you to the correct page without errors.
    - See some useful information about the recipe, so I can make a quick decision on to look at the recipe further. 
    -  Name of the recipe.
    - How long it take to make the recipe and how many people it serves up to.
    - Have the ability to quickly search for a perticular ingredient, type of course or a particular name of a recipe.

- ## Did we achieve the result: Yes

## As a new User, I want understand what the differnet will be between signing up at be a user or just to view as a non-user.

- ## Home Page

    - On the home page there is a imformation panel display regarding the uses a user has when sign up to the site.

![vistor](/documentation/storiestest-images/vistor.png)

- ## Did we achieve the result: Yes

 ## As a new User, I want to sign up to the site and start adding recipes to the site.

- ## All Pages

    - Two spot that a user can sign up, navbar and footer from the home page.
    - Once sign up user will be taken to the user dashbroad. Here instruction on how to add recipes.

- ## Did we achieve the result: Yes

![user](/documentation/storiestest-images/new-user.png)

## As a returning User, I want to log in to my dashbroad.

- ## All Pages

    - Two spot that a user can sign up, navbar and footer from the home page.
    - Navbar indicate if you user is sign up already by remove the sign in button with a log out button.

- ## Sign In page

    - Simple sign in process with username and password.
    - Password has a toggle button to check if the user has return the password correctly.

- ## Did we achieve the result: Yes

![returning](/documentation/storiestest-images/returning-user.png)

## As a User, I want to log out and to know if I am log out.

- ## All Pages

    - Two spot that a user can sign out, navbar and footer from the home page.
    - Navbar indicate if the user is out by remove the log out button with a log in button.
    - The user will be taken to the  home page when logging out.
    - Flash message will appear with a message you have log out.

![log](/documentation/storiestest-images/logout.png)
![log](/documentation/storiestest-images/login.png)

- ## Did we achieve the result: Yes

## As a User, I want to be able to add a recipe to the site

- ## Profile

    - ### Non Account User

        - If user is not sign in the website will redirect the user to the sign up page.

    - ### Account User

        - Once log in you will be direct to your profile dashbroad were you have option to Add / Edit / Delete your own recipes.
        - On the dashboard the user will check ADD reicpe button which will take the user to the add recipe page.
        - In this page the user will follow instructions/input boxes to add recipe into the form.
        - The input boxes will signal if the user has enter detail or missing detail in the essential parts of the form.
        - The form is also set to only except certain values, if any of the input are wrong a prompt will tell the user which section have been fill in wrong.
        - Once added a flash message will appear telling them it was successfully added.

    - ## Did we achieve the result: Yes

![add](/documentation/storiestest-images/add-recipe.png)

## As a User, I want to be able to update/edit an recipe to the site.

- ## Profile

    - ### Non Account User / Other Account Users

        - If user is not the person who did not add the recipe to the site. Then the site will not show this information to the user and flash a message saying access deniced. 

    - ### Account User

        - If the user is the person who  wrote the recipe then the site will show the reicpe detail to they in the form.
        - The user can edit the recipe will some section allowing the user to add and remove information to the recipe.
        - Once the user has finish editing the detail of the recipe then click the edit button which will send a alert to check if this is the action they would to do.
        - A flash message will appear telling them it was successfully edited.

    - ## Did we achieve the result: Yes

![edit](/documentation/storiestest-images/edit.png)
![edit2](/documentation/storiestest-images/update.png)

## As a User, I want to be able to delete a recipe.

- ## Profile

    - ### Other Account Users

        -  In the edit and delete page of the site, if the reicpe don't belong to the user they will not be able to edit or delete the reicpe.
        - Edit and delete buttons will be remove.

    -  ### Account User

        - From the edit and delete recipe page and user will be able to click on a edit reicpe or delete reicpe button, but only if the recipe belong to them.
        - Once the delete button has been click a alert message will appear asking if the user wants to delete this recipe.  I user will have to click ok or cancel button.  This will help the user from deleting a recipe by accident.

    - ## Did we achieve the result: Yes

![delete](/documentation/storiestest-images/delete.png)

## As a User / Vistor want to be able to find a recipe quickly.

-  Users and vistors have two places to quickly find a recipe by the search bar.
- Search bar is in two places:
    - Home page - Middle of the page which when use will take the user to the recipe page and show all the options they requested.
    - Recipe page it's self - at the top of the page.  This will just show the relevant recipes to the request made.

- ## Did we achieve the result now: Yes

![find](/documentation/storiestest-images/find.png)
![find2](/documentation/storiestest-images/find2.png)

## As a User / Vistor want to send a message about the site, problems they are having with the site or any other problem / question they may have.

- Every page has a contact button in the footer which when click will take the user to the contact us page.
- User can fix in the user details in the form and a message about the issue.  This will send a confirmation email to the user saying we receive their message.
- This will also send a message to the company with details about the users and the issue / message they have sent.

- ## Did we achieve the result now: Yes

![contact](/documentation/storiestest-images/contactus.png)

## As a User / Vistor want to view social media from the company.

- Every page has a the relative social media button in the footer which when click will take the user to the appropriate page in a new browser.

- ## Did we achieve the result now: Yes