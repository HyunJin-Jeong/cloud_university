# Generated by Django 3.0.6 on 2020-06-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20200531_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]