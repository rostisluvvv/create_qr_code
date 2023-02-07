import pyqrcode
import png

url_link: str = 'https://github.com/rostisluvvv'
qr_code = pyqrcode.create(url_link)
qr_code.png('link_GH.png', scale=5)