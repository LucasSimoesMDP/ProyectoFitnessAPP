# Generated by Django 4.2.3 on 2023-07-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
