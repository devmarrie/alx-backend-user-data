#!/usr/bin/env python3
"""
Defining  hash password method
"""
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """
    hashing a password
    """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd, salt)
    return hashed


def _generate_uuid() -> str:
    """
    create new unique identifier
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registering a user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except (NoResultFound, InvalidRequestError):
            hash = _hash_password(password)
            return self._db.add_user(email, hash)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Takes in an email and password
        checks if its a vlid user
        """
        try:
            user = self._db.find_user_by(email=email)
            hashed = user.hashed_password
            pwd = password.encode('utf-8')
            return bcrypt.checkpw(pwd, hashed)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Union[str, None]:
        """
        creates a session id from n email
        find the user corresponding to the email
        generate a new UUID
        store it in the database
        """
        try:
            user = self._db.find_user_by(email=email)
            sess_id = _generate_uuid()
            self._db.update_user(user.id, session_id=sess_id)
            return sess_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        Obtaining the user from a session
        """
        try:
            if session_id is None:
                return None
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys the existing session
        Args:
            user_id (int): user's id
        Return:
            None
        """
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except ValueError:
            return None
