# Generated by Django 3.0.6 on 2020-06-18 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0017_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='videofile',
        ),
        migrations.AddField(
            model_name='video',
            name='professor',
            field=models.ForeignKey(default=4, limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CourseProfessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.Course')),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.Semester')),
            ],
        ),
    ]