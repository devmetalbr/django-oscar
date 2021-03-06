from django import template

register = template.Library()


@register.simple_tag
def shipping_charge(method, basket, postcode):
    """
    Template tag for calculating the shipping charge for a given shipping
    method and basket, and injecting it into the template context.
    """
    return method.calculate(basket, postcode)


@register.simple_tag
def shipping_charge_discount(method, basket, postcode=None):
    """
    Template tag for calculating the shipping discount for a given shipping
    method and basket, and injecting it into the template context.
    """
    return method.discount(basket, postcode)


@register.simple_tag
def shipping_charge_excl_discount(method, basket, postcode):
    """
    Template tag for calculating the shipping charge (excluding discounts) for
    a given shipping method and basket, and injecting it into the template
    context.
    """
    return method.calculate_excl_discount(basket, postcode)
