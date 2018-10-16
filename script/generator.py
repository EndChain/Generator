import pyqrcode
import barcode
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image


def generate( qrAddress, barCode ):
    # Generate EAN13 Barcode
    from barcode.writer import ImageWriter
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(barCode, writer=ImageWriter())
    fullname = ean.save('ean13_barcode')
    #Crop the Barcode
    im=Image.open("ean13_barcode.png")
    #print im.size
    im2=im.crop((65, 0, 460, 200))
    #print im2.size
    im2.save("ean13_barcode_cropped.png")

    #Generate QrCode
    url = pyqrcode.create(qrAddress,error = 'H', version=5)
    url.png('generatedQR.png',scale=10)

    #Combine the Barcode and QRcode
    im = Image.open('generatedQR.png')
    im = im.convert("RGBA")
    logo = Image.open('ean13_barcode_cropped.png')
    box = (190,200,450,310)
    im.crop(box)
    region = logo
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    im.paste(region,box)
    im.show()

    #Save the combination
    im.save('out.png')
    return True

generate('https://www.endchain.io/', u'5901234123457')
