from flask import render_template, Response

from pretext_init import app
from pretext_init import project as ptx_project
from pretext_init.forms import NewProjectForm


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')

@app.route('/newproject',  methods=['GET', 'POST'])
def project_file():
    form = NewProjectForm(
            authors=[{'name': 'Author 1'},{'name': 'Author 2'}],
            divisions=[{} for i in range(1,5)]
        )
    form.project_license.choices = [(e['identifier'],e['title']) for e in app.config['LICENSES']]
    if form.validate_on_submit():
        # process form
        project = ptx_project.from_form(form)
        xml = ptx_project.to_xml(project)
        return Response(
            xml,
            mimetype="text/xml",
            headers={"Content-disposition":"attachment; filename=project.xml"}
        )
    # if the form hasn't been submitted and validated, render and serve it instead
    return render_template('new_project.html', title='Initialize Project', form=form)