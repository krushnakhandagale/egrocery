# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to E-Grocery Management System"

# if __name__ == '__main__':
# #     app.run(debug=True)


# //new code/

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return "Login Successful"
        else:
            return "Invalid Username or Password"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
