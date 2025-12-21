import flask 
from routes.auth import auth_routes


app = flask.Flask(__name__)
app.register_blueprint(auth_routes)#Registration of auth 




if __name__ == '__main__':
    app.run(debug=True)