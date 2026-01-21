from flask import Blueprint, render_template, request, jsonify, session
from database.user import get_user
from werkzeug.security import check_password_hash
auth_routes=Blueprint('auth',__name__)#Blueprint for auth_routes
@auth_routes.route('/')# Route to the Loginpage
def index():
    return render_template('system/Login.html')
@auth_routes.route('/auth/login',methods=['POST'])
def login():
    data=request.get_json()
    if data is None:
        return jsonify({'error': 'No input data provided'}), 400
    username=data.get('username')
    password=data.get('password')
    if not all([username,password]):
        return jsonify({'error':'username and password required'}), 400
    user=get_user(username)
    if user is None or not check_password_hash(user.password,password):
        return jsonify({'error':'invalid credentials'}),401
    session['user_id']=user.id
    session['username']=user.username
    return jsonify({
        "message": "login successful",
        "username": user.username
    }), 200



@auth_routes.route('/auth/logout',methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message':'logged out'}), 200
    


