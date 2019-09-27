from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from user import login_bp, register_bp, send_sms_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/test1'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'a'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['get'])
def register_html():
    return render_template('register.html')


app.register_blueprint(login_bp, url_prefix='')
app.register_blueprint(register_bp, url_prefix='')
app.register_blueprint(send_sms_bp, url_prefix='')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
