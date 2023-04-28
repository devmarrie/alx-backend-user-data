#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated:
    """
    PII = re.compile(fr'\b({"|".join(fields)})=.*?({separator})')
    return re.sub(PII, fr'\1={redaction}\2', message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        calls the format method of the parent class LogRecord
        """
        message = super(RedactingFormatter, self).format(record)
        new = filter_datum(self.fields, self.REDACTION,
                           message, self.SEPARATOR)
        return new


def get_logger() -> logging.Logger:
    """
    Takes no arguments and returns a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
