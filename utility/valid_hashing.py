
import hashlib


# this function returns valid hash

def find_valid_hash(nonce, previous_nonce):
    generated_hash = hashlib.sha256(
        str(nonce**2-previous_nonce**2).encode()).hexdigest()

    return generated_hash
