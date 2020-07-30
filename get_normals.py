import numpy as np
import cv2

# create a meshgrid for coordinate calculation
r,c = np.shape(ori_img)
r_ = np.linspace(0,r,r+1)
c_ = np.linspace(0,c,c+1)
x_m, y_m = np.meshgrid(c_, r_, sparse=False, indexing='ij')


im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for c in contours:
     # Get the boundingbox
     x,y,w,h = cv2.boundingRect(c)

     # calculate x,y coordinate of center
     # Get the corresponding roi for calculation
     weights = ori_img[y:y+h,x:x+w]
     roi_grid_x = x_m[y:y+h,x:x+w]
     roi_grid_y = y_m[y:y+h,x:x+w]

     # get the weighted sum
     weighted_x = weights * roi_grid_x
     weighted_y = weights * roi_grid_y

     cx = np.sum(weighted_x) / np.sum(weights)
     cy = np.sum(roi_grid_y) / np.sum(weights)