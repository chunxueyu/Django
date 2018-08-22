import uuid
import hashlib
def create_random_str():
    uid = uuid.uuid4()
    uid_str = str(uid).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uid_str)
    return md5.hexdigest()