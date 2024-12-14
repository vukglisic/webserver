from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/hello')
def hello_world():
    return 'Hello, Wprld!'

# Run the application on the default port (5000)
if __name__ == '__main__':
    app.run(debug=True)
 