# Generated by Django 3.2.8 on 2022-01-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionStages', '0031_alter_stage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='legalstatus',
            field=models.CharField(blank=True, choices=[('Publique', 'Publique'), ('Privée', 'Privée'), ('Semi-Publique', 'Semi-Publique')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='status',
            field=models.CharField(choices=[('En Cours', 'En Cours'), ('Annulé', 'Annulé'), ('Validé', 'Validé'), ('Délai Non Respecté', 'Délai Non Respecté')], default='inprogress', max_length=190),
        ),
    ]
