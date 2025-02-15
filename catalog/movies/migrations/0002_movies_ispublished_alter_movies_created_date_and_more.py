# Generated by Django 4.2.5 on 2024-10-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Time'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.TextField(verbose_name='Movie Description'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.CharField(max_length=100, verbose_name='Movie Image'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Movie Name'),
        ),
    ]
