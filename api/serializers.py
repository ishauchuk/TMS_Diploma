from rest_framework import serializers
from django.core.validators import MinValueValidator
# from rest_framework.serializers import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField
# from phonenumber_field.phonenumber import to_python
from .models import Services, Masters, Clients, Orders


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['service_name', 'service_price', 'service_duration']
        # service_name = serializers.CharField(*args, **kwargs)
        # service_price = serializers.FloatField(*args, **kwargs)
        # service_duration = serializers.DurationField(*args, **kwargs)

    # def validate(self, data):
    #     """
    #     Check that the start is before the stop.
    #     """
    #     if data['service_price'] <= 0.0:
    #         raise serializers.ValidationError("finish must occur after start")
    #     # if data['service_duration'] <= 0:
    #     #     raise serializers.ValidationError("time must be positive")
    #     return data

    # def validate_service_price(self, price):
    #     # user = self.request.data.get('createdByUser', None)
    #     # karma = self.request.data.get('karma', None)
    #     # creationDate = self.request.data.get('creationDate', None)
    #     # service_price = self.request.data.get('service_price')
    #
    #     if price <= 0:
    #         raise serializers.ValidationError(
    #             {"service_price": "it should be positive"})
    #     return price


class MasterSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['service_name']


class MasterPhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Masters
        fields = ['master_photo']


# class PhotosSerializer(serializers.ModelSerializer):
#     photo_url = serializers.ImageField()
#
#     class Meta:
#         model = Masters
#         fields = ('master_photo')
#
#     def get_photo_url(self, car):
#         request = self.context.get('request')
#         photo_url = masters.photo.url
#         return request.build_absolute_uri(photo_url)


# class ImageField(serializers.ImageField):
#     def value_to_string(self, obj): # obj is Model instance, in this case, obj is 'Class'
#         return obj.fig.url

class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    master_photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False,
        use_url=True, required=False)

    class Meta:
        model = Masters
        fields = ('master_photo',)


# class MastersSerializer(serializers.ModelSerializer):
class MastersSerializer(serializers.HyperlinkedModelSerializer):
    master_skills = MasterSkillsSerializer(many=True)
    # master_photo = PhotosSerializer()
    master_photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False,
        use_url=True, required=False)

    # master_photo = MasterPhotosSerializer()
    # master_photo = PhotosSerializer(many=True)
    # master_photo = ImageField()

    class Meta:
        model = Masters
        fields = ['master_name', 'master_surname', 'master_photo',
                  'master_phone', 'master_skills']

    # def master_photo_url(self, masters):
    #     request = self.context.get('request')
    #     photo_url = masters.photo.url
    #     return request.build_absolute_uri(photo_url)


# class CustomPhoneNumberField(PhoneNumberField):
#     def to_internal_value(self, data):
#         phone_number = to_python(data)
#         if phone_number and not phone_number.is_valid():
#             raise ValidationError(self.error_messages["invalid"])
#         return phone_number.as_e164


# class SignupSerializer(serializers.Serializer):
#     client_phone = PhoneNumberField()


class ClientsSerializer(serializers.ModelSerializer):
    # client_phone = SignupSerializer(many=True)
    class Meta:
        model = Clients
        fields = ['client_name', 'client_surname', 'client_phone', 'info']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['order_type', 'order_date', 'order_time', 'master_choice',
                  'client_choice']
