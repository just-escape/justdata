from django.contrib import admin
from contacts import models


class TagAdmin(admin.ModelAdmin):
    form = models.TagForm
    list_display = ('name',)
    exclude = ()


class PersonAdmin(admin.ModelAdmin):
    form = models.PersonForm
    list_display = ('first_name', 'last_name', 'get_tag_list', 'tel', 'mail')
    search_fields = (
        'first_name', 'last_name', 'tel', 'mail', 'notes', 'tags__name')
    exclude = ()

    def get_tag_list(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])

    get_tag_list.short_description = 'tags'

admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Person, PersonAdmin)
