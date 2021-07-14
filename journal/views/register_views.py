from flask import Flask, render_template, url_for, flash, redirect,Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username =  StringField("아이디", 
                            validators=[DataRequired(), Length(min=4, max=20)])
    email =  StringField("이메일", 
                            validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호", 
                            validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField("비밀번호 확인", 
                            validators=[DataRequired(), EqualTo("password")] )
    submit = SubmitField("가입")

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/result/<status>')
def registration(status):
    return render_template("result.html")

@bp.route('/',methods=(['POST','GET']))
def new_post():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.username,form.email,form.password)
        print("valid")
        # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger) 
        flash(f'{form.username.data} 님 가입 완료!', 'success')
        return redirect(url_for('.registration', status = form.validate_on_submit()))
    else:
        print("not valid")
        print(form.username,form.email,form.password)
    return render_template("register.html",form=form)
 