import sys
import qrcode
import qrcode.image.svg
from PIL import Image

uri = 'otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&period=30'

if sys.argv[1] == '--generate-qr':
    if method == 'basic':
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        factory = qrcode.image.svg.SvgGragmentImage
    else:
        factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make(uri, image_factory=factory)
    Image.open(img).save('qr.svg')
    print('made it')
    

