# Generated by Django 5.1.6 on 2025-03-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0004_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landslideId', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=100)),
                ('upazila', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('causeOfLandSlide', models.CharField(max_length=100)),
                ('stateOfLandSlide', models.CharField(max_length=100)),
                ('waterTableLevel', models.CharField(max_length=20)),
                ('areaDisplacedMass', models.CharField(max_length=20)),
                ('numberOfHouseholds', models.CharField(max_length=10)),
                ('incomeLevel', models.CharField(max_length=100)),
                ('injured', models.CharField(max_length=10)),
                ('displaced', models.CharField(max_length=10)),
                ('deaths', models.CharField(max_length=10)),
                ('imagePath', models.CharField(max_length=200)),
                ('landslideSetting', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('materialType', models.CharField(max_length=100)),
                ('failureType', models.CharField(max_length=100)),
                ('distributionStyle', models.CharField(max_length=100)),
                ('landCoverType', models.CharField(max_length=100)),
                ('landUseType', models.CharField(max_length=100)),
                ('slopeAngle', models.CharField(max_length=10)),
                ('rainfallData', models.CharField(max_length=20)),
                ('soilMoistureContent', models.CharField(max_length=20)),
                ('impactInfrastructure', models.TextField()),
                ('damageRoads', models.TextField()),
                ('damageBuildings', models.TextField()),
                ('damageCriticalInfrastructure', models.TextField()),
                ('damageUtilities', models.TextField()),
                ('damageBridges', models.TextField()),
                ('damImpact', models.TextField()),
                ('soilImpact', models.TextField()),
                ('vegetationImpact', models.TextField()),
                ('waterwayImpact', models.TextField()),
                ('economicImpact', models.TextField()),
                ('distance1', models.CharField(max_length=20)),
                ('distance2', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
