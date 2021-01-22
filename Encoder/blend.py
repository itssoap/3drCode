from PIL import Image
import numpy as np

# Load both images and make into Numpy arrays
a=np.array(Image.open('out/1.png').convert('RGBA'))
b=np.array(Image.open('out/2.png').convert('RGBA'))
c=np.array(Image.open('out/3.png').convert('RGBA'))
# Make masks of all opaque pixels in each image, i.e. alpha>0
mA = a[...,3] > 0
mB = b[...,3] > 0
mC = c[...,3] > 0

# Make empty result image
res = np.zeros_like(a)
res[mA] = np.uint8([0,255,255,255])
res[mB] = np.uint8([255,0,255,255])
res[mC] = np.uint8([255,255,0,255])
res[mA & mB] = np.uint8([0,0,255,255])
res[mB & mC] = np.uint8([255,0,0,255])
res[mC & mA] = np.uint8([0,255,0,255])
res[mA & mB & mC] = np.uint8([0,0,0,255])
# Save result

image=Image.fromarray(res)
new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
new_image.convert('RGB').save('test.png', "PNG")
new_image.convert('RGB').save('test.jpg', "JPEG")
