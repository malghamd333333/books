from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField

class AddBook(Form):
    title = StringField('Title', [validators.DataRequired()])
    des = StringField('Description', [validators.DataRequired()])
    page = StringField('Page', [validators.DataRequired()])
    pub_year = StringField('Year of Publication', [validators.DataRequired()])
    Auth_id = StringField('Auth ID', [validators.DataRequired()])
    submit = SubmitField('Submit')

class AddAuth(Form):
   name = StringField('Author Name', [validators.DataRequired()])
   des = StringField('Description', [validators.DataRequired()])
   country = StringField('Country', [validators.DataRequired()])
   submit = SubmitField('Submit')
