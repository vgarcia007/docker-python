#Import the flask module
from flask import Flask
import sys

#Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

#Create a route decorator to tell the application, which URL should be called for the #described function and define the function
def ConsoleLog(text):
    print(text, file=sys.stderr)

@app.route('/')
def home():
    return " D’oh!"


@app.route('/test')
def test():
    ConsoleLog('Hello world!')
    return "nix"

#Create the main driver function
if __name__ == '__main__':
    #call the run method
    app.run(host='0.0.0.0')
