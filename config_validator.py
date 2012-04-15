from jinja2 import Template
import re
class block: 
    """the class def to be used next for storing a blocks information"""
    name = "defualt" #name of block
    kvps ={} #dict of key-value pairs
data = ""
def render_template():
    """Renders a template using the data passed to it"""
    global data
    t = """
{{ title }} {
    {% for kv in kvps %}
    {{kv}} {{kvps[kv]}}
    {% endfor %}
}
"""
    template = Template(t)

    data =  template.render(title='define',kvps={'key1':'value1','key2':'value2'})

def read_file():
    """reads file with the config which is then split back into blocks """
    global data
    print re.findall("[a-zA-Z]+ \{(.+|\n)+\}",data)

if __name__ == "__main__":
    render_template()
    print data
