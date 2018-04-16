from django.template import Library


register = Library()


@register.filter
def odd(value):
    """判断是否为奇数"""
    return value % 2 == 1
