import flask 
from routes.auth import auth_routes
from database.user import Initialize_All_Databases,Get_User,Add_User


app = flask.Flask(__name__)
app.register_blueprint(auth_routes)#Registration of auth 



if __name__ == '__main__':
    Initialize_All_Databases()
    Add_User("admin", "secret", 10)

    user = Get_User("admin")
    print(user["username"], user["rank"])

    app.run()