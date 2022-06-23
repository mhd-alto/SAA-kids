# Generated by Django 3.2.6 on 2022-06-22 06:55

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(max_length=400)),
                ('min_required_age', models.IntegerField()),
                ('max_required_age', models.IntegerField()),
                ('form_url', models.URLField()),
                ('description', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='activity/default_activity_photo.jpg', upload_to='activity/')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
            ],
        ),
    ]
