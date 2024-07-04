from rest_framework import serializers
from .models import Person, Color

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

# Using another serializer class instead of using depth 
class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name', 'id']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info  = serializers.SerializerMethodField()   # We can able to write custom method for the country 
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1 # Controls how deep nested relationships are serialized

# ---# def get_country(self):
#         return 'India'

    # Function for adding a country field in person class
    def get_color_info(self, obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color_name': color_obj.color_name, 'hex_code': '#000'}


    def validate(self, data):
        special_characters = "!@#$%^&*()"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('Name should not contain Special characters')
        
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')    