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

# Profile Information Page
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Process the form data and update the user profile
        # You can access form data using request.form['input_name']
        # Implement logic to update the user's profile information
        pass
    return render_template('profile.html')


@app.route("/sports")
def reservation():
    return render_template('sports.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

