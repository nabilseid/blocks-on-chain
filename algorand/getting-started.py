from algosdk import account, mnemonic
from algosdk.v2client import algod

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print(f'My address: {address}')
    print(f'My private key: {private_key}')
    print(f'My passphrase: {mnemonic.from_private_key(private_key)}')

# My address: YSWZMVJQZXWXGMNWCVDNYWKGEPZFAVQCSL5WKTPVPHTQBWCNETROFOM3IU
# My private key: gIYfb9T15miiSgaxseb1V+1dVuPOP+mMunDP4jY8lgvErZZVMM3tczG2FUbcWUYj8lBWApL7ZU31eecA2E0k4g==
# My passphrase: source lawn daring front social olive fence alien curtain onion wife step rookie stereo jacket divert outdoor tuition reunion coconut horse monitor frequent abandon true

def first_transaction_example(private_key, address):
    """
    """
    algod_address = 'http://localhost:4001'
    algod_token = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                   'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    algod_client = algod.AlgodClient(algod_token, algod_address)

    account_info = algod_client.account_info(address)
    print(f'Account balance: {account_info.get("amount")}')

private_key = ('gIYfb9T15miiSgaxseb1V+1dVuPOP+mMunDP4jY8lgvErZZVM'
               'M3tczG2FUbcWUYj8lBWApL7ZU31eecA2E0k4g==')
address = 'YSWZMVJQZXWXGMNWCVDNYWKGEPZFAVQCSL5WKTPVPHTQBWCNETROFOM3IU'

first_transaction_example(private_key, address)
