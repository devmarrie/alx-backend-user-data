#!/usr/bin/env python3
"""
Defining  hash password method
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hashing a password
    """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd, salt)
    return hashed
