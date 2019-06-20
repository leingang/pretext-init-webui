from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField,\
    SubmitField, FieldList, FormField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Email

class DivisionForm(FlaskForm):
    level = HiddenField('Level',default=1)
    title = StringField('Division')

class AuthorForm(FlaskForm):
    author_name = StringField('Name',validators=[DataRequired()])
    author_institution = StringField('Institution')
    author_department = StringField('Department')
    author_email = StringField('Email',validators=[Email()])

class NewProjectForm(FlaskForm):
    project_title = StringField('Title',validators=[DataRequired()])
    project_subtitle = StringField('Subtitle')
    project_edition = StringField('Edition')
    project_date = StringField('Date')
    project_copyright_year = StringField('Copyright Year')
    project_copyright_holder = StringField('Copyright Holder')
    project_license = RadioField('License')
    project_has_parts = BooleanField('My book has Parts')
    authors = FieldList(FormField(AuthorForm),min_entries=1)
    divisions = FieldList(FormField(DivisionForm),min_entries=1)
    project_chunk = RadioField(
        'One file per',
        choices=[
        ('chapter','Chapter'),
        ('section','Section'),
        ('subsection','Subsection')
    ])
    submit = SubmitField('Generate')
