# Generated by Django 3.2.8 on 2022-01-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionStages', '0030_alter_company_legalstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='status',
            field=models.CharField(choices=[('inprogress', 'En Cours'), ('out', 'Annulé'), ('valid', 'Validé'), ('deadline', 'Délai Non Respecté')], default='inprogress', max_length=190),
        ),
    ]
