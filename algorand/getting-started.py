import json
import base64
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.transaction import PaymentTxn

def generate_algorand_keypair():
    """
    """
    private_key, address = account.generate_account()
    print(f'My address: {address}')
    print(f'My private key: {private_key}')
    print(f'My passphrase: {mnemonic.from_private_key(private_key)}')


tenXStaff = {
        'private_key': ('gIYfb9T15miiSgaxseb1V+1dVuPOP+mMunDP4jY8lgv'
                        'ErZZVMM3tczG2FUbcWUYj8lBWApL7ZU31eecA2E0k4g=='),
        'address': ('YSWZMVJQZXWXGMNWCVDNYWKGEPZFAVQCSL5WK'
                    'TPVPHTQBWCNETROFOM3IU'),
        'passphrase': ('source lawn daring front social olive fence alien '
                       'curtain onion wife step rookie stereo jacket '
                       'divert outdoor tuition reunion coconut horse '
                       'monitor frequent abandon true')
        }

tenXStudent = {
        'private_key': ('UzhjuNNXrmPyluwsdtsVfhn2qiJe0/vM9L6eBM/+OlEpt'
                        'ZUkPj5weIN1iR98+3ILxxeSbri4qhah+BSEyiS6Gw=='),
        'address': ('FG2ZKJB6HZYHRA3VREPXZ63SBPDRPETOXC4KUF'
                    'VB7AKIJSREXINQO4JAPM'),
        'passphrase': ('apology mind switch large frequent ocean '
                       'resource uncle sheriff horse april obey umbrella '
                       'primary valve spy panda spring garage enemy own '
                       'sausage mean able common')
        }


ALGOD_ADDRESS = 'http://localhost:4001'
ALGOD_TOKEN = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
               'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')

class AccountInfo:
    def __init__(self,
                 address,
                 algod_client=None,
                 algod_address=ALGOD_ADDRESS,
                 algod_token=ALGOD_TOKEN):
        """
        """
        self.address = address
        self.algod_address = algod_address
        self.algod_token = algod_token

        self.algod_client = algod_client or self._get_client()
        self.account_info = self.algod_client.account_info(address)

        # accountKeys 
        # - https://developer.algorand.org/docs/rest-apis/algod/v2/#account
        self.info_keys = ['address', 'amount', 'amount-without-pending-rewards', 
                          'assets', 'min-balance', 'rewards', 'round', 'status',
                          'total-apps-opted-in', 'total-created-apps',
                          'total-created-assets']

        for info_key in self.info_keys:
            attr_name = info_key.replace('-', '_')
            setattr(self, attr_name, self.account_info.get(info_key))

    def _get_client(self):
        return algod.AlgodClient(self.algod_token, self.algod_address)


def first_transaction_example(private_key, my_address):
    """
    """
    algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

    tenXStaff_info = AccountInfo(tenXStaff['address'], algod_client)
    print(f'Account balance: {tenXStaff_info.amount}')

    # build transaction
    params = algod_client.suggested_params()
    # comment out next two lines to use suggested params 
    params.flat_fee = True
    params.fee = 1000 
    receiver = tenXStudent['address']
    note = "Hello World".encode()

    unsigned_txn = PaymentTxn(my_address, params, receiver, 1000000, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)


first_transaction_example(tenXStaff['private_key'], tenXStaff['address'])
