# Generated by Django 3.2.12 on 2022-08-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0003_auto_20220812_0256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Style Boards'},
        ),
        migrations.AddField(
            model_name='style',
            name='name_template',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
