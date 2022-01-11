from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("demo.html")


@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'
@app.route('/start page')
@app.route('/end page')
def start_page():
    return render_template('home.html')



if __name__ == '__main__':
   app.run(debug=True)
#To run from the terminal
# python name.py

#The most popular styling framework is Bootstrap