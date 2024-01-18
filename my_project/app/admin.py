from django.contrib import admin

# Register your models here.
from .models import Produs, Favorit, Question, Answer

admin.site.register(Produs)
admin.site.register(Favorit)
admin.site.register(Question)
admin.site.register(Answer)