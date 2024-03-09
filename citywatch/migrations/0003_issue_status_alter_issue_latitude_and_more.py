# Generated by Django 5.0.2 on 2024-03-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citywatch', '0002_issuecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('IN_PROGRESS', 'In Progress'), ('RESOLVED', 'Resolved')], default='OPEN', max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issuecategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]