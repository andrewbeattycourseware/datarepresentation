from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
   return  redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    return "served by Login"

@app.route('/user')
def getUser():
    return "served by getUser"

@app.route('/user/<int:id>')
def findByIdUser(id):
    return "served by findByIdUser with id = "+str(id)

@app.route('/user', methods=['POST'])
def createUser():
    return "served by createUser"

@app.route("/demo_url_for")
def demoUrlFor():
    returnString = "url For index is "+ url_for('index')
    returnString += "<br/>"
    returnString += "url for findByIdUser "+ url_for('findByIdUser', id=12)
    return returnString

@app.route("/demo_request", methods=['POST', 'GET', 'DELETE'])
def demoRequest():
    return request.method

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)
