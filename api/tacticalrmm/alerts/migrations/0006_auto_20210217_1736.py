# Generated by Django 3.1.6 on 2021-02-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_auto_20210212_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerttemplate',
            name='agent_include_desktops',
        ),
        migrations.AddField(
            model_name='alerttemplate',
            name='exclude_servers',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='alerttemplate',
            name='exclude_workstations',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='agent_always_alert',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='agent_always_email',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='agent_always_text',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='check_always_alert',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='check_always_email',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='check_always_text',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='task_always_alert',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='task_always_email',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='task_always_text',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
