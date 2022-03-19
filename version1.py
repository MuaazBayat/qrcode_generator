import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr = pyqrcode.create("https://www.youtube.com/results?search_query=mrbeast")
qr.png("mrbeast.png",scale=8)
