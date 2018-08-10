import flask
# start every session like this, creates a instance for that class
app = flask.Flask(__name__)

# Is a wrapper to a function, a decorator
@app.route("/test")  # This code means that the function will only run when you go to site /test.
def function_test():
    return "This is a test"  # Need to return something

flask.redirect(url)  # redirects to another site


flask.render_template("template.html")  # renders a site template which is coded in html ad stored in a template folder
                                        # in the project folder

