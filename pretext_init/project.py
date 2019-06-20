from lxml import etree
import yaml

class Project(object):
    """A PreTeXt project"""

    def __init__(self, *args, 
        title=None, subtitle=None, 
        edition=None,
        copyright_year=None, copyright_holder=None,
        license=None,
        **kwargs):
        self.title = title
        self.subtitle = subtitle
        self.edition = edition
        self.copyright_year = copyright_year
        self.copyright_holder = copyright_holder
        self.license = license

def from_form(form):
    """Create a project from a NewProjectForm"""
    project = Project(
        title=form.project_title.data,
        subtitle=form.project_subtitle.data,
        edition=form.project_edition.data,
        copyright_year=form.project_copyright_year.data,
        copyright_holder=form.project_copyright_holder.data,
        license=form.project_license.data
    )
    return project

def to_xml(project):
    """Serialize a project as a string of XML"""
    root = etree.Element('book')
    root.set('{http://www.w3.org/XML/1998/namespace}id','main')
    metadata = etree.SubElement(root,'metadata')
    title = etree.SubElement(metadata,'title')
    title.text = project.title
    subtitle = etree.SubElement(metadata,'subtitle')
    subtitle.text = project.subtitle
    edition = etree.SubElement(metadata,'edition')
    edition.text = project.edition
    copyright = etree.SubElement(metadata,'copyright')
    copyright_year = etree.SubElement(copyright,'year')
    copyright_year.text = project.copyright_year
    copyright_holder = etree.SubElement(copyright,'holder')
    copyright_holder.text = project.copyright_holder
    license = etree.SubElement(metadata,'license')
    license.text = project.license
    return etree.tostring(root,pretty_print=True)

def to_yaml(project):
    """Serialize a project as a string of YAML
    
    Don't use.  We're going with XML for now.
    """
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
