# **Milestone Project 3**
**THIS PROJECT IS FOR EDUCATIONAL USE ONLY**

**Asian Flavours**

Welcome to Asian flavor. 
The purpose of this website is that people can share different (preferably Asian) dishes with each other. You can do this by registering yourself. If you are registered you can sign in and sign out, keep track of recipes, change and delete your own recipes.

Come and share your favorite asian meals! <br />

Don't wait any longer and Sign Up! !

live site [Asian Flavour](https://asian-flavours.herokuapp.com/)

## **Contents** ##
* UX
    * [Project Summary](#project-summary)
    * [User Stories](#user-stories)
    * [Design Choices](#design-choices)
* [Wireframes](#wireframes)
* [Features](#features)

* [Technologies](#technologies)
* [Testing](#testing)
* [Fixed Issues](#fixed-issues)
* [Deployment](#deployment)
* [Credit](#credits)

## **UX (User Experience)** ##
### **Project Summary** ###

The goal of this project is (CRUD) to create a database of recipes that allows users to add, read, update and delete recipes.
Asian Flavors gives access to all recipes in the database for all registered and unregistered users. Registered users can add new recipes, edit and delete their own recipes.

### **UX** ###
** First time user **

-	As a first user, I want to be able to register easily.
-   As a first time user, I want an easy navigation website so that I can add 
    and see my (new) recipes.
-	As a first user, I want a clear looking website so that the recipes are         easy to follow.

** Returning Users **

-	As a returning user, I want to be able to sign in and out easily.
-   As a returning user, I want to be able to edit and/or delete my added 
    recipes.
-   As a returning user, I would like to see all added recipes without logging 
    in.

** Site owner’s Goal: **

-   As the site owner, I want the user to have an easily accessible site.
-   As the site owner, I want the user to be able to see all recipes added by       the registered users.

### **Design choices**

The chosen design for this website is clear and user-friendly.

In the navigation and throughout the website there are several buttons that lead you back to the homepage.

**Framework**

* Front-end framework, [Materialize](https://materializecss.com/)
was used for this website. It was used to create features such as navigation bar, forms and buttons.

* [JQuery](https://jquery.com/) was used to initialize some Materialize elements.

* Micro framework [Flask](https://flask.palletsprojects.com/en/1.1.x/), 
for this website flask was chosen to build the backend.

**Typography**

- I used [Google Fonts](https://fonts.google.com/specimen/Roboto) for the font style of this project. The font used for this website is Roboto with a backup font of Sans-serif. It is a simple and easy to read font. The font is also easy to read on smaller devices.


**Icons**
-   An existing favicon has been chosen for this
    website [Favicon](https://favicon.io/). 
-   [FontAwesome](https://fontawesome.com/) was used for my forms and buttons, 
    to make it more appealing.

**Colour Scheme**

For this website I chose the color pink. The color comes out nicely for this Asian looking website.

Edit button
color: Green darken-2

Delete button
color: Red darken-2 

Card-Panel
grey lighten-5

Kleuren nog uitwerken!!!

page-header 
color: #880e4f

home-image h1
color: #fff

All Icons
color: #f48fb1 pink lighten-3

Cancel button
color: #bdbdbd grey lighten-1

flash messages
color: #880e4f pink darken-4

---
## **Wireframes**
For the user stories I used [Balsamiq](https://balsamiq.com/) to create a nice and simple layout for the desktop and mobile screen.

Links to the wireframes can be found here:

Desktop Wireframes <br>
1.  <img src="readme-documents/desktop-home.jpg" width="60%" height="60%">
2.  <img src="readme-documents/desktop-signup.jpg" width="60%" height="60%">
3.  <img src="readme-documents/desktop-login.jpg" width="60%" height="60%">
4.  <img src="readme-documents/desktop-addrecipe.jpg" width="60%" height="60%">
5.  <img src="readme-documents/desktop-recipes.jpg" width="60%" height="60%">

Desktop Wireframe, for bigger image click here the following numbers [ (1.) ](readme-documents/desktop-home.jpg)[ (2.) ](readme-documents/desktop-signup.jpg)[ (3.) ](readme-documents/desktop-login.jpg)[ (4.) ](readme-documents/desktop-addrecipe.jpg)[ (5.) ](readme-documents/desktop-recipes.jpg)


Mobile Wireframe <br>
1a. <img src="readme-documents/mobile-home.jpg" width="60%" height="60%">

2a. <img src="readme-documents/mobile-signup.jpg" width="60%" height="60%">

3a. <img src="readme-documents/mobile-login.jpg" width="60%" height="60%">

4a. <img src="readme-documents/mobile-addrecipe.jpg" width="60%" height="60%">

5a. <img src="readme-documents/mobile-recipes.jpg" width="60%" height="60%">


Mobile Wireframe, for bigger image [click here the following numbers [ (1a.) ](readme-documents/mobile-home.jpg)[ (2a.) ](readme-documents/mobile-signup.jpg)[ (3a.) ](readme-documents/mobile-login.jpg)[ (4a.) ](readme-documents/mobile-addrecipe.jpg)[ (5a.) ](readme-documents/mobile-recipes.jpg)


Note: There were some layout changes. The result is not quite the same as the examples of the wireframes.
 
---

## **Features**

***Home/ Index Page***

On this page there is a small introduction about the website. There is also a button on this page to register so you can start adding recipes right away.

***Sign Up Page***

A user must register first to add recipes. You can easily sign up, by creating a username and password.

If a new user tries to register a username and it has already been used. Then a flash banner will appear at the top of the page. That will say “Username already in use!”

When registering and all is well, the user will be greeted with a flash banner at the top of the page. That will say “Registration Successful” 

***Sign In Page***

You can easily sign in, by entering your username and password.

When the users name and/or password do not match, a flash banner will appear at the top of the page. That will say "Incorrect username and/or Password".

When signed in, the page will direct you to the profile page, the user will be greeted with a flash banner at the top of the page. That will say "Welcome username”.

***Profile Page***

The profile page will show the recipes entered by the user.

Only when you are logged in and on the profile page, the user can see the recipes added by this user. The user can delete or edit these recipes.

The delete button will delete the entire recipe. When you press this button, it can no longer be retrieved and you will have to add the recipe again. A pop-up warning will be given if they are sure they want to delete the recipe.

***Recipes Page***

The recipes page can be viewed by registered and unregistered users.

All recipes are displayed in rows of 3.

When you click on one of these images the recipe will be opened/enlarged in a card shape so that it is easy to follow.

There is a search bar on the page to look up recipes, in the index for the mongo database can be searched for recipe_name and/ or recipe_ingredients.

***Add Recipe Page***

The 'Add Recipe' button will direct users to the form to add a recipe.

How to add a recipe is very simple. You can easily fill in the form, under each line you will find a note on how to fill in the form.

-   Recipe Name<br />
    40 characters max
-   Country<br />
    Place the name of the country where the dish comes from
-   Ingredients<br />
    Enter each ingredient on a new line
-   Instructions<br />
    Enter each instruction/step or on a new line
-   Servings<br />
    Enter the number of people the recipe servings (for 2 people just enter "2"), please enter the NUMBER ONLY
-   Duration<br />
    Enter the number of minutes needed to make the recipe (for 25 mins just enter "25"), please enter the NUMBER ONLY
-   URL Image<br />
    Enter the URL for your recipe image
-   Spicy?<br />
    There is an on and off button where you can indicate whether a dish is spicy or not

The form must be completed in full, otherwise it cannot be created.

When the user added the correct information of the recipe, the users can see it on their profile page. The user will see a flash banner at the top of the page. That will say " Recipe Succesfully Added!”.

***Edit Recipe Page***

Users can choose to edit or delete their existing recipes from their profile.

When the edit button is clicked. The completed form (same form as add recipe) appears and can be edited. When you are done editing you can press "edit". The edited data is then saved. Or you press "Go Back" Then the saved data remains the same.

***Log Out***

In the navbar the user can choose to log out. When logging out, a flash banner at the top of the page will say “You have been logged out” 


**Features Left to Implement**
-   Entering an email address for newsletter.
-   Leave a comment underneath a recipe (for account members only).
-   Rate the recipe.
-   ption to download the recipe.

---
## **Technologies**

**Deployment**
  * [Heroku](https://dashboard.heroku.com/)
  * [Git](https://git-scm.com/)
  * [Github](https://github.com/)
  * [Gitpod](https://gitpod.io/)

**Front-End**

- [HTML5](https://en.wikipedia.org/wiki/HTML)
    - To give the page its structure and presenting static data.
    - All HTML files are located within the 'templates' directory.
- [CSS](https://en.wikipedia.org/wiki/CSS)
    - CSS has been used to style and customise the content of this project.
- [Materialize](https://materializecss.com/)
    - This is a framework that I have used to simplify CSS classes, features that have been used and modified include the navbar, responsive design classes, and colors for backgrounds and text.
- [JQuery](https://en.wikipedia.org/wiki/JQuery)
    - JQuery has been used to give the site its functionality as well as making DOM manipulation simpler.

- **Back-end**
- [MongoDB](https://www.mongodb.com/) 
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [werkzeug.security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
      - generate_password_hash
      - check_password_hash
- [datetime](https://docs.python.org/3/library/datetime.html)
      - datetime
- [Python](https://www.python.org/)


---

## **Testing** ##
 
For the main foundation of this website I used Tim Nelson's Code Institute Task Manager Mini-Project. Then I modified it to my website.

**Validators**
The validator that are used for this website are:
    - [HTML Validator](https://validator.w3.org/nu/) - the website works as it should 
    - [JavaScript Validator](https://jshint.com/) the website works as it should
    - [Python Validator](http://pep8online.com/) the website works as it should

## **Deployment**

Github

How to clone code from GitHub:
1.  Go to [Github repository](https://github.com/gwenjo/asian-flavours), navigate to the main page and click Code:
2.  To Clone the repository using HTTPS, under "Clone" click HTTPS.

<img src="readme-documents/clone-github.png" width="50%" height="50%">

3.  Open Git Bash in your local IDE.
4.  Change your current working directory to where you want the cloned directory to be made.
5.  Type `$ git clone`, and paste the URL you copied earlier:
    `$ git clone https://github.com/YOUR-USERNAME/asian-flavours.git`
6. Press enter your local clone will be ready.

### **How to clone this repository to your device**
1.  Create an `env.py` file to store variables, also create .gitignore file to keep these from being displayed:
     - Import os 
     - os.environ.setdefault("IP", "value") 
     - os.environ.setdefault("PORT", "value") 
     - os.environ.setdefault("SECRET_KEY", " value") 
     - os.environ.setdefault("MONGO_URI", " value") 
     - os.environ.setdefault("MONGO_DBNAME", "value")

To properly explain the deployment to Heroku progress. I’ll give a detailed explanation below:

2.  Create a new application using the Heroku dashboard.
3. With `npm install -g Heroku` you can install Heroku.
4. Create a requirements.txt in the console using 
-	`pip3 freeze > requirements.txt`.
5. Create a Procfile via the console using 
`echo web: python app.py > Procfile`.
6. Go to [Heroku]( https://id.heroku.com/login) and login, on your dashboard on the right, click ‘New’ than ‘Create new app’:

<img src="readme-documents/new-app.png" width="50%" height="50%">
    
Create an app name
Choose region closest to you:
Then click ‘Create app’:

<img src="readme-documents/heroku-app-name.png" width="50%" height="50%">
    
3.  Than select:
-   Deploy
-   Deployment method and choose GitHub.
-   Search for a repository to connect to
-   Add your repository name,
-   Click the `Search` button,
-   If the repository is found, click `Connect` to connect to this app:

<img src="readme-documents/deployment-method.png" width="50%" height="50%">

4.  Now go to `Settings`. Click `Reveal Config Vars`.

Here you can fill in the variables from the `env.py` file to securely tell Heroku which variables are required:
- IP
- PORT
- MONGO_DBNAME
- MONGO_URI
- SECRET_KEY

<img src="readme-documents/reveal-config-vars.png" width="50%" height="50%">

5.  After adding the variables push requirements.txt and Profile to the repository
`$ git add requirements.txt`
`$ git commit -m “add requirements.txt”`

`$ git add Profile`
`$ git commit -m ”Profile”`

`$ git push`

6.  Go back to the Heroku page, and press ‘Enable Automatic Deployment’ and then click ‘Deploy Branch’.
    
<img src="readme-documents/deploy-branch.png" width="50%" height="50%">

7.  When Heroku is finished building you will see Your app was successfully deployed.
Click on ‘View’ to launch the app.
    
<img src="readme-documents/view-deploy.png" width="50%" height="50%">
 

## **Credits**
- **Content and Media**
I want to reiterate that THIS PROJECT IS FOR EDUCATION USE ONLY. I have used different websites for different recipes.
The content and images used in this site were obtained from links below:

Content

-   The content of the index.html page is written by me.

Used websites and images

[Char Siu Recipe](https://thewoksoflife.com/chinese-bbq-pork-cha-siu/)

[Pad Thai Recipe](https://www.eatingthaifood.com/pad-see-ew-recipe/)

[Thai Basil Recipe](https://www.eatingthaifood.com/thai-basil-chicken-recipe-pad-kra-pao-gai/)

[Orange Chicken Recipe](https://tasty.co/recipe/original-orange-chicken-by-panda-express)

[Cashew Chicken Recipe](https://www.onceuponachef.com/recipes/cashew-chicken.html)

[Chines Dumplings Recipe](https://mamalovestocook.com/chinese-dumplings-recipe/)

[Steamed Fish With Lime and Garlic Recipe](https://www.eatingthaifood.com/steamed-fish-with-lime-and-garlic-recipe/)


[Springroll Recipe](https://www.allrecipes.com/recipe/245343/authentic-vietnamese-spring-rolls-nem-ran-hay-cha-gio/#:)
-   Image from [Dima Valkov](https://images.pexels.com/photos/4001867/pexels-photo-4001867.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260) - www.pexels.com

[Noodle Soup Recipe](https://www.feastingathome.com/thai-chicken-noodle-soup/)
-   Image from [Quang Nguyen Vinh](https://images.pexels.com/photos/2133989/pexels-photo-2133989.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)

**Resources**

The resources used to create this project:
For the main foundation of this website I used Tim Nelson's Code Institute Task Manager Mini-Project. Then I modified it to my website

### **Acknowledgements**



**THIS PROJECT IS FOR EDUCATIONAL USE ONLY**