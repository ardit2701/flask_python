from flask_app import app

@app.route('/')
def hello_world():
   return 'hello World!'
