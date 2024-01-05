# pip install Flask 
# pip install flask-wtf

### initiating flask ### 
# export FLASK_APP=config.py (linux/mac)
# export FLASK_DEBUG=1 (linux/mac)
# flask run

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/profile")
def reservation():
    return render_template('profile.html')

@app.route("/sports")
def reservation():
    return render_template('sports.html')



if __name__  == '__main__':
    app.run(debug=True)
