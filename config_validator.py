from jinja2 import Template
import re
import test_parser

def render_template(data):
    """Renders a template using the data passed to it"""
    t = \
    """{{ title }} {
    {% for kv in kvps %}{%if kv[0]%}    {{kv[0]}} {{kv[1]}}
    {%else%}    {{kv.keys()[0]}} {
            {%for key in kv[kv.keys()[0]]%} {{key}} {{kv[kv.keys()[0]][key]}}
            {%endfor%}
        }{%endif%}{% endfor %}
}
"""
    template = Template(t)
    keys = data.keys()
    for key in keys:
        print template.render(title = key, kvps = data[key])

if __name__ == "__main__":
    global data
    data1 = test_parser.parse("/home/akarsh/Documents/tmp/config2.conf")
    data2 = test_parser.parse("/home/akarsh/Documents/git/NetApp-PESIT-Configuration-Validation-Tool/output/output.conf")
    render_template(data1)
    print data1 == data2
