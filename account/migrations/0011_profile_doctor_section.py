# Generated by Django 4.2.5 on 2023-11-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_profile_type_of_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='doctor_section',
            field=models.CharField(choices=[('TOOTHS', 'TOOTHS'), ('ANIMALS', 'ANIMALS'), ('MOUSE', 'MOUSE')], default=1, max_length=60),
            preserve_default=False,
        ),
    ]
