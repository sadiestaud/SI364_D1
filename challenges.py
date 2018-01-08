from flask import Flask, request
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Task 2
# Write a return statement such that it displays 'Welcome to <course_name>'
# when you navigate to localhost:5000/course/<course_name>
# Remember to get rid of the pass statement
@app.route('/course/<course>')
def course(course):
   return 'Welcome to {} on localhost:5000/course/{}'.format(course,course)

# Task 3.1
# Edit the HTML form such that form data is sent to localhost:5000/result using POST method
@app.route('/form')
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<form action="http://localhost:5000/result" method="POST">
  INGREDIENT:<br>
  <input type="text" name="ingredient">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
# Note that by default eggs would be entered in the input field
    return s


## Task 3.2
## Modify the function code and return statement
## to display recipes for the ingredient entered
@app.route('/result',methods = ['POST', 'GET'])
def displayData():
    baseurl = "http://www.recipepuppy.com/api"
    if request.method == 'POST':
      ingredient = request.form['ingredient']
      param_dict = {'i':ingredient}
      req = requests.get(baseurl, params = param_dict) #response object
      diction = req.json()
      list_of_recipies = []
      for recipe in diction['results']:
        list_of_recipies.append(recipe['title'])
      return str(list_of_recipies)

    if request.method == 'GET':
      ingredient = request.args['ingredient']
      param_dict = {'i':ingredient}
      req = requests.get(baseurl, params = param_dict) #response object
      diction = req.json()
      list_of_recipies = []
      for recipe in diction['results']:
        list_of_recipies.append(recipe['title'])
      return str(list_of_recipies)




      
      



      


## Task 4
## Note : Since this is a dyanmic URL, recipes function should recieve a paramter called `ingrdient` 
@app.route('/recipe/<ingredient>')
def recipes():
  pass

if __name__ == '__main__':
    app.run()
