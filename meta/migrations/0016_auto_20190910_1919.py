# Generated by Django 2.2.5 on 2019-09-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0015_auto_20190910_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='Fotos associadas a este autor.', to='meta.Image', verbose_name='fotos'),
        ),
        migrations.AlterField(
            model_name='author',
            name='videos',
            field=models.ManyToManyField(blank=True, help_text='Vídeos associados a este autor.', to='meta.Video', verbose_name='vídeos'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='Fotos associadas à esta referência.', to='meta.Image', verbose_name='fotos'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='videos',
            field=models.ManyToManyField(blank=True, help_text='Vídeos associados à esta referência.', to='meta.Video', verbose_name='vídeos'),
        ),
        migrations.AlterField(
            model_name='source',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='Fotos associadas a este especialista.', to='meta.Image', verbose_name='fotos'),
        ),
        migrations.AlterField(
            model_name='source',
            name='videos',
            field=models.ManyToManyField(blank=True, help_text='Vídeos associados a este especialista.', to='meta.Video', verbose_name='vídeos'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='Fotos associadas a este marcador.', to='meta.Image', verbose_name='fotos'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='videos',
            field=models.ManyToManyField(blank=True, help_text='Vídeos associados a este marcador.', to='meta.Video', verbose_name='vídeos'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='Fotos associadas a este táxon.', to='meta.Image', verbose_name='fotos'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='videos',
            field=models.ManyToManyField(blank=True, help_text='Vídeos associados a este táxon.', to='meta.Video', verbose_name='vídeos'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='Fotos associadas a este tour.', to='meta.Image', verbose_name='fotos'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='references',
            field=models.ManyToManyField(blank=True, help_text='Referências associadas a este tour.', to='meta.Reference', verbose_name='referências'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='videos',
            field=models.ManyToManyField(blank=True, help_text='Vídeos associados a este tour.', to='meta.Video', verbose_name='vídeos'),
        ),
    ]