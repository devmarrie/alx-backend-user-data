#!/usr/bin/env python3
"""
SQLAlchemy model named User
"""
from flask_sqlalchemy import db
from flask_user import UserMixin

class Users(db.Models, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    session_id = db.Column(db.String, nullable=False)
    reset_token = db.Column(db.String, nullable=False)