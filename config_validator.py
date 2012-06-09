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
    keys = data.keys()
    print keys
    for key in keys:
        print template.render(title = key, kvps = data[key])

if __name__ == "__main__":
    global data
    data = test_parser.parse("/home/akarsh/Documents/tmp/config2.conf")#render_template()
    render_template(data)
#    print data
