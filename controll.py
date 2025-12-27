import flask 
from routes.auth import auth_routes
from database.user import initialize_all_databases


app = flask.Flask(__name__)
app.register_blueprint(auth_routes)#Registration of auth 



if __name__ == '__main__':

    app.run()