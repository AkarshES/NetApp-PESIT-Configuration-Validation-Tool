from jinja2 import Template
import re
import test_parser

def render_template(data):
    """Renders a template using the data passed to it"""
    t = """
{{ title }} {
    {% for kv in kvps %}{%if kv[0]%}
        {{kv[0]}} {{kv[1]}}
    {%else%}
        {{kv.keys()[0]}} {
            {%for key in kv[kv.keys()[0]]%}
                 {{key}} {{kv[kv.keys()[0][key]]}}
            {%endfor%}
        }{%endif%}{% endfor %}
}
"""
    template = Template(t)
    print template.render(title = data.keys()[0],kvps=data[data.keys()[0]])
#    data =  template.render(title='define',kvps={'key1':'value1','key2':'value2'})

def read_file():
    """reads file with the config which is then split back into blocks """
    global data
    print re.findall("[a-zA-Z]+ \{(.+|\n)+\}",data)

if __name__ == "__main__":
    global data
    data = test_parser.parse()#render_template()
    render_template(data)
#    print data
