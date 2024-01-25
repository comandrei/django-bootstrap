from django.contrib import admin

# Register your models here.
from .models import Produs, Favorit, Question, Answer, UserProfile, Curs, Student, Recenzie, Elev, ElevCurs

admin.site.register(Produs)
admin.site.register(Favorit)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserProfile)
admin.site.register(Curs)
admin.site.register(Student)
admin.site.register(Recenzie)
admin.site.register(Elev)
admin.site.register(ElevCurs)