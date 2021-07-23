from flask import Flask, render_template, url_for, flash, redirect,Blueprint, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name =  StringField(validators=[DataRequired()])
    email =  StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/result/<status>')
def registration(status):
    print
    return render_template("result.html")

@bp.route('/',methods=(['POST','GET']))
def new_post():
    form = RegistrationForm()
    if request.method =='POST':
        if form.validate_on_submit():
            print(request.form["name"])
            print(request.form["email"])
            print(request.form["password"])
            print(request.form["date"])
            print("valid")
            # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger) 
            flash(f'{form.name.data} 님 가입 완료!', 'success')
            return redirect(url_for('.registration', status = form.validate_on_submit()))
        else:
            print(request.form["name"])
            print(request.form["email"])
            print(request.form["password"])
    else:
        print("wtf")
    return render_template("register.html",form=form)
 