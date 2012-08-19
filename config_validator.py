from jinja2 import Template
import re
import test_parser
import argparse
import os
import sys

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

def compare(old,new):
    mod = old
    if len(old) is not len(new):
        temp = new.keys()
        for key in old.keys():
            temp.pop(temp.index(key))
        print("The following blocks are missing in your config.\n Please select an option for changing the configuratoin to the optimal value. [Y/n]")
        print(temp)
        dec = str(raw_input())

    

if __name__ == "__main__":
    global data
    parser = argparse.ArgumentParser(description = "Accepts addresses of config file")
    parser.add_argument("--path1",dest = "path1")
    parser.add_argument("--path2",dest = "path2")
    paths = parser.parse_args()
    if paths.path1 is None or paths.path2 is None:
        print("Paths incomplete")
        sys.exit()
    if not os.path.exists(paths.path1) or not os.path.exists(paths.path2):
        print("Files do not exist.")
        sys.exit()
    data1 = test_parser.parse(paths.path1)#"/home/akarsh/Documents/tmp/config2.conf")
    data2 = test_parser.parse(paths.path2)#"/home/akarsh/Documents/git/NetApp-PESIT-Configuration-Validation-Tool/output/output.conf")
    render_template(data1)
    print data1 == data2
