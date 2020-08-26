from django.core.exceptions import ValidationError

ETH_ADD_LEN = 42
ETH_TX_HASH_LEN = 66

def ethAddress(value):
    if len(value) != ETH_ADD_LEN:
        raise(ValidationError("Length of given address {} is not correct ({})".format(value, ETH_ADD_LEN)))


def txHash(value):
    if len(value) != ETH_TX_HASH_LEN:
        raise(ValidationError("Length of given transaction hash {} is not correct ({})".format(value, ETH_TX_HASH_LEN)))
