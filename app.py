# install flast
from flask import Flask
# create instance (singular version of something)
# dunder - variable name with double underscore: name of current funciton 
# dunder is a magic method. 
# used to determine if your code is being run from the command line or if it has been imported into another piece of code
app = Flask(__name__)
# define route
@app.route('/')
def hello_world():
    return 'Hello world'



# to run this in terminatl and get the app running, enter 'export FLASK_APP=app.py' into the command line
# followed by 'flask run' 
# copy the url into your browser to see the app as a web page. 