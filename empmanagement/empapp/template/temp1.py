from jinja2 import Template
t = Template("Hello {{ token }}!")
t.render(token="Jinja")
u'Hello Jinja!'