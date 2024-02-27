# Generated by Django 5.0 on 2024-02-14 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complex',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complex',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complex',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.complextype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='complex',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.complex'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.stata'),
            preserve_default=False,
        ),
    ]
