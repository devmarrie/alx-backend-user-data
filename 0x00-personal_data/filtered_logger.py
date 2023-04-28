#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated:
    """
    PII = re.compile(fr'\b({"|".join(fields)})=.*?({separator})')
    return re.sub(PII, fr'\1={redaction}\2', message)
