# Generated by Django 4.1 on 2022-10-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_editor', '0012_alter_videoid_author_id_alter_videoid_video_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoid',
            name='video_hashtags',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Video tags'),
        ),
    ]
