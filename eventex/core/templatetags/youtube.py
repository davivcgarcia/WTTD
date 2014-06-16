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
<object width="480" height="385">
    <param name="movie" value="http://www.youtube.com/v/{{ id }}" />
    <param name="allowFullScreen" value="true" />
    <param name="allowscriptaccess" value="always" />
    <embed src="http://www.youtube.com/v/{{ id }}"
      type="application/x-shockwave-flash" allowscriptaccess="always"
      allowfullscreen="true" width="480" height="385">
    </embed>
</object>
"""


def do_youtube(parser, token):
    """
    Implements a custom template tag for Youtube videos.
    """
    try:
        tag_name, id_ = token.split_contents()
    except:
        message = "%r tag requires 1 argument" % token.contents.split()[0]
        raise template.TemplateSyntaxError(message)
    return YoutubeNode(id_)


class YoutubeNode(Node):
    """
    Implements the tag class.
    """
    def __init__(self, id_):
        """
        Object initialization.
        """
        self.id = template.Variable(id_)

    def render(self, context):
        """
        Implements the parent render method.
        """
        try:
            actual_id = self.id.resolve(context)
        except template.VariableDoesNotExist:
            actual_id = self.id

        t = Template(TEMPLATE)
        c = Context(
            {'id': actual_id},
            autoescape=context.autoescape
        )
        return t.render(c)


register = template.Library()
register.tag('youtube', do_youtube)
