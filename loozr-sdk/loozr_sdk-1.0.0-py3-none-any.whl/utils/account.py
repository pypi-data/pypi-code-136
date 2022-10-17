import os

LZR_MIXER_SECRET_KEY = os.environ.get('MIXER_SECRET_KEY')
LZR_MIXER_ACCOUNT_ID = os.environ.get('MIXER_ACCOUNT_ID',
                                      default='lzr.testnet')

LZR_FACTORY_MIXER_SECRET_KEY = os.environ.get('LZR_FACTORY_MIXER_SECRET_KEY')
LZR_FACTORY_MIXER_ACCOUNT_ID = os.environ.get('LZR_FACTORY_MIXER_ACCOUNT_ID',
                                              default='lzr-mixer.testnet')
LZR_TOKEN_CONTRACT_ID = os.environ.get('LZR_ACCOUNT_ID',
                                       default='lzr-mixer.testnet')
