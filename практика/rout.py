from flask import Flask, Blueprint, render_template, jsonify

app = Flask(__name__)

class HtmlResponse:
    def __init__(self, content):
        self.content = content

class JsonResponse:
    def __init__(self, data):
        self.data = data

def before_middleware():
    print("Executing before middleware")

def after_middleware():
    print("Executing after middleware")

def create_router():
    router = Blueprint('router', __name__)

    @router.route('/about')
    def about():
        before_middleware()
        response = HtmlResponse("<h1>About Us</h1>")
        after_middleware()
        return response.content

    @router.route('/company')
    def company():
        before_middleware()
        response = HtmlResponse("<h1>Our Company</h1>")
        after_middleware()
        return response.content

    @router.route('/posts/<int:post_id>')
    def post(post_id):
        before_middleware()
        response = JsonResponse({"post_id": post_id, "title": "Sample Post"})
        after_middleware()
        return jsonify(response.data)

    return router

if __name__ == '__main__':
    app.register_blueprint(create_router())

    @app.route('/')
    def home():
        return "<h1>Welcome to the Home Page</h1>"

    app.run(debug=True)

