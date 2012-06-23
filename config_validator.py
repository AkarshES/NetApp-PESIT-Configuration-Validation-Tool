from jinja2 import Template
import re
import test_parser

def render_template(data):
    """Renders a template using the data passed to it"""
    t = \
    """{{ title }} {
    {% for key in kvps.keys() %}{% if kvps[key] is not mapping%}    {{key}} {{kvps[key]}}
    {%else%}    {{key}} {
            {%for k in kvps[key].keys()%} {{k}} {{kvps[key][k]}}
            {%endfor%}
        }{%endif%}{% endfor %}
}
"""
    template = Template(t)
    keys = data.keys()
    for key in keys:
        print template.render(title = key, kvps = data[key])

#def compare(d1,d2):
#    if d1 == d2: return 0
#    elif len(d1) is not len(d1):


if __name__ == "__main__":
    global data
    data1 = test_parser.parse("/home/akarsh/Documents/tmp/config2.conf")
    data2 = test_parser.parse("/home/akarsh/Documents/git/NetApp-PESIT-Configuration-Validation-Tool/output/output.conf")
    render_template(data1)
    print data1 == data2
