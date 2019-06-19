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
        project = ptx_project.from_form(form)
        yaml = ptx_project.to_yaml(project)
        return Response(
            yaml,
            mimetype="text/yaml",
            headers={"Content-disposition":"attachment; filename=project.yml"})
    return render_template('new_project.html', title='Initialize Project', form=form)