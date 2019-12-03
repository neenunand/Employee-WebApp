import string
import random
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q

class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='Confirm Password')
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {"password":{"write_only":True},"password2":{"write_only":True
        }}

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This email already exists.")
        return data

    def validate_password(self, value):
        data = self.get_initial()
        passwd2 = data.get('password2')
        passwd1 = value
        if passwd1 != passwd2:
            raise ValidationError("Passwords must match.")
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        passwd1 = data.get('password')
        passwd2 = value
        if passwd1 != passwd2:
            raise ValidationError("Passwords must match.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=True, allow_blank=False)
    class Meta:
        model = User
        fields = ['username','password','token']
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, data):
        user_obj = None
        username = data.get('username')
        password = data['password']
        # if not username:
        #     raise ValidationError("Username is required.")
        user = User.objects.filter(username=username)        
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username is invalid.")
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials, please try again.")

        # string_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        # token_text = ''.join(random.choice(string_chars) for _ in range(50))
        # data['token'] = token_text

        return data