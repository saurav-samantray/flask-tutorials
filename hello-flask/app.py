from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get("name")
    if name == None:
        name = "flask!"
    return "Hello "+name+"!"
	
if __name__ == '__main__':
    app.run(port=5000,debug=True)