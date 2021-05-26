# **Milestone Project 3**
**Practical Python and Data-Centric Development Milestone Project.**

**Asian Flavours**

This app is the easiest way to find any recipe that you like, and start cooking right away. You can also add your own recipes just as easily. To make the management of the recipes effortless; the admin can remove any spam from the recipes,if needed.

Sign in, get inspired, contribute, cook and enjoy!

[live site Asian Flavour](https://)

![Asian Flavour]()
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

The goal of this full-stack MongoDB-based Flask project is to create a recipe database that allows users (CRUD) to add, read, update, and delete recipes.
Asian Flavors gives access to all recipes in the database for all registered and non-registered users. Registered users can add new recipes, edit and delete their own recipes.

### ** UX **
** First time user **

-	As a first time user, I want an easy navigation website so that add and see     my (new) recipes.
-	As a first user, I want a clear looking website so that the recipes are         easy to follow.
-	As a first user, I want to be able to register.

** Returning Users **

-	As a returning user I want to be able to edit my added recipes.
-   As a returning user, I want to be able to log in and out easily.

** Site owner’s Goal: **

•	As the site owner, I want the user to have an easily accessible site.
•	As the site owner, I want the user to be able to see all recipes added by       the registered users.

### **Design choices**

The goal of the design was to create a website that is user-friendly, has a simple appearance and to provide clear information about (new) recipes.

**Framework**

* Front-end framework, [Materialize](https://materializecss.com/), 
Materialize has been used to for this website. It was used for creating functions such as navigation bar, maps and forms.

* [JQuery](https://jquery.com/) was used for initializing some Materialize elements.

* Micro framework [Flask](https://flask.palletsprojects.com/en/1.1.x/), 
for this website flask was chosen to build the backend.

- **Typography**
- I used [Google Fonts]() for the font style of my project:

- **Icons**
  - I used [Favicon]() to make a unic brand for my website.
  - I used [FontAwesome]() for my forms and buttons.

- **Colour Scheme**

For this website I used different shades of pink. There are also colors of gray.

- **Main colour palette**


---
## **Wireframes**
For the user stories I used [Balsamiq](https://balsamiq.com/) to create a nice and simple layout for the desktop and mobile screen.
Links to the wireframes can be found here:

Desktop Wireframes <br>
<img src="readme-documents/" width="60%" height="60%">

Desktop Wireframe, for bigger image [Click here](readme-documents/)

Tablet Wireframe <br>
<img src="readme-documents/" width="60%" height="60%">

Tablet Wireframe, for bigger image [Click here](readme-documents/)

Mobile Wireframe <br>
<img src="readme-documents/" width="60%" height="60%">

Mobile Wireframe, for bigger image [Click here](readme-documents/)

note: There were some layout changes. The result is not quite the same as the examples of the wireframes.
 
---

## **Features**

- **Features Left to Implement**
email adres invoeren voor nieuwsbrief
comment achterlaten voor account members only

---
## **Technologies**
- **Front-End**

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
  - [MongoDB](https://en.wikipedia.org/wiki/MongoDB) 
    - As the data entered by users can always be different from one to the next, the project uses MongoDB to store its data as MongoDB is a Document Based Database.
  - [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
    - Flask is a framework that allows developers to easily present data in an orderly fashion. All data entered by a user, such as the Recipe Name, is presented to users with a few lines of code embedded into the HTML.
      - Modules from Flask that have been included are:
      - Flask
      - flash
      - render_template
      - redirect
      - request
      - session
      - url_for
      - PyMongo
  - [bson.objectid](https://www.npmjs.com/package/bson-objectid)
      - ObjectId
  - [werkzeug.security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
      - generate_password_hash
      - check_password_hash
  - [datetime](https://docs.python.org/3/library/datetime.html)
      - datetime
  - [Python](https://www.python.org/)
    - Python is working very closely with Flask to manipulate data and HTML across multiple pages within the app.
- **Deployment**
  * [Heroku](https://dashboard.heroku.com/)
  * [Git](https://git-scm.com/)
  * [Github](https://github.com/)
  * [Gitpod](https://gitpod.io/)
- **validators**
  - The validators that have been used on the project are as followed:
    - [HTML Validator](https://validator.w3.org/nu/) - No issues apart from jinja templating
    - [CSS Validator](https://jigsaw.w3.org/css-validator/) - No issues
    - [JavaScript Validator](https://jshint.com/) - No issues 
    - [Python Validator](http://pep8online.com/) - No issues
---
## **Testing**
 
For the main foundation of this website I used Tim Nelson's Code Institute Task Manager Mini-Project.


## **Deployment**

Github

How to clone code from GitHub:

1.  Go to [Github repository](https://github.com/gwenjo/asian-flavours), navigate to the main page and click Code:
2.  To Clone the repository using HTTPS, under "Clone" click HTTPS.
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

    <img src="readme-documents/new-appng" width="50%" height="50%">
    
Create an app name
Choose region closest to you:
Then click ‘Create app’:
    
    <img src="readme-documents/app-name.jpg" width="50%" height="50%">

3.  Than select:
Deploy
Deployment method and choose GitHub.

<img src="readme-documents/app-name.png" width="50%" height="50%">
    
Search for a repository to connect to
Add your repository name,
Click the `Search` button,
If the repository is found, click `Connect` to connect to this app:

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
  The content and images used in this site were obtained from links below:
  Images | Content
 
- **Resources**

  The resources used to create this project:

  - [Handeling Applications Errors -- Flask Documentation](https://flask.palletsprojects.com/en/master/errorhandling/#error-handlers)
  - [(Totorial) Docstring in Python](https://www.datacamp.com/community/tutorials/docstrings-python)
  - [quick start -- Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  - [Adding a favicon -- Flask documentations](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)
  - [Stack Overflow](https://stackoverflow.com/)
### **Acknowledgements**

 

**This project is purely educational, please contact me if there are any issues with Copyright.**