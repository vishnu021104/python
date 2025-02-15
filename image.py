import PIL
from PIL import Image

img=PIL.image.open("C:\Users\vishn\OneDrive\Pictures.jpg")
width,height=img.size

print(width,height)