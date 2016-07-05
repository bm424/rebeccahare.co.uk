from django import template

from homepage.models import ContactDetails

register = template.Library()


@register.inclusion_tag('contact.html')
def contact_details():
    contact = ContactDetails.objects.first()
    return {'contact': contact}
