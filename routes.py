from config import app, db, jwt
from flask import jsonify, redirect, render_template, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField, validators
from models.user import User
from models.todo import Todo
from models.token_blocklist import TokenBlocklist

class RegisterForm(FlaskForm):
    email = EmailField('email', [validators.InputRequired(), validators.Email()])
    username = StringField('username', [validators.InputRequired()])
    password = StringField('password', [validators.InputRequired()])

class LoginForm(FlaskForm):
    email = EmailField('email', [validators.InputRequired(), validators.Email()])
    password = StringField('password', [validators.InputRequired()])

class TodoForm(FlaskForm):
    title = StringField('title', [validators.InputRequired()])
    description = StringField('description', [validators.InputRequired()])
    completed = BooleanField('completed')

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None

@app.route('/register', methods=['POST'])
def register():
    # validate_csrf()
    form = RegisterForm(request.form)
    if form.validate():
        password = form.password.data
        hashed_password = generate_password_hash(password).decode('utf-8')
        user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 201, 'message': 'successfully created a new user'}), 201
    else:
        return jsonify({'status': 400, 'message': 'failed to create a new user', 'error': form.errors}), 400

@app.route('/login', methods=['POST'])
def login():
    # validate_csrf()
    form = LoginForm(request.form)
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            return jsonify({'status': 400, 'message': 'failed to login', 'error': form.errors}), 400
        access_token = create_access_token(identity=form.email.data)
        return jsonify({'status': 200, 'message': 'successfully login', 'data': access_token}), 200

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()
    return jsonify({'status': 200, 'message': 'successfully logged out'}), 200

@app.route('/todo', methods=['GET'])
@jwt_required()
def get_todos():
    # validate_csrf()
    todos = Todo.query.all()
    return jsonify({'status': 200, 'message': 'successfully get all todos', 'data': todos}), 200

@app.route('/todo', methods=['POST'])
@jwt_required()
def add_todo():
    # validate_csrf()
    user_email = get_jwt_identity()
    user = User.query.filter_by(email=user_email).first()
    form = TodoForm(request.form)
    if form.validate():
        todo = Todo(title=form.title.data, description=form.description.data, user_id=user.id)
        db.session.add(todo)
        db.session.commit()
        return jsonify({'status': 201, 'message': 'successfully created a new todo'}), 201
    else:
        return jsonify({'status': 400, 'message': 'failed to create a new todo', 'error': form.errors}), 400

@app.route('/todo/<int:todo_id>', methods=['GET'])
@jwt_required()
def get_todo(todo_id):
    # validate_csrf()
    todo = Todo.query.get(todo_id)
    if todo:
        return jsonify({'status': 200, 'message': 'successfully get current todo', 'data': todo}), 200
    else:
        return jsonify({'status': 404, 'message': 'current todo doesn\'t exist'}), 404

@app.route('/todo/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_todo(todo_id):
    # validate_csrf()
    todo = Todo.query.get(todo_id)
    if todo:
        form = TodoForm(request.form)
        if form.validate():
            todo.title = form.title.data
            todo.description = form.description.data
            todo.completed = form.completed.data if form.completed.data else False
            db.session.commit()
            return jsonify({'status': 200, 'message': 'successfully updated current todo'}), 200
        else:
            return jsonify({'status': 400, 'message': 'failed to update current todo', 'error': form.errors}), 400
    else:
        return jsonify({'status': 404, 'message': 'current todo doesn\'t exist'}), 404

@app.route('/todo/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    # validate_csrf()
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'status': 200, 'message': 'successfully deleted current todo'}), 200
    else:
        return jsonify({'status': 404, 'message': 'current todo doesn\'t exist'}), 404