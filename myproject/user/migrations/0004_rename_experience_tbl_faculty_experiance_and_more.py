# Generated by Django 5.1.1 on 2024-09-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_pictur_tbl_infra_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_faculty',
            old_name='experience',
            new_name='experiance',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Mobile',
            field=models.CharField(max_length=22, null=True),
        ),
    ]