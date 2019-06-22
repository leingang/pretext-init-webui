from flask import render_template, Response

from pretext_init import app
from pretext_init import project as ptx_project
from pretext_init.forms import NewProjectForm


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')

# Projects
class ProjectXmlResponse(Response):
    def __init__(self,content,**kwargs):
        super().__init__(content,mimetype="text/xml",**kwargs)


class ProjectXmlAttachmentResponse(ProjectXmlResponse):
    def __init__(self,content,filename='project.xml',**kwargs):
        super().__init__(content,**kwargs)
        self.headers['Content-disposition'] \
             = "attachment; filename={}" . format(filename)


@app.route('/newproject',  methods=['GET', 'POST'])
def project_file():
    form = NewProjectForm()
    if form.validate_on_submit():
        # process form
        # TODO: overload NewProjectForm.populate_obj()
        project = ptx_project.from_form(form)
        xml = ptx_project.to_xml(project)
        return ProjectXmlAttachmentResponse(xml)
    # if the form hasn't been submitted and validated, render and serve it instead
    return render_template('new_project.html',
        title='Initialize Project',
        form=form)