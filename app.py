from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.get('/signup')
def signup():
    return render_template('signup.html')


@app.get('/login')
def login():
    return render_template('login.html')

@app.post('/signup')
def create_customer():
    name = request.form['name']
    email = request.form['email']
    dob = request.form['dob']
    gender = request.form['gender']
    password = request.form['password']
    # Add your logic to create a customer here
    return "Customer created successfully!"

@app.post('/login')
def validate_user():
    return "customer logged in successfully"

    
if __name__ == '__main__':
    app.run(debug=True)
