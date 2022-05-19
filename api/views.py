from rest_framework import generics
from rest_framework.decorators import action
from django.core.files import File
# from utils import Base64ImageField
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.base_user import BaseUserManager
import string

print(BaseUserManager().make_random_password(5, string.digits))

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from api.models import Services, Masters, Clients, Orders
from api.serializers import (ServicesSerializer, MastersSerializer,
                             ClientsSerializer, OrdersSerializer)


class ServicesAPIView(generics.ListAPIView):
    # queryset = Services.objects.all()
    serializer_class = ServicesSerializer

    def get(self, request):
        services_lst = Services.objects.all()
        # services_serializer = ServicesSerializer(services_lst, many=True)
        return Response(
            {'Services': ServicesSerializer(services_lst, many=True).data})

    # permission_classes = (IsA,)

    def post(self, request):
        serializer = ServicesSerializer(data=request.datas)
        # data = request.DATA, files = request.FILES
        serializer.is_valid(raise_exception=True)
        service_new = Services.objects.create(
            service_name=request.data['service_name'],
            service_price=request.data['service_price'],
            service_duration=request.data['service_duration'],
        )
        return Response({'Services': model_to_dict(service_new)})


# def post(self, request):
#     serializer = ServicesSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     service_new = Services.objects.create(
#         service_name=request.data['service_name'],
#         service_price=request.data['service_price'],
#         service_duration=request.data['service_duration'],
#     )
#     return Response({'Services': model_to_dict(service_new)})

class MastersAPIView(generics.ListAPIView):
    # queryset = Masters.objects.all()
    serializer_class = MastersSerializer

    def get(self, request):
        masters_lst = Masters.objects.all()
        # masters_serializer = MasterSerializer(services_lst, many=True)
        return Response(
            {'Masters': MastersSerializer(masters_lst, many=True).data})

    def post(self, request):
        serializer = MastersSerializer(data=request.data)
        # serializer_1 = MastersSerializer(data=request.data, files=request.FILES)
        serializer.is_valid(raise_exception=True)
        master_new = Masters.objects.create(
            master_name=request.data['master_name'],
            master_surname=request.data['master_surname'],
            # master_photo=request.data['master_photo'],
            master_photo=serializer.validated_data['master_photo'],
            master_phone=request.data['master_phone'],
            master_skills=request.data['master_skills'],
        )
        master_new.save()
        for skill in data["master_skills"]:
            skill.obj = Services.objects.get(
                master_skills=skill[master_skills])
            master_new.services.add(skill.obj)
        return Response({'Masters': model_to_dict(master_new)})

    @action(detail=True, methods=['put'])
    def photo(self, request, pk=None):
        user = self.get_object()
        photo = user.masters
        serializer = MastersSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.data, status=400)


# class MasterAPIView(generics.ListCreateAPIView):
#
#     serializer_class = MasterSerializer
#
#     def get(self, request):
#         master_lst = Master.objects.all()
#         master_serializer = MasterSerializer(master_lst, many=True)
#         return Response({'Masters': master_serializer.data})
#
#     def post(self, request):
#         master_new = Master.objects.create(
#             master_name=request.data['master_name'],
#             master_surname=request.data['master_surname'],
#             master_photo=request.data['master_photo'],
#             master_phone=request.data['master_phone'],
#             master_skills=request.data['master_skills'],
#         )
#         return Response({'Master': model_to_dict(master_new)})


class ClientsAPIView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = ClientsSerializer

    def get(self, request):
        clients_lst = Clients.objects.all()
        clients_serializer = ClientsSerializer(clients_lst, many=True)
        return Response({'Clients': clients_serializer.data})

    # def get(self, request, id=None):
    #     if id:
    #         item = Clients.objects.get(id=id)
    #         serializer = ClientsSerializer(item)
    #         return Response({"status": "success", "Master": serializer.data},
    #                         status=status.HTTP_200_OK)
    #
    #     items = Clients.objects.all()
    #     serializer = ClientsSerializer(items, many=True)
    #     return Response({"status": "success", "Masters": serializer.data},
    #                     status=status.HTTP_200_OK)

    # def post(self, request):
    #     client_new = Clients.objects.create(
    #         client_name=request.data['client_name'],
    #         client_surname=request.data['client_surname'],
    #         # data['client_phone'] = str(instance.phone_number)
    #         # client_phone=request.data.str(['client_phone']),
    #         client_phone=request.data['client_phone'],
    #         info=request.data['info'],
    #     )
    #     return Response({'Clients': model_to_dict(client_new)})

    # def post(self, request):
    #     serializer = ClientsSerializer(data=request.data)
    #     data = {}
    #     if serializer.is_valid():
    #         clients = serializer.save()
    #         data['response'] = 'successfully registered new user.'
    #         data['client_name'] = clients.client_name
    #         data['client_surname'] = clients.client_surname
    #         data['client_phone'] = clients.client_phone
    #         data['info'] = clients.info
    #     else:
    #         data = serializer.errors
    #     return Response(data)

    @api_view(['POST', ])
    def clients_view(request):

        if request.method == 'POST':
            serializer = ClientsSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                clients = serializer.save()
                data['response'] = 'successfully registered new client.'
                data['client_name'] = clients.client_name
                data['client_surname'] = clients.client_surname
                data['client_phone'] = clients.client_phone
                data['info'] = clients.info
            else:
                data = serializer.errors
            return Response(data)


class OrdersAPIView(generics.ListCreateAPIView):
    serializer_class = OrdersSerializer

    def get(self, request):
        orders_lst = Orders.objects.all()
        return Response(
            {'Orders': OrdersSerializer(orders_lst, many=True).data})


