import sys
import qrcode

uri = 'otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&period=30'

if sys.argv[1] == '--generate-qr':
    img = qrcode.make(uri)
    img.save('qr.jpg')
    
    print('made it')
    

