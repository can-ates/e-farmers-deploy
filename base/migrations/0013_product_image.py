# Generated by Django 3.1.7 on 2021-06-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_user_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to=''),
        ),
    ]
