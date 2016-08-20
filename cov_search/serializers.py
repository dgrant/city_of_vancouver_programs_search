from .models import *
from rest_framework import serializers

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
#class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('url', 'id', 'number', 'name', 'numberopen',)
#         'membership', 'description', 'site',
#            'season', 'category', 'days', 'agegroup', 'agemin', 'agemax',
#            'enrollmin', 'enrollmax', 'sessions', 'numberopen',
#            'numberwaitlisted', 'ignoremaximum', 'maxenrolledonline',
#            'numberenrolledonline', 'dropin', 'firstclass', 'onlinereg',
#            'instructor', 'lac', 'fee',)

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('id', 'name', 'address', 'postalcode', 'phone',)

class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'name',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'programtype',)

class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'name',)

class AgeGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgeGroup
        fields = ('id', 'name',)

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id', 'name',)
