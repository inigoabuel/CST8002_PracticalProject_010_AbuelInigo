from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "secret123"

    from app.views.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
