# Generated by Django 3.2.12 on 2022-08-12 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0003_auto_20220812_0256'),
        ('template', '0003_alter_templates_name_template'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='templates',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='templates',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='style.style'),
        ),
        migrations.AlterField(
            model_name='templates',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
