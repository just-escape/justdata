from django.contrib import admin
from reviews import models


class CompanyAdmin(admin.ModelAdmin):
    form = models.CompanyForm
    list_display = ('name',)
    exclude = ()


class CityAdmin(admin.ModelAdmin):
    form = models.CityForm
    list_display = ('name',)
    exclude = ()


class PersonAdmin(admin.ModelAdmin):
    form = models.PersonForm
    list_display = ('name',)
    exclude = ()


class ScenarioAdmin(admin.ModelAdmin):
    form = models.ScenarioForm
    list_display = (
        'name',
        'company',
        'city',
        'done',
        'get_reviewers',
        'date',
        'scenery',
        'puzzles',
    )
    exclude = ()

    def get_reviewers(self, obj):
        return ', '.join([str(r) for r in obj.reviewers.all()])

    get_reviewers.short_description = 'reviewers'


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Scenario, ScenarioAdmin)
