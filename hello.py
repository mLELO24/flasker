from flask import Flask , render_template

#create a flask instance
app = Flask(__name__)
#crete a route decorater
@app.route('/')#main webpage
#def index():
    #return "<h1> Hello Cosmos!</h1>"

def index():
    first_name = "John"
    stuff = "This is <strong>Bold</strong>"
    favourite_pizza = ["pepperoni",'cheese',56]

    return render_template("index.html",first_name = first_name,stuff=stuff, favourite_pizza=favourite_pizza)

if __name__ =='__main__':
    app.run(debug=True)

@app.route('/user/<name>')


def user(name):
    return render_template("user.html",name=name)
#create custom error pages
#invalid url
@app.errorhandler(404)
def  page_not_found(e):
     return render_template("404.html"),404

@app.errorhandler(500)
def  page_not_found(e):
     return render_template("500.html"),404
