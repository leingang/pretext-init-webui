from lxml import etree
import yaml

# Licenses
# array of dicts.  The keys of each dict are:
# * title: (full) title of the license
# * identifier: (short) initialism
# * uri: URI/URL of the license
LICENSES = [
    {'title': 'Attribution-ShareAlike 2.0 Generic',
     'identifier': 'CC BY-SA 2.0',
     'uri': 'https://creativecommons.org/licenses/by-sa/2.0/'},
    {'title': 'Attribution-NonCommercial-ShareAlike 2.0 Generic',
     'identifier': 'CC BY-NC-SA 2.0',
     'uri': 'https://creativecommons.org/licenses/by-nc-sa/2.0/'},
    {'title': 'GNU Free Documentation License',
     'identifier': 'GFDL',
     'uri': 'https://www.gnu.org/licenses/fdl-1.3.en.html'},
]

class Project(object):
    """A PreTeXt project"""

    def __init__(self, *args, 
        title=None, subtitle=None, 
        edition=None,
        copyright_year=None, copyright_holder=None,
        license=None,
        authors=None,
        **kwargs):
        self.title = title
        self.subtitle = subtitle
        self.edition = edition
        self.copyright_year = copyright_year
        self.copyright_holder = copyright_holder
        self.license = license
        if authors is None:
            self.authors = []
        else:
            self.authors = authors


def from_form(form):
    """Create a Project from a NewProjectForm"""
    authors = []
    for author_form in form.authors:
        author = {
            'name': author_form.author_name.data,
            'institution': author_form.author_institution.data,
            'department': author_form.author_department.data,
            'email': author_form.author_email.data
        }
        authors.append(author)
    project = Project(
        title=form.project_title.data,
        subtitle=form.project_subtitle.data,
        edition=form.project_edition.data,
        copyright_year=form.project_copyright_year.data,
        copyright_holder=form.project_copyright_holder.data,
        license=form.project_license.data,
        authors=authors
    )
    project.outline = [
        (division_form.title.data, int(division_form.level.data))
        for division_form in form.divisions
    ]
    return project

def to_xml(project):
    """Serialize a Project as a string of XML"""
    root = etree.Element('book')
    XML_ID = '{http://www.w3.org/XML/1998/namespace}id'
    root.set(XML_ID,'main')
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
    for author in project.authors:
        author_element = etree.Element('author')
        author_children = {}
        for field in ['name','institution','department','email']:
            author_children['field'] = etree.SubElement(author_element,field)
            author_children['field'].text = author[field]
        metadata.append(author_element)
    outline = etree.SubElement(root,'outline')
    labels=[('chapter','chap'),('section','sec'),('subsection','subsec')]
    current_level = 0
    current_element = outline
    level_stack = []
    def get_id(short,lst):
        return short + '-'.join(str(i) for i in lst)
    for (title,level) in project.outline:
        tag,short_tag = labels[level-1]
        element = etree.Element(tag)
        if (level > current_level):            
            # add as a child
            parent = current_element
            level_stack.append(1)
        else:
            # add as a sibling or ancestor
            # the range starts from 0, so if level = current_level, we go up
            # exactly once.  The new element's parent is the same as the
            # current element's parent.  Otherwise, we go up a few more times
            # on the tree.
            for _ in range(current_level - level+1):
                current_element = current_element.getparent()
                v = level_stack.pop()
            level_stack.append(v+1)
            parent = current_element
        element.set(XML_ID,get_id(short_tag,level_stack))
        etree.SubElement(element,'title').text = title
        parent.append(element)
        current_level = level
        current_element = element
    return etree.tostring(root,xml_declaration=True,pretty_print=True)

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
