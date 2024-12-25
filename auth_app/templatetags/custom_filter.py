# custom_filter.py
from django import template

register = template.Library()

@register.filter
def attr(field, attributes):
    """Adds custom attributes to form fields in templates."""
    attrs = attributes.split(",")
    for attr in attrs:
        key, value = attr.split(":")
        field.field.widget.attrs[key.strip()] = value.strip()
    return field

@register.filter
def addclass(field, css_class):
    """Adds a CSS class to form fields."""
    field.field.widget.attrs["class"] = css_class
    return field
