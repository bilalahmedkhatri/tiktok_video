# Generated by Django 4.1 on 2022-10-19 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_editor', '0008_alter_hashtag_count_top_tag_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoid',
            name='len_hashtags',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='videoowner',
            name='instagram_acc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='videoid',
            name='owner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video_editor.videoowner', verbose_name='Video Onwer'),
        ),
        migrations.AlterField(
            model_name='videoid',
            name='video_hashtags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video_editor.hashtag', verbose_name='Video tags'),
        ),
        migrations.AlterField(
            model_name='videoowner',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='videoowner',
            name='total_videos',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]