from django.db import models

class Reports(models.Model):
    landslideId = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    causeOfLandSlide = models.CharField(max_length=100)
    stateOfLandSlide = models.CharField(max_length=100)
    waterTableLevel = models.CharField(max_length=20)
    areaDisplacedMass = models.CharField(max_length=20)
    numberOfHouseholds = models.CharField(max_length=10)
    incomeLevel = models.CharField(max_length=100)
    injured = models.CharField(max_length=10)
    displaced = models.CharField(max_length=10)
    deaths = models.CharField(max_length=10)
    
    # Modify the imagePath to be optional
    imagePath = models.CharField(max_length=200, blank=True, null=True)
    
    landslideSetting = models.TextField()
    classification = models.CharField(max_length=100)
    materialType = models.CharField(max_length=100)
    failureType = models.CharField(max_length=100)
    distributionStyle = models.CharField(max_length=100)
    landCoverType = models.CharField(max_length=100)
    landUseType = models.CharField(max_length=100)
    slopeAngle = models.CharField(max_length=10)
    rainfallData = models.CharField(max_length=20)
    soilMoistureContent = models.CharField(max_length=20)
    impactInfrastructure = models.TextField()
    damageRoads = models.TextField()
    damageBuildings = models.TextField()
    damageCriticalInfrastructure = models.TextField()
    damageUtilities = models.TextField()
    damageBridges = models.TextField()
    damImpact = models.TextField()
    soilImpact = models.TextField()
    vegetationImpact = models.TextField()
    waterwayImpact = models.TextField()
    economicImpact = models.TextField()
    distance1 = models.CharField(max_length=20)
    distance2 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.landslideId + ' ->' + ' district: ' + self.district