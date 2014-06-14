# coding: utf-8
"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django import template
from django.template import Context, Template, Node


TEMPLATE = """
<object id="__sse{{ id }}" width="425" height="355">
  <param name="movie"
    value="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc={{ doc }}" />
  <param name="allowFullScreen" value="true"/>
  <param name="allowScriptAccess" value="always"/>
  <embed name="__sse{{ id }}"
    src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc={{ doc }}"
    type="application/x-shockwave-flash"
    allowscriptaccess="always"
    allowfullscreen="true"
    width="425"
    height="355">
  </embed>
</object>
"""


def do_slideshare(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, id_, doc = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 2 arguments" % token.contents.split()[0]
    return SlideShareNode(id_, doc)


class SlideShareNode(Node):
    def __init__(self, id_, doc):
        self.id = template.Variable(id_)
        self.doc = template.Variable(doc)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except template.VariableDoesNotExist:
            actual_id = self.id

        try:
            actual_doc = self.doc.resolve(context)
        except template.VariableDoesNotExist:
            actual_doc = self.doc

        t = Template(TEMPLATE)
        c = Context({'id': actual_id, 'doc': actual_doc}, autoescape=context.autoescape)
        return t.render(c)


register = template.Library()
register.tag('slideshare', do_slideshare)
