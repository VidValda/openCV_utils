import cv2
import numpy as np
import matplotlib.pyplot as plt
class CountoursRb:

    def segment(self, image):

        image_copy = np.copy(image)
        gray_image = cv2.cvtColor(image_copy,cv2.COLOR_RGB2GRAY)
        image_base = np.copy(image_copy)
        image_base2 = np.copy(image_copy)

        filtered_image = cv2.GaussianBlur(gray_image,(5,5),0)

        ret, thresh = cv2.threshold(filtered_image,0,255,cv2.THRESH_OTSU)

        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        img_contours = cv2.drawContours(image_base,contours,-1,(0,255,0),3)

        edged = cv2.Canny(filtered_image,150,255)
        kernel = np.ones((3,3),np.uint8)
        edged_best = cv2.dilate(edged,kernel,iterations=1)
        contours2, hierarchy2 = cv2.findContours(edged_best,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        img_contours2 =  cv2.drawContours(image_base2,contours2[3],-1,(0,255,0),3)

        for i,c in enumerate(contours):
            M = cv2.moments(c)
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.drawContours(img_contours, [c], -1, (0, 255, 0), 2)
                cv2.circle(img_contours, (cX, cY), 7, (0, 0, 255), -1)
                cv2.putText(img_contours, str(hierarchy[0][i]) , (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            except:
                pass
        # for i,c in enumerate(contours2):
        #   M = cv2.moments(c)
        #   cX = int(M["m10"] / M["m00"])
        #   cY = int(M["m01"] / M["m00"])
        #   cv2.drawContours(img_contours2, [c], -1, (0, 255, 0), 2)
        #   cv2.circle(img_contours2, (cX, cY), 7, (255, 255, 255), -1)
        #   cv2.putText(img_contours2, str(hierarchy2[0][i]) , (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


        #f, axarr = plt.subplots(1,3,figsize=(15,15))
        #axarr[0].imshow(image)
        #axarr[1].imshow(img_contours)
        #axarr[2].imshow(img_contours2)

        return (image,img_contours,img_contours2)
