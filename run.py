from flask import Flask
from app.routes import bp as routes_bp
from config import Config
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register API routes
app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(debug=True)

