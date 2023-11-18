#!/usr/bin/env python3
"""
Authentification module
"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """
    hashes pasword with bcryp.hashpw
    returns salted hash of the input password
    """
    return hashpw(password.encode('utf-8'), gensalt())
