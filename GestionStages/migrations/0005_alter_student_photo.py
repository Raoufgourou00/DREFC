# Generated by Django 3.2.8 on 2022-01-04 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionStages', '0004_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='userimg.png', null=True, upload_to=''),
        ),
    ]