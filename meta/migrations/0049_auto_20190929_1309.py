# Generated by Django 2.2.5 on 2019-09-29 16:09

from django.db import migrations

def size_to_tag(apps, schema_editor):
    '''Convert Size to a tag.'''

    Size = apps.get_model('meta', 'Size')
    Tag = apps.get_model('meta', 'Tag')
    TagCategory = apps.get_model('meta', 'TagCategory')

    sizecat = TagCategory.objects.create(name_pt_br='Tamanho', name_en='Size', description_pt_br='Classes de tamanhos.', description_en='Size classes.')

    for size in Size.objects.all():

        newtag = Tag.objects.create(name=size.name, slug=size.slug,
                description_pt_br=size.description_pt_br,
                description_en=size.description_en, parent=sizecat)

        for entry in size.media_set.all():
            newtag.media.add(entry)

        newtag.save()

        print(newtag.id, newtag.name, newtag.media.count())


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0048_auto_20190919_1811'),
    ]

    operations = [
        migrations.RunPython(size_to_tag, reverse_code=migrations.RunPython.noop),
    ]
