from django import template
import base64

register = template.Library()

@register.filter(name='encryptb64')
def encryptb64(value):
	return base64.b64encode(value.encode('utf8'))
        
@register.filter(name='times')
def times(number):
	return range(1, number+1)   