from flask import Blueprint, render_template

auth_routes=Blueprint('auth',__name__)#Blueprint for auth_routes
@auth_routes.route('/')# Route to the Loginpage
def loginsite():
    return render_template('system/Login.html')

