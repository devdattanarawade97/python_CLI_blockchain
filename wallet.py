
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import serialization


class Wallet:

    def __init__(self):

        self.private_key = None
        self.public_key = None

    def create_keys(self):

        private_key = (rsa.generate_private_key(
            public_exponent=65537, key_size=1024))
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

        self.private_key = private_key_pem.decode('utf-8')
        public_key = private_key.public_key()
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        self.public_key = public_key_pem.decode('utf-8')

        return (self.private_key, self.public_key)
