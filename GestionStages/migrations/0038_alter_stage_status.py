# Generated by Django 3.2.8 on 2022-01-20 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionStages', '0037_alter_stage_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='status',
            field=models.CharField(choices=[('EnCours', 'En Cours'), ('Annule', 'Annulé'), ('Valide', 'Validé'), ('DelaiNonRespecte', 'Délai Non Respecté')], default='inprogress', max_length=190),
        ),
    ]
