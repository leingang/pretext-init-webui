import yaml

class Project(object):
    """A PreTeXt project"""

    def __init__(self, *args, 
        title=None, subtitle=None, 
        edition=None,
        copyright_year=None, copyright_holder=None,
        **kwargs):
        self.title = title
        self.subtitle = subtitle
        self.edition = edition
        self.copyright_year = copyright_year
        self.copyright_holder = copyright_holder

def from_form(form):
    """Create a project from a NewProjectForm"""
    project = Project(
        title = form.project_title.data,
        subtitle = form.project_subtitle.data,
        edition = form.project_edition.data,
        copyright_year = form.project_copyright_year.data,
        copyright_holder = form.project_copyright_holder.data,
    )
    return project


def to_yaml(project):
    """serialize a project as a string of YAML"""
    project_dict = {
        'title': project.title,
        'subtitle': project.subtitle,
        'edition': project.edition,
        'copyright': {
            'year' : project.copyright_year,
            'holder' : project.copyright_holder
        }
    }
    return yaml.dump(project_dict)
