# Testing user Stories

## As a new user, I want an access the website on different device so I need to site to be responsive.

 - ## Navbar menu

    - The content has to be optimised for the device I am using when I visit the site.

    - Due to lack of real estate in the navbar on tablet and mobile devices, the navbar menu needs to collapse. A toggle button on the right hand side will appear and when click, a menu will display the menu option.

    - If toggle the button is click once, the menu will appear and clicked again it will close and disappear.

- ## Did we achieve the result: Yes

![navbar](/documentation/storiestest-images/navbar.png)
![navbar2](/documentation/storiestest-images/navbar-small.png)
![navbar3](/documentation/storiestest-images/navbar-small-open.png)

## As a User, I want an easy and hassle free navigate through out the site for page to page.

- ## Navbar buttons

    - The buttons are responsive, showing exactly which button you are on. When click the correct action is taken without errors.

    - All buttons take you to the page or perform the exact action which is stated without errors.

    - All social media icons are linked to the correct website or application without errors.

    - All buttons are easy to read and understand.

- ## Did we achieve the result: Yes

## As a new User, I want to see the recipes without having to register. I want to peru's the site to see if this is a site suitable for me to use before joining.

- ## Home Page

    - Have the ability to quickly search for a particular ingredient, type of course or a particular name of a recipe.

- ## Recipes Page

    - Clear looking layout that is easy for the eye to follow and also to understand what to do with the information and what to do/go next.

    - All buttons take you to the correct page without errors.

    - See some useful information about the recipes, so I can make a quick decision whether on to look at the recipe further.

    -  Name of the recipe.

    - How long it take to make the recipe and how many people it serves.

    - Have the ability to quickly search for a particular ingredient, type of course or a particular name of a recipe.

- ## Did we achieve the result: Yes

## As a new User, I want to understand what the difference will be between signing up and be a user or just view as a non-user.

- ## Home Page

    - On the home page there is an information panel display benefits a user has when signing up to the site.

![vistor](/documentation/storiestest-images/vistor.png)

- ## Did we achieve the result: Yes

 ## As a new User, I want to sign up to the site and start adding recipes to the site.

- ## All Pages

    - Two spots that a user can sign up, navbar and footer from the home page.

    - Once signed up the user will be taken to the user dash-broad. Here they will find the instruction on how to add recipes.

- ## Did we achieve the result: Yes

![user](/documentation/storiestest-images/new-user.png)

## As a returning User, I want to log in to my dash-broad.

- ## All Pages

    - Two spots that a user can sign up, navbar and footer from the home page.

    - Navbar indicate if you as a user is signed up already by transforming the sign in button with a log out button.

- ## Sign In page

    - Simple sign in process with username and password.

    - Password has a toggle button to check if the user has enter the password correctly.

- ## Did we achieve the result: Yes

![returning](/documentation/storiestest-images/returning-user.png)

## As a User, I want to log out and to know if I am logged out.

- ## All Pages

    - Two spots that a user can sign out, navbar and footer from the home page.

    - Navbar indicate if the user is log out by replacing the log out button with a log in button.

    - The user will be taken to the home page when logging out.

    - Flash message will appear with a message that you have logged out.

![log](/documentation/storiestest-images/logout.png)
![log](/documentation/storiestest-images/login.png)

- ## Did we achieve the result: Yes

## As a User, I want to be able to add a recipe to the site

- ## Profile

    - ### Non Account User

        - If a user is not signed in to the website it will redirect the user to the sign up page.

    - ### Account User

        - Once logged in you will be directed to your profile dash-broad were you have the option to Add / Edit / Delete your own recipes.

        - On the dashboard the user will check ADD recipe button which will take the user to the add recipe page.

        - In this page the user will follow instructions/input boxes to add recipes into the form.

        - The input boxes will signal if the user has entered details or is missing details in the essential parts of the form.

        - The form is also set to only accept certain values, if any of the inputs are wrong a prompt will tell the user which section have been filled in wrong.

        - Once added a flash message will appear telling them it was successfully added.

    - ## Did we achieve the result: Yes

![add](/documentation/storiestest-images/add-recipe.png)

## As a User, I want to be able to update/edit a recipe to the site.

- ## Profile

    - ### Non Account User / Other Account Users

        - If the user is not the person who added the recipe on the site, then the site will not show this information to the user and flash a message saying access denied.

    - ### Account User

        - If the user is the person who wrote the recipe then the site will show the recipe details to them in the form.

        - The user can edit the recipe with some sections allowing the user to add and remove information to the recipe.

        - Once the user has finished editing the details of the recipe, then they can click the edit button which will send an alert to check if this is the action that they would want to do.

        - A flash message will appear telling them it was successfully edited.

    - ## Did we achieve the result: Yes

![edit](/documentation/storiestest-images/edit.png)
![edit2](/documentation/storiestest-images/update.png)

## As a User, I want to be able to delete a recipe.

- ## Profile

    - ### Other Account Users

        -  In the edit and delete page of the site; if the recipe do not belong to the user they will not be able to edit or delete the recipe.

        - Edit and delete buttons will be removed.

    -  ### Account User

        - From the edit and delete recipe page the user will be able to click on a edit recipe or delete recipe button, but only if the recipe belongs to them.

        - Once the delete button has been clicked an alert message will appear asking if the user wants to delete this recipe. Then the user will have to click the ok or cancel button. This will help the user from deleting a recipe by accident.

    - ## Did we achieve the result: Yes

![delete](/documentation/storiestest-images/delete.png)

## As a User / Visitor I want to be able to find a recipe quickly.

-  Users and visitors have two places to quickly find a recipe by the search bar.

- Search bar is in two places:

    - Home page - Middle of the page which when used will take the user to the recipe page and show all the options they requested.

    - Recipe page itself - at the top of the page. This will just show the relevant recipes to the request made.

- ## Did we achieve the result now: Yes

![find](/documentation/storiestest-images/find.png)
![find2](/documentation/storiestest-images/find2.png)

## As a User / Visitor  wants to send a message about the site, problems they are having with the site or any other problem / questions they may have.

- Every page has a contact button in the footer which when clicked will take the user to the contact us page.

- Users can fill in the user details in the form and a message about the issue. This will send a confirmation email to the user saying we received their message.

- This will also send a message to the company with details about the users and the issue / message they have sent.

- ## Did we achieve the result now: Yes

![contact](/documentation/storiestest-images/contactus.png)

## As a User / Visitor want to view social media from the company.

- Every page has the related social media button in the footer which when clicked will take the user to the appropriate page in a new browser.

- ## Did we achieve the result now: Yes