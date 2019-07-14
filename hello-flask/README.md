# Getting started with python flask (Windows)

## Creating an Anaconda virtual environment
* Create a new folder where all your project files will be present.<br/>
  `C:\SAMS\workspace\python\flask-training`<br/>
* Run the below command to create a virtual environment with python version 3.5 <br/>
  `conda create -n flask-demo python=3.5` <br/>
  You will be prompted Proceed [y]/n to. Default selection is yes, so just press enter to create your new environment.
* Once environment is created run the below command to activate it.<br/>
  `activate flask-demo`<br/>

## What is flask?
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[3] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself.
Source: Wikipedia


## Installing flask
`pip install flask`

Now that we have our environment and nerdy definition in place let move on to creating a simple hello world program in flask.

## Creating flask app
Create a file app.py inside flask-training folder, it will initialize and run out flask server.

Things you need to understand
* The import statement import the Flask class that will be used to initialize our application. </br>
* `app = Flask(__name__)`</br>
  You should use __name__ because depending on if it is started as application or imported as module the name will be different   ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on.
*	`@app.route('/')` : The route() decorator in Flask app is used to bind URL to a function, like index method our case. All request like <our-domain>:<port>/ will be rendered using the index() method.
*	`name = request.args.get("name")` : This will fetch request param name from request.
*	`return "Hello "+name+"!"` : This sends back the response to browser
*	`app.run(port=5000,debug=True)` : This will start the flask application on port number 500. This code is enclosed within `if __name__ == '__main__':` to make sure application would only execute if this module was called interactively and would not execute if this module was imported into another module. Debug=True will enable flask to detect and change in code and automatically restart the server to reflect the change.

## Running flask app
Assuming you are still in flask-training folder in your anaconda command prompt Enter “python app.py” and wait for the server to start. You would get below type of logs once the server is up and running.</br>

`
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 318-157-857
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
`
Accessing the server from browser
Hit the url http://127.0.0.1:5000/?name=saurav on any browser. You should get something like below.

![alt text](https://github.com/skynet357/flask-tutorials/blob/master/hello-world/brower_output.JPG)
