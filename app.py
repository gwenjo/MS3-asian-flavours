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
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_recipes")  
def get_recipes():
    recipes = list(mongo.db.recipes.find()) 
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])  
def search():
    query = request.form.get('query')
    recipes = list(mongo.db.recipes.find({'$text': {'$search': query}}))
    return render_template(
        'recipes.html', recipes=recipes)


@app.route("/register", methods=["GET", "POST"]) 
def register():
    if request.method == "POST":
        # check if username already is in use in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # if username is in use
        if existing_user:
            flash("Username already in use!")
            return redirect(url_for("register"))
        # create username/password
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


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
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])  
def profile(username):
    if not session.get("user"):
        return render_template("404.html")
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find())
    # if existing user display profile
    if session["user"]:
        return render_template("profile.html",
                               username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")  
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])  
def add_recipe():
    if not session.get("user"):
        return render_template("404.html")
        
    if request.method == "POST":
        recipe_spicy = "on" if request.form.get(
            "recipe_spicy") else "off"
        recipe_image = request.form.get("recipe_image") 
        if ".jpg" in recipe_image or ".png" in recipe_image:
            recipe_image = recipe_image
        else:
            recipe_image = "static/images/asian-dish.jpg"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_country": request.form.get("recipe_country"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_spicy": recipe_spicy,
            "recipe_addedby": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Succesfully Added!")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if not session.get("user"):
        return render_template("404.html")

    if request.method == "POST":
        recipe_spicy = "on" if request.form.get(
            "recipe_spicy") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_country": request.form.get("recipe_country"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_spicy": recipe_spicy,
            "recipe_addedby": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Succesfully updated!")
        return redirect(url_for("get_recipes"))
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")  
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted!")
    return redirect(url_for("get_recipes"))


@app.route("/recipe_input/<recipe_id>")  
def recipe_input(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_input.html", recipe=recipe)


# @app.errorhandler(404)  
# def page_not_found(error):
#    return render_template('404.html'), 404


# @app.errorhandler(500) 
# def something_wrong(error):
#    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
            