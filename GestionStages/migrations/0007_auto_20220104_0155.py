# Generated by Django 3.2.8 on 2022-01-04 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionStages', '0006_auto_20220104_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='collegelevel',
            field=models.CharField(choices=[('1CPI', '1CPI'), ('2CPI', '2CPI'), ('1CS', '1CS'), ('2CS', '2CS'), ('3CS', '3CS')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='datebirth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='matricule',
            field=models.CharField(max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='userimg.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='placebirth',
            field=models.CharField(max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=190, null=True),
        ),
    ]
