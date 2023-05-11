#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        save the user to the database
        Args:
            email (str): user's email address
            hashed_password (str): password hashed by bcrypt's hashpw
        Return:
            Newly created User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self.__session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        takes in arbitrary keyword arguments
        Return:
              the first row found in the users table
               as filtered by the method’s input arguments
        """
        all_users = self._session.query(User)
        for k, v in kwargs.items():
            if k in User.__dict__:
                for user in all_users:
                    if getattr(user, k) == v:
                        return user
                    raise NoResultFound
        raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        update the user’s attributes as passed in the method’s arguments
        then commit changes to the database.
        Returns: None
        """
        try:
            found_user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError
        for k, v in kwargs.items():
            if hasattr(found_user, k):
                setattr(found_user, k, v)
            else:
                raise ValueError
        self.__session.commit()
