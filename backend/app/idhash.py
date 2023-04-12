import base64
import hashlib
import time


class IdHash:
    # Get base64 hash from current timestamp
    def hash(self):
        hash_object = hashlib.md5(str(time.time()).encode("UTF-8"))
        h = hash_object.hexdigest()[:9]
        b = base64.b64encode(h.encode())
        return b.decode("UTF-8")
