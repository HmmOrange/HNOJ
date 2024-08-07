# Generated by Django 3.2.23 on 2024-04-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0192_add_registration_fields_squashed_0192_add_contest_tag_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='enable_grading',
            field=models.BooleanField(default=True, help_text='Whether judges are allowed to grade this problem.', verbose_name='enable grading'),
        ),
    ]
