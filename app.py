from flask import Flask, request, render_template, redirect, url_for

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


accounts = {
        "Mauve": "Purple",
        "Eminence": "Tyrian",
        "Turquoise": "Fuschia"
}
facebook_friends=["Pink", "Teal", "Rosewater", "Ruby", "Violet", "Magenta"]

@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        post_username = request.form["username"]
        post_password = request.form["password"]
        try:
            if post_username in accounts and accounts[post_username] == post_password:
                return redirect(url_for('home'))
        except:
            return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html', friends=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET','POST'])
def friend_exists(name):
    return render_template('friend_exists.html', infriends=(name in facebook_friends))

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
