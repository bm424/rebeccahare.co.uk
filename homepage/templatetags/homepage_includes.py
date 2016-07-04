from django import template

from homepage.models import ContactDetail

register = template.Library()


@register.inclusion_tag('contact.html')
def contact_details():
    contact = ContactDetail.objects.first()
    return {'contact': contact}
