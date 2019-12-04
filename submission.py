import sys
import hmac
import hashlib
import qrcode
import time
import datetime
import base64

uri = 'otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&period=30'

if sys.argv[1] == '--generate-qr':
    img = qrcode.make(uri)
    img.save('qr.jpg')
    
if sys.argv[1] == '--get-otp':
    i = datetime.datetime.now()
    j = time.mktime(i.timetuple())
    k = j // 30
    T = int(k)
    T_array = bytearray()
    
    while T != 0:
        T_array.append(T & 0xff)
        T >>= 8
    result = bytes(bytearray(reversed(T_array)).rjust(8, b'\0'))

    key = base64.b32decode('JBSWY3DPEHPK3PXP')
    
    hasher = hmac.new(key, result, hashlib.sha1)
    hmac_result = bytearray(hasher.digest())
    
    offset = hmac_result[19] & 0xf
    bin_code = ((hmac_result[offset] & 0x7f) << 24 |
                (hmac_result[offset + 1] & 0xff) << 16 |
                (hmac_result[offset + 2] & 0xff) << 8 |
                (hmac_result[offset + 3] & 0xff))
    bin_num = int(bin_code)
    str_code = str(bin_code % 10 ** 6)
    while len(str_code) < 6:
        str_code = '0' + str_code
    print(str_code)

    

