from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="starrating")
def starrating(value):
    # <i class="bi {% if produs.rating > 0 %} {% if produs.rating < 1 %} bi-star-half {% else %} bi-star-fill {% endif %} text-warning {% else %} bi-star {% endif %}  "></i>
    # <i class="bi {% if produs.rating > 1 %} {% if produs.rating < 2 %} bi-star-half {% else %} bi-star-fill {% endif %} text-warning {% else %} bi-star {% endif %}"></i>
    # <i class="bi {% if produs.rating > 2 %} {% if produs.rating < 3 %} bi-star-half {% else %} bi-star-fill {% endif %} text-warning {% else %} bi-star {% endif %}"></i>
    # <i class="bi {% if produs.rating > 3 %} {% if produs.rating < 4 %} bi-star-half {% else %} bi-star-fill {% endif %} text-warning {% else %} bi-star {% endif %}  "></i>
    # <i class="bi {% if produs.rating > 4 %} {% if produs.rating < 5 %} bi-star-half {% else %} bi-star-fill {% endif %} text-warning {% else %} bi-star {% endif %}"></i>
    return_value = ""
    for i in range(5):
        classes = " bi "
        if value > i:
            if value < i+1:
                classes += " bi-star-half "
            else:
                classes += " bi-star-fill "
            classes += " text-warning "
        else:
            classes += "bi-star"

        return_value += f'<i class="{classes}"></i>'
    return mark_safe(return_value)
