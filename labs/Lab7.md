Here are the steps I did to create Lab 7:

virtualenv ~/venv/webscraping/Scripts/activate.ps1
pip install pillow
python

>>> from PIL import Image,ImageFilter

>>> myImage = Image.open('C:/Users/Administrator/Pictures/Saved Pictures/bbh.jpg')
>>> myImage.load
<bound method WebPImageFile.load of <PIL.WebPImagePlugin.WebPImageFile image mode=RGBA size=1060x993 at 0x2064CE64EB0>>
>>> myImage.format
'WEBP'
>>> myImage.size
(1060, 993)
>>> myImage.show()


>>> blur = myImage.filter(ImageFilter.BLUR)
>>> blur.show()

>>> from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE)
>>> img2 = myImage.filter(EDGE_ENHANCE)
>>> img2.show()

>>> img3 = myImage.filter(CONTOUR)
>>> img3.show
<bound method Image.show of <PIL.Image.Image image mode=RGBA size=1060x993 at 0x2064CF716D0>>
>>> img3.show()


>>> quit()

>>> deactivate
