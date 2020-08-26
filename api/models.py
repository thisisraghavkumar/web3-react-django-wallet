from django.db import models
from .validators import ethAddress, txHash
from django.db.models.signals import pre_save

ETH_ADD_LEN = 42
ETH_TX_HASH_LEN = 66

# Create your models here.
class Contacts(models.Model):

    owner = models.CharField(max_length=ETH_ADD_LEN, null = False, blank = False, validators=[ethAddress])
    contact_address = models.CharField(max_length=ETH_ADD_LEN, null = False, blank = False, validators=[ethAddress])
    contact_name = models.CharField(max_length=128)
    combined_address = models.CharField(max_length=2*ETH_ADD_LEN, unique=True) # to ensure that only one contact pair is saved

def contactPreSave(sender, instance, **kwargs):
    combined_addr = instance.owner + instance.contact_address
    instance.combined_address = combined_addr

pre_save.connect(receiver=contactPreSave, sender=Contacts)

class Transactions(models.Model):
    txHash = models.CharField(max_length=ETH_TX_HASH_LEN, primary_key = True, validators=[txHash])
    owner = models.CharField(max_length=ETH_ADD_LEN, null = False, blank = False)
    date_of_transaction = models.DateTimeField( auto_now_add=True)

