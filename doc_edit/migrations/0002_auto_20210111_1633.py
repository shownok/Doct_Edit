# Generated by Django 3.1.5 on 2021-01-11 10:33

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('doc_edit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=froala_editor.fields.FroalaField(blank=True, null=True),
        ),
    ]