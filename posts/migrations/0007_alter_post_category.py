# Generated by Django 3.2.4 on 2024-09-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('formal', 'Formal'), ('casual', 'Casual'), ('party', 'Party')], max_length=50),
        ),
    ]
