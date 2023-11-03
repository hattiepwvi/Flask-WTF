import data
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import re
from flask_bootstrap import Bootstrap5



class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    # 1、代替 html 里的 <input type="submit" value="Log In">
    submit = SubmitField(label='Log In')

    # def validate_password(self, field):
    #     if len(field.data) < 8:
    #         raise ValidationError('Invalid email address.')
    #
    # def validate_email(self, field):
    #     pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    #     if not re.match(pattern, field.data):
    #         raise ValidationError('Field must be at least 8 characters long.')



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "nidedoraameng"

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # login_form.validate_on_submit()
    # 2、相当于 if request.method == "POST"
    # if login_form.validate_on_submit():
    if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
        # print(login_form.email.data)
        return render_template('success_styling.html')
    else:
        return render_template('denied.html')

    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
