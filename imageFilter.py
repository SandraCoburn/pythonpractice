#import image
from PIL import Image, ImageFilter
before = Image.open("bridge.jpeg")
after =before.filter(ImageFilter.BLUR)
after.save("out.jpeg")
