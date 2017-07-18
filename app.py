from flask import Flask

from app.routes import init_api_routes

# create the Flask application
app = Flask(__name__)

init_api_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
