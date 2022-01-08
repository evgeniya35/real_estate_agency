# Generated by Django 2.2.24 on 2022-01-03 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    def fill_new_building(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        for flat in Flat.objects.all():
            flat.new_building = flat.construction_year >= 2015
            flat.save()

    operations = [
        migrations.RunPython(fill_new_building),
    ]

