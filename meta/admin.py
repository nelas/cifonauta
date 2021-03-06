from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from meta.models import *
from modeltranslation.admin import TranslationAdmin

# Translation admin.
class FlatPageAdmin(TranslationAdmin):
    pass


class MediaAdmin(TranslationAdmin):
    list_display = ('filepath', 'is_public', 'highlight', 'title', 'caption', 'timestamp')
    list_filter = ('is_public', 'highlight', 'timestamp', 'person', 'tag', 'taxon')


class TagAdmin(TranslationAdmin):
    filter_horizontal = ('media',)
    list_display = ('name', 'description', 'category')


class CatAdmin(TranslationAdmin):
    pass


class CityAdmin(TranslationAdmin):
    pass


class StateAdmin(TranslationAdmin):
    pass


class CountryAdmin(TranslationAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    filter_horizontal = ('media',)


class TaxonAdmin(admin.ModelAdmin):
    filter_horizontal = ('media',)


class ReferenceAdmin(admin.ModelAdmin):
    filter_horizontal = ('media',)


class TourAdmin(TranslationAdmin):
    filter_horizontal = ('media', 'references',)


# Regular models.
admin.site.register(Location)
admin.site.register(Stats)

# Translation models.
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Taxon, TaxonAdmin)
admin.site.register(Reference, ReferenceAdmin)

