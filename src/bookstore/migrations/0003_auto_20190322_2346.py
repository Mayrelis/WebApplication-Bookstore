# Generated by Django 2.1.7 on 2019-03-22 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookstore', '0002_auto_20190203_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('dob', models.CharField(blank=True, max_length=12, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=75, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.URLField(null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('publication_date', models.CharField(blank=True, max_length=12, null=True)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
                ('pages', models.IntegerField(default=0)),
                ('avg_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('sales_rank', models.IntegerField(default=0)),
                ('top_sellers', models.BooleanField(default=False)),
                ('authors', models.ManyToManyField(blank=True, to='bookstore.Author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.Publisher'),
        ),
    ]