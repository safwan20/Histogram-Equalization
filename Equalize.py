import numpy as np
from PIL import Image
import cv2
import math

def cumsum(histogram):
    result = [histogram[0]]
    for i in histogram[1:]:
        result.append(result[-1] + i)
    return result

def flat(img) :
    Hist = img.flatten()
    return Hist

def Histogram(Hist) :
    histogram = np.zeros(256)
    for pixel in Hist:
        histogram[pixel] += 1
    return histogram

def normalize(cumsumfreqs):
    numerator = (cumsumfreqs - np.min(cumsumfreqs)) * 255
    denorminator = np.max(cumsumfreqs) - np.min(cumsumfreqs)

    result = numerator / denorminator
    result.astype('uint8')

    return result

def normalize_col(x) :
    y = np.ma.masked_equal(x, 0)
    y = (y - y.min()) * 255 / (y.max() - y.min())
    z = np.ma.filled(y, 0).astype('uint8')

    return z

def hist_equal(img) :
    im = cv2.imread(img.filename,0)

    im = np.asarray(im)
    Hist = flat(im)
    histogram = Histogram(Hist)
    cumsumfreqs = cumsum(histogram)
    new_pix = normalize(cumsumfreqs)
    img_new_his = new_pix[Hist]
    img_out = np.reshape(img_new_his, im.shape)
    
    img_out = Image.fromarray(img_out)
    img_out = img_out.convert("L")

    equ_dest = "equalized_" + img.filename 
    
    img_out.save('Equalized_images/'+equ_dest)

    return img_out

def hist_equal_color(image) :
    im = cv2.imread(image.filename)
    b, g, r = cv2.split(im)

    Hist_b = flat(b)
    histogram_b = Histogram(Hist_b)
    cumsumfreqs_b = cumsum(histogram_b)
    new_pix_b = normalize_col(cumsumfreqs_b)
    img_new_his_b = new_pix_b[b]

    Hist_g = flat(g)
    histogram_g = Histogram(Hist_g)
    cumsumfreqs_g = cumsum(histogram_g)
    new_pix_g = normalize_col(cumsumfreqs_g)
    img_new_his_g = new_pix_g[g]

    Hist_r = flat(r)
    histogram_r = Histogram(Hist_r)
    cumsumfreqs_r = cumsum(histogram_r)
    new_pix_r = normalize_col(cumsumfreqs_r)
    img_new_his_r = new_pix_r[r]

    img_out = cv2.merge((img_new_his_b, img_new_his_g, img_new_his_r))

    img_out = Image.fromarray(img_out)
    
    equ_dest = "equalized_" + image.filename 
    
    img_out.save('Equalized_images/' + equ_dest)

    return img_out
