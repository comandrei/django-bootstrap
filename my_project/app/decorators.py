from functools import wraps
from django.shortcuts import redirect

def is_staff(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect("/")
        else:
            return func(request, *args, **kwargs)
    return wrapper