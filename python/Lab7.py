from PIL import Image

im = Image.open(r"bbh.jpg")

im1 = im.filter(ImageFilter.BoxBlur(4))

im1.show()