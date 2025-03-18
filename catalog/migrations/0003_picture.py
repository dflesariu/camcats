# Generated by Django 5.1.7 on 2025-03-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_cat_breed_alter_cat_nickname_cat_breed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the cat', max_length=1000)),
                ('image', models.ImageField(upload_to='animal_images')),
            ],
        ),
    ]
