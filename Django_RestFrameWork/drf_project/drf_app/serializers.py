from rest_framework import serializers
from .models import Person, Color

# Using another serializer class instead of using depth 
class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name', 'id']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    country = serializers.SerializerMethodField()   # We can able to write custom method for the country 
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1 # Controls how deep nested relationships are serialized

    #1:02:43  ------ time continue

    def validate(self, data):
        special_characters = "!@#$%^&*()"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('Name should not contain Special characters')
        
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')    