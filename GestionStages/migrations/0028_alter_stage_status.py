# Generated by Django 3.2.8 on 2022-01-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionStages', '0027_auto_20220119_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='status',
            field=models.CharField(choices=[('En Cours', 'inprogress'), ('Annulé', 'out'), ('Validé', 'valid'), ('Délai Non Respecté', 'deadline')], default='inprogress', max_length=190),
        ),
    ]