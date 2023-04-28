#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string.
    """
    passen = password.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passen, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks whether a password is valid
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
