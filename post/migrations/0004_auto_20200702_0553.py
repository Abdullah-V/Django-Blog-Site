# Generated by Django 3.0.7 on 2020-07-02 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_elebele'),
    ]

    operations = [
        migrations.DeleteModel(
            name='elebele',
        ),
        migrations.AddField(
            model_name='post',
            name='kategori',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
    ]