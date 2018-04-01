from django import template
import base64

register = template.Library()

@register.filter(name='encryptb64')
def encryptb64(value):
	return base64.b64encode(value.encode('utf8'))
    