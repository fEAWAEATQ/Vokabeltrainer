import flask 
from routes.auth import auth_routes
from database.user import initialize_all_databases, get_user, add_user


app = flask.Flask(__name__)
app.register_blueprint(auth_routes)#Registration of auth 



if __name__ == '__main__':
    initialize_all_databases()#Initialization of all databases
    add_user("admin", "secret", 10)
    add_user("asdf","bb",22)
    user = get_user("asdf")
    print(user["username"], user["rank"])

    app.run()