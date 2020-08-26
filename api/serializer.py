from rest_framework.serializers import ModelSerializer
from .models import Contacts, Transactions

class contactSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['owner', 'contact_address', 'contact_name']

class transactionSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['txHash', 'owner', 'date_of_transaction']