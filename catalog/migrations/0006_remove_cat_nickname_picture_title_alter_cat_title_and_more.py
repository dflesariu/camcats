# Generated by Django 5.1.7 on 2025-03-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_picture_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='nickname',
        ),
        migrations.AddField(
            model_name='picture',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='title',
            field=models.CharField(help_text='Made up nickname for the cat when we do not know its actual name', max_length=200),
        ),
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.TextField(help_text='Enter a brief description of the image', max_length=1000),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='cat_images'),
        ),
    ]
