import hashlib
import time
import base64

class IdHash:

    # Get base64 hash from current timestamp
    def hash():
        hash_object = hashlib.md5(str(time.time()).encode("utf-8"))
        h = hash_object.hexdigest()[:9]
        b = base64.b64encode(h.encode())
        return b.decode('UTF-8')