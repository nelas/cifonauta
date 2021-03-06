# Generated by Django 2.2.5 on 2019-09-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0035_auto_20190914_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxon',
            name='image_count',
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='tsn',
        ),
        migrations.RemoveField(
            model_name='taxon',
            name='video_count',
        ),
        migrations.AlterField(
            model_name='taxon',
            name='common',
            field=models.CharField(blank=True, help_text='Nome popular do táxon.', max_length=256, null=True, verbose_name='nome popular'),
        ),
    ]
