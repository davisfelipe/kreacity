from hashlib import sha256

from fastapi import Form


class UserAuth:
    def __init__(self, username: int = Form(...), password: str = Form(...)):
        hash_pass = sha256()
        hash_pass.update(password.encode('utf-8'))
        self.username = username
        self.password = hash_pass.hexdigest()
