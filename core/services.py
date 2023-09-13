import os
import sys
import redis_app.services as redis_services


def create_otp(key, header=None, length=5, **options):
    """
    generates otp with given length and stores it with given key and header.

    :param str key: key value to be used for storing otp.
    :param str header: header value to be used for storing otp.
    :param int length: length of generated otp.

    :keyword int expire: number of seconds to expire the key.
                         defaults to None if not provided and
                         the key won't be expired.

    :rtype: str
    """

    otp = str(int.from_bytes(os.urandom(int(length / 2)), sys.byteorder))
    otp = otp[:length]
    if len(otp) < length:
        otp = otp.zfill(length)

    redis_services.set(redis_services.make_key(key, header), otp, **options)
    return otp


def is_otp_match(otp, key, header=None, **options):
    """
    gets a value indicating that given otp matches the stored value for given key and header.

    :param str otp: otp value.
    :param str key: key value to be used for getting otp.
    :param str header: header value to be used for getting otp.

    :rtype: bool
    """

    result_otp = redis_services.get(redis_services.make_key(key, header))
    if result_otp is None or result_otp.decode('utf-8') != otp:
        return False

    return True
