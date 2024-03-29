# Generated by Django 4.2.5 on 2024-02-15 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_complex_payment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplexImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ComplexIMG')),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='EnvironmentIMG')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='FeaturesIMG')),
            ],
        ),
        migrations.AddField(
            model_name='complex',
            name='environment_img',
            field=models.ManyToManyField(to='main.environmentimg'),
        ),
        migrations.AddField(
            model_name='complex',
            name='feature_img',
            field=models.ManyToManyField(to='main.featureimage'),
        ),
        migrations.AddField(
            model_name='complex',
            name='img',
            field=models.ManyToManyField(to='main.compleximage'),
        ),
    ]
