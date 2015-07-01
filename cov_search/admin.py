# vim: set fileencoding=utf-8 :
import models
from django.contrib import admin


class SiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'address', 'postalcode', 'phone')
    search_fields = ('name',)


class SeasonAdmin(admin.ModelAdmin):

    list_display = (u'id', 'name')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'programtype')
    search_fields = ('name',)


class ProgramTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class DayAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class AgeGroupAdmin(admin.ModelAdmin):

    list_display = (u'id', 'name')
    search_fields = ('name',)


class InstructorAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class ProgramAdmin(admin.ModelAdmin):

    list_display = (
        'number',
        'name',
        'membership',
        'description',
        'site',
        'season',
        'category',
        'agegroup',
        'agemin',
        'agemax',
        'enrollmin',
        'enrollmax',
        'sessions',
        'numberopen',
        'numberwaitlisted',
        'ignoremaximum',
        'maxenrolledonline',
        'numberenrolledonline',
        'dropin',
        'firstclass',
        'onlinereg',
        'instructor',
        'lac',
        'fee',
        'id',
    )
    list_filter = ('membership', 'dropin', 'firstclass', 'onlinereg', 'lac')
    raw_id_fields = ('site', 'season', 'category', 'agegroup', 'instructor')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Site, SiteAdmin)
_register(models.Season, SeasonAdmin)
_register(models.Category, CategoryAdmin)
_register(models.ProgramType, ProgramTypeAdmin)
_register(models.Day, DayAdmin)
_register(models.AgeGroup, AgeGroupAdmin)
_register(models.Instructor, InstructorAdmin)
_register(models.Program, ProgramAdmin)
