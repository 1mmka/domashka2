from rest_framework.serializers import ModelSerializer,CharField
from main.models import Client
from rest_framework.exceptions import ValidationError

class ClientSerializer(ModelSerializer): # для CRUD, а validate,create нужен при post 
    password = CharField(write_only=True,required=True,style={'input_type':'password'})
    password2 = CharField(write_only=True,required=True,style={'input_type':'password'})
    
    class Meta:
        model = Client
        fields = ('username','password','password2','email','avatar')
        
    def validate(self, data):
        if len(data['username']) < 5:
            raise ValidationError('username len < 5')
        if data['password'] != data['password2']:
            raise ValidationError('pass1 do not match pass2')
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        client = Client.objects.create_user(**validated_data)
        return client
    

class LoginSerializer(ModelSerializer): 
    class Meta:
        model = Client
        fields = ('username','password')