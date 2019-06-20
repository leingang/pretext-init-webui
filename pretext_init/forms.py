from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, Email

class AuthorForm(FlaskForm):
    author_name = StringField('Name',validators=[DataRequired()])
    author_institution = StringField('Institution')
    author_department = StringField('Department')
    author_email = StringField('Email',validators=[Email()])

class NewProjectForm(FlaskForm):
    project_title = StringField('Title',validators=[DataRequired()])
    project_subtitle = StringField('Subtitle')
    project_edition = StringField('Edition')
    project_copyright_year = StringField('Copyright Year')
    project_copyright_holder = StringField('Copyright Holder')
    project_license = RadioField('License')
    authors = FieldList(FormField(AuthorForm),min_entries=1)
    submit = SubmitField('Generate')
