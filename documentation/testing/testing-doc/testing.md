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

#### JSHint validator

- Javascript file was tested in [JSHint](https://jshint.com/) and came back all clear expect ES6 (use 'esversion: 6) code.

![JSHint](/documentation/testing/images/validator/jshint.png)

#### PEP 8

- I run the python file throught [PEP8 online](http://pep8online.com/) and returned 4 errors (E125, E127).

![PEP8](/documentation/testing/images/PEP8/PEP8-14.png)

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


##  Intersesting bugs and Issues

### Password show toggle 

