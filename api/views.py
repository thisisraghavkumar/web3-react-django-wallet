from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contacts, Transactions
from .serializer import contactSerializer, transactionSerializer
from django.db.models import Model
# Create your views here.

class Contact(APIView):
    def get(self, request, format=None):
        print(request.query_params)
        res = Contacts.objects.filter(owner__iexact = request.query_params["owner"])
        serialized_res = contactSerializer(res, many = True)
        ret = serialized_res.data
        return Response(ret)

    def post(self, request, format=None):
        rec = contactSerializer(data = request.data['data'])
        print(request.data)
        print(rec.is_valid())
        if rec.is_valid():
            rec.save()
            print("Saved object {}".format(rec))
            return Response(rec.validated_data, status = status.HTTP_201_CREATED)
        print(rec.data)
        return Response(rec.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Transaction(APIView):
    def get(self, request, format=None):
        res = Transactions.objects.filter(owner__iexact=request.query_params["owner"])
        print(res)
        serialized_res = transactionSerializer(res, many= True)
        ret = serialized_res.data
        return Response(ret)

    def post(self, request, format=None):
        rec = transactionSerializer(data=request.data['data'])
        if rec.is_valid():
            rec.save()
            print("Saved object {}".format(rec))
            return Response(rec.validated_data, status = status.HTTP_201_CREATED)
        return Response(rec.errors, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

class IsContact(APIView):
    def get(self, request, format=None):
        print(request.query_params)
        combined_addr = request.query_params["owner"]+request.query_params["contact_address"]
        try:
            res = Contacts.objects.get(combined_address = combined_addr)
            if res:
                return Response(True)
        except:
            return Response(False)