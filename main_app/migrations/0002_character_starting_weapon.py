# Generated by Django 4.2 on 2023-05-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='starting_weapon',
            field=models.CharField(choices=[('S', 'Straight Sword'), ('K', 'Katana'), ('G', 'Greatsword'), ('A', 'Axe'), ('C', 'Curved Sword'), ('D', 'Dagger'), ('H', 'Halberd'), ('B', 'Bow'), ('W', 'Whip'), ('T', 'Talisman')], default='S', max_length=100),
        ),
    ]
