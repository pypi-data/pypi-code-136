import base58
from .requesters import http
import datetime
import struct
from nacl.signing import SigningKey, VerifyKey
from nacl.public import SealedBox
from nacl.encoding import RawEncoder
from mnemonic import Mnemonic
from bip_utils import Bip39Languages, Bip39SeedGenerator
from bip_utils import Bip32Ed25519Slip


class Client:
    """Client class to interact with DeenAiR blockchain
    Args:
        endpoint: URL of the RPC endpoint
        """

    def __init__(self, endpoint: str = None):
        super().__init__()
        self.requester = http.HTTPRequester(endpoint)
        self.message_type_codes = {"withdraw": 5,
                                   "delegate": 4,
                                   "transfer": 2,
                                   "fee": 3
                                   }

    def get_node_list(self):
        return self.requester.make_request("GetNodeList", [])

    def get_block(self, block: str):

        if block == "latest":
            param = {}
        elif block.isdigit():
            param = {"blk": block}
        else:
            raise Exception('''Block parameter must be "latest" or string contains only integers''')

        return self.requester.make_request("GetBlock", param)

    def get_leader(self):
        return self.requester.make_request("GetLeader", [])

    def get_wallet_state(self, wallet):
        param = {"wallet": wallet}
        return self.requester.make_request("GetWalletState", param)

    def get_wallet_transactions(self, wallet):
        param = {"wallet": wallet}
        return self.requester.make_request("GetWalletTrxs", param)

    def get_transaction(self, transaction_id) -> dict:
        param = {"trxid": transaction_id}
        return self.requester.make_request("GetTrxInfo", param)

    @staticmethod
    def get_base58_public_from_secret(secret_key) -> str:
        payer_secret_raw = base58.b58decode(secret_key)
        key_object = SigningKey(payer_secret_raw).verify_key.encode()
        return base58.b58encode(key_object).decode()

    @staticmethod
    def get_binary_public_from_secret(secret_key) -> bytes:
        payer_secret_raw = base58.b58decode(secret_key)
        key_object = SigningKey(payer_secret_raw)
        return key_object.verify_key.encode()

    @staticmethod
    def sign_message(secret_key: str, message: bytes) -> bytes:
        secret_key_binary = base58.b58decode(secret_key)
        signer = SigningKey(secret_key_binary, encoder=RawEncoder)
        sign = signer.sign(message, encoder=RawEncoder)
        return sign.signature

    @staticmethod
    def create_binary_message(
            message_type_code: int,
            current_timestamp: int,
            payer_public_key_binary: bytes,
            receiver_public_key_binary: bytes,
            amount_solidius: float,
            comment: str = ""):

        message_type_code_binary = struct.pack(">H", message_type_code)

        current_timestamp_binary = struct.pack(">Q", current_timestamp)

        amount_solidius_binary = struct.pack(">Q", amount_solidius)

        comment_length = len(comment)
        comment_length_binary = struct.pack("b", comment_length)
        comment_binary = comment.encode()

        message_binary_data = \
            message_type_code_binary + \
            current_timestamp_binary + \
            payer_public_key_binary + \
            receiver_public_key_binary + \
            amount_solidius_binary + \
            comment_length_binary + \
            comment_binary

        return message_binary_data

    def create_message(self, **args):

        message_type_code = self.message_type_codes[args["message_type"]]

        current_timestamp = int(datetime.datetime.utcnow().timestamp() * 1e3 + 10800000)

        payer_public_key_binary = self.get_binary_public_from_secret(args["payer_secret"])
        payer_public_key_b58 = base58.b58encode(payer_public_key_binary).decode()

        receiver_public_key_binary = base58.b58decode(args["receiver_public"])

        amount_solidius = int(args["amount"] * 10_000_000)

        message_binary_data = self.create_binary_message(message_type_code,
                                                         current_timestamp,
                                                         payer_public_key_binary,
                                                         receiver_public_key_binary,
                                                         amount_solidius,
                                                         args["comment"])

        message_signature = self.sign_message(args["payer_secret"], message_binary_data)

        message = {
            "type": args["message_type"],
            "time": current_timestamp,
            "payer": payer_public_key_b58,
            "receiver": args["receiver_public"],
            "sum": str(amount_solidius),
            "comment": args["comment"],
            "sign": base58.b58encode(message_signature).decode()
        }

        return message

    @staticmethod
    def calculate_fee_transaction(message_binary=None, message_dict=None):
        if message_binary is not None:
            fee_calc = len(message_binary) + 64
        elif message_dict is not None:
            fee_calc = 83 + len(message_dict["comment"]) + 64
        else:
            raise Exception("Messages are not provided")

        fee_calc = fee_calc + 32 + 2 * 8
        fee_calc = fee_calc + 32 + 2 * 8
        fee_calc *= 10
        fee_calc += 10_000
        return fee_calc

    def create_and_send_transaction(self, messages: list, fee_payer_secret: str):
        total_fee = 0
        messages_list = []
        for message in messages:

            message_dict = self.create_message(**message)

            messages_list.append(message_dict)
            message_fee = self.calculate_fee_transaction(message_dict=message)
            total_fee += message_fee

        fee_message_args = {
            "message_type": "fee",
            "payer_secret": fee_payer_secret,
            "receiver_public": "deenAiRoven55555555555555555555555555555555",
            "amount": total_fee / 10_000_000,
            "comment": ""}

        fee_message = self.create_message(**fee_message_args)

        messages_list.append(fee_message)
        param = {"messages": messages_list}
        return self.requester.make_request("NewTrx", param)

    @staticmethod
    def encrypt_data(receiver_public_key, message):
        receiver_public_key_bytes = base58.b58decode(receiver_public_key)
        verify_key = VerifyKey(key=receiver_public_key_bytes, encoder=RawEncoder)
        pub_key = verify_key.to_curve25519_public_key()
        cryptor = SealedBox(pub_key)
        return cryptor.encrypt(message)

    @staticmethod
    def decrypt_data(secret_key, message):
        secret_key_bytes = base58.b58decode(secret_key)
        sec = SigningKey(seed=secret_key_bytes, encoder=RawEncoder)
        pk = sec.to_curve25519_private_key()
        decrypt = SealedBox(pk)
        return decrypt.decrypt(message)

    @staticmethod
    def verify_signature(public, signature, message):
        receiver_public_key_bytes = base58.b58decode(public)

        verify_key = VerifyKey(key=receiver_public_key_bytes, encoder=RawEncoder)

        verif = verify_key.verify(message, signature, encoder=RawEncoder)
        return verif == message

    @staticmethod
    def generate_mnemonic(strength=128):
        lang = "english"
        mnemo = Mnemonic(lang)
        words = mnemo.generate(strength=strength).split(" ")
        return words

    @staticmethod
    def recover_keypair_from_phrase(phrase: list, wallet_id: int = 3) -> dict:
        mnemonic_string = " ".join(phrase)
        seed_bytes = Bip39SeedGenerator(mnemonic_string, Bip39Languages.ENGLISH).Generate()

        bip32_ctx = Bip32Ed25519Slip.FromSeedAndPath(seed_bytes, f"m/44'/3566'/1'/0'/{wallet_id}'")
        priv_key = base58.b58encode(bip32_ctx.PrivateKey().Raw().ToBytes()).decode()
        publ_key = base58.b58encode(bip32_ctx.PublicKey().RawUncompressed().ToBytes()[1:]).decode()

        return {"wallet_id": wallet_id, "priv_key": priv_key, "publ_key": publ_key}

    def generate_keypair(self, wallet_id: int = 3, strength: int = 128) -> dict:

        words = " ".join(self.generate_mnemonic(strength))
        seed_bytes = Bip39SeedGenerator(words, Bip39Languages.ENGLISH).Generate()

        bip32_ctx = Bip32Ed25519Slip.FromSeedAndPath(seed_bytes, f"m/44'/3566'/1'/0'/{wallet_id}'")
        priv_key = base58.b58encode(bip32_ctx.PrivateKey().Raw().ToBytes()).decode()
        publ_key = base58.b58encode(bip32_ctx.PublicKey().RawUncompressed().ToBytes()[1:]).decode()

        return {"seed_phrase": words, "wallet_id": wallet_id, "priv_key": priv_key, "publ_key": publ_key}

    def get_my_stakes(self, wallet):

        my_trx = self.get_wallet_transactions(wallet)
        if my_trx["status"] == "error":
            return []
        else:
            my_trx = my_trx["result"]
        current_timestamp = int(datetime.datetime.utcnow().timestamp() * 1e3 + 10800000)
        my_stakes = {}
        for trx in my_trx:
            if trx["type"] == "remittance":
                messages = trx["msgs"]
                for message in messages:
                    current_diff = current_timestamp - int(message["time"])
                    receiver = message["receiver"]
                    if receiver not in my_stakes:
                        dict_trx = dict()
                        current_stake = 0
                        withdrawable_stake = 0
                    else:
                        dict_trx = my_stakes[receiver]
                        current_stake = my_stakes[receiver]["stake"]
                        withdrawable_stake = my_stakes[receiver]["withdrawable"]

                    if message["type"] == "stake delegate" and message["payer"] == wallet:
                        dict_trx.update({"stake": current_stake + int(message["sum"])})
                        if current_diff / 86400000 > 14:
                            dict_trx.update({"withdrawable": withdrawable_stake + int(message["sum"])})
                            my_stakes.update({receiver: dict_trx})
                        else:
                            dict_trx.update({"withdrawable": withdrawable_stake + 0})
                            my_stakes.update({receiver: dict_trx})
                    elif message["type"] == "stake withdraw" and message["receiver"] == wallet:
                        dict_trx.update({"stake": current_stake - int(message["sum"]),
                                         "withdrawable": withdrawable_stake - int(message["sum"])})
                        my_stakes.update({receiver: dict_trx})
        return my_stakes
