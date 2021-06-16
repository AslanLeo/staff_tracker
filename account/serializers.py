from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, required=True)
    password_confirm = serializers.CharField(min_length=6, required=True)

    class Meta:
        model = User
        fields = ( 'phone_number', 'password', 'password_confirm',
                  'first_name', 'last_name')

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            # print("phone_number =", phone_number, "\npassword =", password)
            user = authenticate(username=phone_number, password=password,
                                request=self.context.get('request'))
            if not user:
                msg = ('Неверно указан номер телефона или пароль',)
                raise serializers.ValidationError(msg)
        else:
            raise serializers.ValidationError('Введите номер телефона и пароль')
        attrs['user'] = user
        return attrs


class UserCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



# class AtWorkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AtWork
#         fields = '__all__'
#
#     def at_work_tracker(self,attrs):
#         at_work = attrs.get('at_work')
#         if not User.IsAuthenticated:
#             AtWork.at_work == False
#
#         return attrs

