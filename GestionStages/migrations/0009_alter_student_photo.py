# Generated by Django 3.2.8 on 2022-01-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionStages', '0008_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='GestionStage/static/images/user.jpg', null=True, upload_to=''),
        ),
    ]