# gCryptUtil
Encrypt data string with GCP KMS (symmetric key)

# Install

```sh
pip install --upgrade  gCryptUtil
```

# Features
* Encrypt data string with GCP KMS (symmetric key)

# Usage
```
util = CryptUtil(project_id, location_id, key_ring_id, crypto_key_id)
msg = "test123"
enc_msg = util.encrypt(msg)
msg == util.decrypt(enc_msg)
```

# Reference
[Cloud Key Management Service documentation](https://cloud.google.com/kms/docs/)