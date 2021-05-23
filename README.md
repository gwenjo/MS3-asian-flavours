# **Milestone Project 3**
**Practical Python and Data-Centric Development Milestone Project.**

**Asian Flavours**

This app is the easiest way to find any recipe that you like, and start cooking right away. You can also add your own recipes just as easily. To make the management of the recipes effortless; the admin can remove any spam from the recipes,if needed.

Sign in, get inspired, contribute, cook and enjoy!

To view the live version of the site, please click [here]()

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
[Balsamiq Wireframes](https://balsamiq.com/wireframes/) was used to create all wireframes for the project.

 
---

## **Features**

- **Features Left to Implement**

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
 
## **Deployment**
This project is stored in a GitHub repository and hosted on Heroku.
### **How to deploy to Github**
1. Click [here](") to get to the projects repository.

2. Click on 'Settings' to the far right in navigation menu below your repository name.

3. Scroll down to 'GitHub Pages' and select 'master branch' as the source.

4. Click save.

5. The link to the site hosted on GitHub Pages should appear at the top of the section.

### **How to clone this repository in order to run the code locally on your machine**
1. Click [here]() to get to the projects repository.

2. Click "Clone or Download".

3. Click the "copy" icon.

4. Open Git Bash in your local IDE.

5. Change your current working directory to where you want the cloned directory to be made.

6. Type `$ git clone` and then paste the URL you copied earlier.

   `git clone https://github.com/USERNAME/REPOSITORY`
7. When you press enter your local clone will be ready.
### **How to clone this repository in order to run the code locally on your machine**

1. Created a new application using the Heroku dashboard.

2. Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).

3. Install Heroku via the console using 'npm install -g Heroku'.

4. Log into Heroku via the console using 'heroku login' and follow the on screen instructions to log in.

5. Create a requirements.txt via the console using 'pip3 freeze > requirements.txt'.

6. Create a Procfile via the console using 'echo web: python app.py > Procfile'.

7. Connect GitHub to Heroku via the console using 'heroku git:remote a creative-hub'

8. Commit all files in your project via the console using 'git add .' and 'git commit -m "Message"'.

9. Deploy your project to Heroku via the consol using 'git push heroku master'.

### **Running the application locally using Gitpod**

1. Clone the repository as outlined above and upload it to GitPod.

2. Install the necessary libraries specified in the requirements.txt.

3. Set your environment variables by creating and adding them into a env.py file.

4. Create a .gitignore file in the root directory and add the env.py file to avoid it being pushed to GitHub.

5. Import the env.py file into the app.py file.

6. Run the application.

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