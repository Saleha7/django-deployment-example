# Generated by Django 3.0.3 on 2020-04-07 02:27

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Fname',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Lname',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='user',
            name='Bdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Contact',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]