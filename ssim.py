from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import math

def mse(imageA, imageB):	
	err = np.sum(np.absolute(imageB.astype("float") - imageA.astype("float")))
	err /= float(imageA.shape[0] * imageA.shape[1])	
	return err



def psnr(imageA, imageB):
	mse = np.mean((imageA - imageB) ** 2)
	if(mse == 0): 
		return 100
	max_pixel = 255.0
	psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
	return psnr



def compare_images(imageA, imageB, title):	
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	p = psnr(imageA, imageB)	
	print("mae ",m)
	print("ssim ",s)
	print("psnr ",p)


original = cv2.imread("enh.jpg")
contrast = cv2.imread("orig.jpg")

original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)


compare_images(original, contrast, "Original vs. Contrast")
