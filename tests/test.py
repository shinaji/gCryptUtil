from gCryptUtil import CryptUtil
import os


def test_encrypt_decrypt():
    project_id = os.environ["project_id"]
    location_id = os.environ["location_id"]
    key_ring_id = os.environ["key_ring_id"]
    crypto_key_id = os.environ["crypto_key_id"]
    util = CryptUtil(project_id, location_id, key_ring_id, crypto_key_id)

    assert util.project_id == project_id, "stored project id is not correct"
    assert util.location_id == location_id, "stored location id is not correct"
    assert util.key_ring_id == key_ring_id, "stored key ring id is not correct"
    assert util.crypto_key_id == crypto_key_id, \
        "stored crypt key id is not correct"

    msg = "test123"
    enc_msg = util.encrypt(msg)
    assert msg == util.decrypt(enc_msg), "encryption or decryption was failed"


def test_key_name_based_initialization():
    project_id = os.environ["project_id"]
    location_id = os.environ["location_id"]
    key_ring_id = os.environ["key_ring_id"]
    crypto_key_id = os.environ["crypto_key_id"]

    name = (f'projects/{project_id}/locations/{location_id}/keyRings/'
            f'{key_ring_id}/cryptoKeys/{crypto_key_id}')

    util = CryptUtil(key_name=name)

    assert util.key_name == name, "storeed key name is not correct"
    assert util.project_id == project_id, "stored project id is not correct"
    assert util.location_id == location_id, "stored location id is not correct"
    assert util.key_ring_id == key_ring_id, "stored key ring id is not correct"
    assert util.crypto_key_id == crypto_key_id, \
        "stored crypt key id is not correct"

    msg = "test123"
    enc_msg = util.encrypt(msg)
    assert msg == util.decrypt(enc_msg), "encryption or decryption was failed"