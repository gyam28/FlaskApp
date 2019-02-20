from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (DataRequired, Email, Length,
                                EqualTo, ValidationError)
from app.auth.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2,max=20, message="Must be more than 2 and less than  20 characters long.")])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(), Length(min=4, message="Must containt at least 4 characters and a symbol.")])
    confirm_password = PasswordField("Confirm your password",validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Sign up")

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Already registered with this username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Already registered with this email.")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("Wrong email. Please try again.")

    def validate_password(self, password):
        user=User.query.filter_by(password=password.data).first()
        if user:
            raise ValidationError("Wrong password. Please try again.")

class UpdateAccount(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2,max=20, message="Must be more than 2 and less than  20 characters long.")])
    email = StringField("Email", validators=[DataRequired(),Email()])
    picture = FileField("Upload your picture", validators=[FileAllowed(['jpg','png','jpeg','gif'])])
    submit = SubmitField("Update")

    def validate_user(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Already registered with this username.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Already registered with this email.")


#HOMEWORK to do in OOP
    # def validate_email()
    #
    # def validate_password()
