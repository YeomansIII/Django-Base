from django.db import models

# Create your models here.
class Class(models.Model):
    year_int = models.IntegerField()
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

    def __str__(self):              # __unicode__ on Python 2
        return self.year_int


class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address')

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.name)


class Room(models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()
    bedA = models.CharField(max_length=80)
    bedB = models.CharField(max_length=80)
    bedC = models.CharField(max_length=80)
    bedD = models.CharField(max_length=80)
    building = models.ForeignKey('Building')

    def __str__(self):              # __unicode__ on Python 2
        return self.building.__str__()+" "+self.number.__str__()


class Address(models.Model):
    street = models.CharField(max_length=100)
    zip_code = models.IntegerField(max_length=5)
    state = models.CharField(max_length=2)

    def __str__(self):              # __unicode__ on Python 2
        return self.street
