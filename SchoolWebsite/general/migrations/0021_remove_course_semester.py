# Generated by Django 3.0.6 on 2020-06-30 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0020_remove_course_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
    ]