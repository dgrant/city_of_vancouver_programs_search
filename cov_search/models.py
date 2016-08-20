import pprint

from django.db import models

from model_utils import FieldTracker

class Site(models.Model):
    id = models.IntegerField(primary_key=True) # comes from siteid
    name = models.CharField(max_length=50) # comes from site
    address = models.CharField(max_length=100) # comes form address
    postalcode = models.CharField(max_length=10) # comes from postalcode
    phone = models.CharField(max_length=15) # comes from phone

    tracker = FieldTracker()

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.name, self.address, self.postalcode, self.phone)

    class Meta:
        ordering = ['name', 'address',]

class Season(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True) # comes from season

    tracker = FieldTracker()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]

class Category(models.Model):
    id = models.IntegerField(primary_key=True) # comes from categoryid
    name = models.CharField(max_length=50, unique=True) # comes from programcategory 
    programtype = models.ForeignKey('ProgramType')

    tracker = FieldTracker()

    def __str__(self):
        return '{0}->{1}'.format(self.programtype, self.name)

    class Meta:
        ordering = ['name',]


class ProgramType(models.Model):
    id = models.IntegerField(primary_key=True) # comes from activitytypeid
    name = models.CharField(max_length=50, unique=True, db_index=True) # comes from programtype

    tracker = FieldTracker()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]



DAYS_OF_WEEK = (
    (1, 'Mon'),
    (2, 'Tue'),
    (3, 'Wed'),
    (4, 'Thu'),
    (5, 'Fri'),
    (6, 'Sat'),
    (7, 'Sun'),
)

class Day(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=3) # comes from day1, day2, day3, etc...

    tracker = FieldTracker()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id',]


class AgeGroup(models.Model):
    name = models.CharField(max_length=10, unique=True, db_index=True) # comes from agegroup

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]


class Instructor(models.Model):
    id = models.IntegerField(primary_key=True) # comes from instructorid
    name = models.CharField(max_length=60) # comes from instructor

    tracker = FieldTracker()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]



class Program(models.Model):
    number = models.CharField(max_length=20) # comes from programnumber
    name = models.CharField(max_length=60) # comes from programname
    membership = models.BooleanField() # comes as 'N' or 'Y'
    description = models.CharField(max_length=2000)
    site = models.ForeignKey('Site')
    season = models.ForeignKey('Season')
    category = models.ForeignKey('Category')
    days = models.ManyToManyField('Day')
    agegroup = models.ForeignKey('AgeGroup')
    agemin = models.IntegerField() # comes from agesmin
    agemax = models.IntegerField() # comes from agesmax
    enrollmin = models.IntegerField() # comes form enrollmin
    enrollmax = models.IntegerField() # comes form enrollmax
    sessions = models.IntegerField() # comes from sessions
    numberopen = models.IntegerField() # comes from numberopen
    numberwaitlisted = models.IntegerField() # comes for numberwaitlists
    ignoremaximum = models.IntegerField() # comes from ignoremaximum
    maxenrolledonline = models.IntegerField() # comes from maxenrolledonline
    numberenrolledonline = models.IntegerField() # comes from numberenrolledonline
    dropin = models.BooleanField() # comes from dropin 'N' or 'Y'
    firstclass = models.BooleanField() # comes from firstclass 'N' or 'Y'
    onlinereg = models.BooleanField() # comes from onlinereg 'N' or 'Y'
    instructor = models.ForeignKey('Instructor', null=True)
#    startdate = models.DateField() # comes as date like: Jun 12, 2015
#    enddate = models.DateField() # comes as date like: Jul 3, 2015
#    starttime = models.TimeField() # comes as 9:00am
#    endtime = models.TimeField() # comes as 9:00am
    lac = models.BooleanField() # comes from lac as 'N' or 'Y'
    fee = models.DecimalField(max_digits=6, decimal_places=2) # comes as "$20.00" from fee1
#         "fee1grp":"",
#         "fee2":"$0.00",
#         "fee2grp":"seniors",
#         "fee3":"$0.00",
#         "fee3grp":"",
#         "fee4":"$0.00",
#         "fee4grp":"",
#       "room":", Fitness Centre",
#         "roomid":"2333",
#    activitytype = models.ForeignKey('ActivityType')
    id = models.IntegerField(primary_key=True)
#         "pfsiteid":"0",
#         "pfftypeid":"0",
#         "pfactypeid":"0",
#         "gradeidmin":"0"


    tracker = FieldTracker()

    def __str__(self):
        return '{0} ({1}, {2})'.format(self.name, self.number, self.id)


    class Meta:
        ordering = ['name',]
