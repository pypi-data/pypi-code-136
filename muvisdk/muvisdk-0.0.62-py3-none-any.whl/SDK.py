from .mercadopago_sdk.MercadoPagoSDK import MercadoPagoSDK
from .decidir_sdk.DecidirSDK import DecidirSDK
import os

class SDK:
    def __init__(self, merchant: dict, merchant_cadena: dict, processor: str = None, marketplace: bool = False):
        self._sdk = None

        # Se verifica la variable de entorno:
        test = os.getenv('TEST')
        test_sdk = True
        if test.lower() == 'false':
            test_sdk = False

        # Se verifica el procesor
        if processor == 'mercadopago':
            self.processor = 'mercadopago'
            self._sdk = MercadoPagoSDK(merchant, marketplace=marketplace)
        elif processor == 'decidir':
            self.processor = 'decidir'
            self._sdk = DecidirSDK(merchant, merchant_cadena, marketplace=marketplace, test=test_sdk)

    def customer(self):
        return self._sdk.customer()

    def card(self):
        return self._sdk.card()

    def card_token(self):
        return self._sdk.card_token()

    def payment(self):
        return self._sdk.payment()

    def refund(self):
        return self._sdk.refund()

    def ok(self):
        return self._sdk is not None and self._sdk.ok()
