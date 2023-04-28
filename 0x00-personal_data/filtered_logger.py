#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(
        fields:List[str], redaction:str, 
        message:str, separator:str) -> str:
    """
    returns the log message obfuscated: 
    """
    PPI = re.compile(fr'\b({"|".join(fields)})=.*?({separator})')
    print(PPI.sub(fr'\1={redaction}\2', message))
        
    
"""if __name__ == "__main__":
    f = ["password", "date_of_birth"]
    m = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
    filter_datum(f,'xxx', m, ';')"""

