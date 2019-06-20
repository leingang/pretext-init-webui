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
    form = NewProjectForm()
    if form.validate_on_submit():
        # process form
        project = ptx_project.from_form(form)
        yaml = ptx_project.to_xml(project)
        return Response(
            yaml,
            mimetype="text/xml",
            headers={"Content-disposition":"attachment; filename=project.xml"})
    # set up and serve form
    form.project_license.choices = [(e['identifier'],e['title']) for e in app.config['LICENSES']]
    return render_template('new_project.html', title='Initialize Project', form=form)