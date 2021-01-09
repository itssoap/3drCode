from PIL import Image
from sklearn.cluster import KMeans
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
import platform

def is_wsl() -> bool:
    platform_info = platform.uname()
    return platform_info.system == "Linux" and 'microsoft' in platform_info.release.lower()

def colorset(file_name): #so here we get an image qwith a white bg
    tdr=Image.open(file_name)
    tdr=tdr.convert("RGBA") #forcing its color-space to rgba for trnasparency when we scrape out white
    data=tdr.getdata()
    non_whites=[] #to store all non-white-ish colors
    for cols in data:
        if cols[0] in list(range(190, 256)):
            non_whites.append((0,0,0,0))
        else:
            non_whites.append(cols)
    tdr.putdata(non_whites) #contains all the non-white-ish colors
    tdr.save("temp.png")
#bg = Image.new("RGBA", tdr.size, "WHITE")
#bg.putdata(colors)
#bg.show()
    return "temp.png"

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def HEX2RGB(color):
    color=color.lstrip('#') # remove the # from Hex Code
    return [int(color[i:i+2], 16) for i in (0,2,4)] #convert hex values from base16 to int and make list
    
def woohoo_machine_learning(temp_file): #this function is to extract major colors from the messed up temp file
    image = cv2.imread(temp_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    try:
        if is_wsl():
            backend = "TkAgg" #WSL doesnt support Qt5Agg
        else:
            backend = "Qt5Agg"
        matplotlib.use(backend)
    except ImportError:
        pass
    #matplotlib.use("TkAgg")
    #plt.imshow(image)
    #plt.show() #to check the newly generated temp image
    
    #    RESIZE IMAGE FOR FASTER PROCESSING
    resized=cv2.resize(image, (250,250), interpolation=cv2.INTER_AREA) # I tried 500x500, but MemoryError, 250x250
    resized=resized.reshape(resized.shape[0]*resized.shape[1], -1) #Image is 3D (idk why), check this error
    #ValueError: Found array with dim 3. Estimator expected <= 2.
    #SO had to reshape it to dim=2, used -1 to determine it automatically
    
    #    HERE COMES MACHINE LEARNING !!!
    number_of_colors=8
    clf=KMeans(n_clusters = number_of_colors)
    labels=clf.fit_predict(resized)
    
    #   TRAINING ENDS HERE< WE WILL NOW USE THE COLORS
    counts=Counter(labels)
    center_colors=clf.cluster_centers_
    
    #   EXTRACT COLOR TO PLOT
    ordered_colors=[center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    #rgb_colors = [int_colors for i in rgb_colors]
    plt.figure(figsize = (8, 6))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
    plt.show()
    base_colors(hex_colors)
    #rgb_colors = [ordered_colors[i] for i in counts.keys()]
def base_colors(hex_colors):
    rgb_colors=[]
    for cols in hex_colors:
        rgb_colors.append(HEX2RGB(cols))
    print(rgb_colors)
    
