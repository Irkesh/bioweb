import datetime
from django import template

#register our new library of template functions
register = template.Library()

@register.simple_tag
def todays_date():
 return datetime.datetime.now().strftime("%d %b, %Y")