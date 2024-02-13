from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

# Register your models here.
from .models import Produs, Favorit, Question, Answer, UserProfile, Curs, Student, Recenzie, Elev, ElevCurs, Post, Producator
from .forms import ProdusForm


admin.site.register(Favorit)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserProfile)
admin.site.register(Curs)

admin.site.register(Recenzie)
admin.site.register(Elev)
admin.site.register(ElevCurs)
admin.site.register(Post)
admin.site.register(Producator)

def retrage_din_oferta(modeladmin, request, queryset):
    # for produs in queryset:
    #     produs.stoc = 0
    #     produs.save()

    queryset.update(stoc=0)

class ProdusAdmin(admin.ModelAdmin):
    search_fields = ("titlu", "producator__nume")
    list_display = ("producator", "titlu", "stoc")
    list_filter = ("producator", )
    list_per_page = 3
    change_list_template = "admin/produs_change_list.html"
    change_form_template = "admin/produs_change_form.html"
    list_select_related = ("producator", )
    list_editable = ("titlu", "stoc")
    actions = (retrage_din_oferta, )
    form = ProdusForm

    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #     return super().get_queryset(request).select_related("producator")

admin.site.register(Produs, ProdusAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("nume", "an")
    list_filter = ("an", )
    fieldsets = (
        ('Date Personale', {'fields': ["nume", "telefon"]}),
        ('Date scoala', {'fields': ["an", "cursuri"], 'classes': ('collapse', )})
    )

admin.site.register(Student, StudentAdmin)