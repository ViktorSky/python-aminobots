from typing import Union
from ..enums import ClientType
from ..exceptions import InvalidSID

import hashlib
import base64
import json
import time
import hmac
import os

__all__ = (
    'apis',
    'decorators',
    'wrappers',
    'device_gen',
    'update_device',
    'signature_gen',
    'encode_sid',
    'decode_device',
    'decode_signature',
    'decode_sid'
)

PREFIX: str = '19'
DEVKEY: str = 'e7309ecc0953c6fa60005b2765f99dbbc965c8e9'
SIGKEY: str = 'dfa5ed192dda6e88a12fe12130dc6206b1251e44'


def device_gen(identifier: bytes = os.urandom(20)) -> str:
    device_info: bytes = bytes.fromhex(PREFIX) + identifier
    new_device: str = (
        device_info + hmac.new(
            bytes.fromhex(DEVKEY),
            device_info,
            hashlib.sha1
        ).digest()
    ).hex().upper()
    return new_device


def update_device(device: str) -> str:
    return device_gen(decode_device(device)['id'])


def signature_gen(data: str) -> str:
    new_signature: str = base64.b64encode(
        bytes.fromhex(PREFIX) + hmac.new(
            bytes.fromhex(SIGKEY),
            data.encode('utf-8'),
            hashlib.sha1
        ).digest()
    ).decode('utf-8')
    return new_signature


def encode_sid(
    uid: str,
    ip_address: str,
    clientType: ClientType = ClientType.MASTER,
    timestamp: int = int(time.time()),
    sidKey: Union[str, bytes] = os.urandom(20)
) -> str:
    data: bytes = json.dumps({
        '1': None,
        '0': 2,
        '3': 0,
        '2': str(uid),
        '5': int(timestamp),
        '4': str(ip_address),
        '6': int(clientType)
    }).encode("utf-8")
    sid_info: bytes = bytes.fromhex("02") + data
    if isinstance(sidKey, str):
        sidKey = bytes.fromhex(sidKey)
    new_sid: str = base64.urlsafe_b64encode(
        sid_info + hmac.new(
            sidKey,
            sid_info,
            hashlib.sha1
        ).digest()
    ).decode("utf-8")
    return new_sid.strip("=")


def decode_device(device: str) -> dict:
    device: bytes = bytes.fromhex(device)
    return dict(
        prefix=device[0:1],
        id=device[1:21],
        hash=device[21:]
    )


def decode_signature(sig: str) -> dict:
    # dict(prefix=None, hash=None, data=None)
    raise NotImplementedError


def decode_sid(sid: str) -> dict:
    try:
        decoded_sid: bytes = base64.urlsafe_b64decode(
            sid + "=" * (4 - len(sid) % 4)
        )
        data: dict = json.loads(decoded_sid[1:-20].decode("utf-8"))
    except (TypeError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise InvalidSID(sid) from exc
    else:
        return dict(
            version=data["0"],
            null=data["1"],  # ?
            uid=data["2"],
            objectType=data["3"],
            ip_address=data["4"],
            timestamp=data["5"],
            clientType=data["6"],
            sidKey=decoded_sid[-20:].hex(),
            sidType=decoded_sid[:2].hex(),
        )
