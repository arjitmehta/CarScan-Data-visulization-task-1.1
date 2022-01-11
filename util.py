


from matplotlib import patches
import numpy as np
import  matplotlib.pyplot as plt
import json
from PIL import Image
#from numpy import asarray
#import cv2

    
def task1(img,data,visibility=0.3):
    Json=open(data)
    data = json.load(Json)
    img = Image.open(img)
    #img_cv=cv2.imread("1.jpg")
    #np_img= asarray(img)
    #print(np_img)
    fig = plt.figure(figsize = (25,15))
    plt.subplot(121)
    Axes = fig.add_axes([0,0,1,1])
    plt.imshow(img)
    if len(data)<=2:
        s=0
        e=len(data)
    else:
        s=1
        e=len(data)-1
    for i in range(s,e):
        box_width = data[i]['original_width']
        box_height =data[i]['original_height']
        x1 = 100000
        x2 = 0
        y1=100000
        y2 = 0
        #a=[]
        for x,y in data[i]['value']['points']:
            temp1 = (x*box_width)/100
            temp2 = (y*box_height)/100
    #         a.append(x)
            #print(mask)

            if(x1 > temp1):
                x1 = temp1
            if(x2 < temp1):
                x2 = temp1
            if(y1 > temp2):
                y1 = temp2
            if(y2 < temp2):
                y2= temp2
        l = x2- x1
        b = y2 - y1
        X_cen = x1+(l/2)
        Y_cen = y1+(b/2)
        eclip = patches.Ellipse((X_cen,Y_cen),l,b,facecolor = 'none',edgecolor = 'r',angle=0)
        Axes.add_patch(eclip)

    # mask=a
    # mask_arr=np.array(mask)
    # #print(mask)

    # mask=cv2.resize(np_img,(l,b))


    body_color = [(1,1,0,visibility),(0,1,0,visibility),(1,0,1,visibility),(0,0,1,visibility),(1,0,0,visibility),(1,1,1,visibility)]
    edge_val = [(1,1,0),(0,1,0),(1,0,1),(0,0,1),(1,0,0),(1,1,1)]
    fig = plt.figure(figsize = (25,15))
    plt.subplot(121)
    Axes = fig.add_axes([0,0,1,1])
    plt.imshow(img)
    p=0
    for i in range(s,e):
        box_width = data[i]['original_width']
        box_height =data[i]['original_height']
        x1 = 100000
        x2 = 0
        y1=100000
        y2 = 0

        for x,y in data[i]['value']['points']:
            temp1 = (x*box_width)/100
            temp2 = (y*box_height)/100

            if(x1 > temp1):
                x1 = temp1
            if(x2 < temp1):
                x2 = temp1
            if(y1 > temp2):
                y1 = temp2
            if(y2 < temp2):
                y2= temp2
        l = x2- x1
        b = y2 - y1
    #     area_mask=img_cv[int(y1):int(y2), int(x1):int(x2)]
    #     imgray = cv2.cvtColor(area_mask, cv2.COLOR_BGR2GRAY)
    #     ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    #     contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #area_mask.show()

        X_cen = x1+(l/2)
        Y_cen = y1+(b/2)
        #print('x1,x2:',x1,x2)
        #print('l,b',l,b)
        #print('X_cen,Y_cen:',X_cen,Y_cen)
        #cv2.RETR_TREE()
        #patches.BoxStyle()
        if p <6:
            bbox = patches.Rectangle((x1,y1), l, b, edgecolor = edge_val[p], facecolor ='none',label='Label')
            #for cnt in contours:
    #             cv2.fillPoly(area_mask, [cnt], body_color[j])
            eclip = patches.Ellipse((X_cen,Y_cen),l,b,facecolor = body_color[p],edgecolor = edge_val[p],angle=0)
        else:
            p=0
            bbox = patches.Rectangle((x1,y1), l, b, edgecolor = edge_val[p], facecolor = 'none' ,label='Label')
            #for cnt in contours:
    #             cv2.fillPoly(area_mask, [cnt], (body_color[j]))
            eclip = patches.Ellipse((X_cen,Y_cen),l,b,facecolor = body_color[p],edgecolor = edge_val[p],angle=0)
        p+=1

        cen_x =x1
        cen_y = y1
        plt.text(cen_x, cen_y,"".join(data[i]['value']['polygonlabels']),color = 'black',ha='right',va = 'top',size=20)
        Axes.add_patch(bbox)
        Axes.add_patch(eclip)
        #cv2.imshow("Image", img_cv)
        #plt.imshow(img_cv)
        #cv2.imshow("Black image", black_image)
        #cv2.waitKey(0)





