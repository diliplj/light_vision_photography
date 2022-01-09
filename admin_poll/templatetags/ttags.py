from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css ):
    return field.as_widget(attrs={"class":css,"placeholder":field.name})
