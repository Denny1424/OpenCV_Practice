import cv2
import numpy as np
img = cv2.imread("101.png")

'''國旗繪製'''
x_1 = [10000]
y_1 = [10000]
a_1 = [0]
for i in range(0,5):
    rd = 0
    a = np.random.uniform(2,3)
    while rd != len(x_1):
        rd = 0
        x = np.random.randint(0,1200-int(120*a))
        y = np.random.randint(0,1200-int(120*a))

        for i in range(len(x_1)):
            if (np.abs(x_1[i]-x) > 120*a_1[i] or np.abs(y_1[i]-y) > 80*a_1[i]) and\
                (np.abs(x_1[i]-x) > 120*a or np.abs(y_1[i]-y) > 80*a):
                rd += 1
            else: continue

    
    cv2.rectangle(img,(x,y),(x+int(120*a),int(y+80*a)),(255,255,255),2,shift = 0)
    cv2.rectangle(img,(x,y),(x+int(120*a),int(y+80*a)),(0,0,242),-1,shift = 0)
    cv2.rectangle(img,(x,y),(x+int(60*a),int(y+40*a)),(204,40,0),-1,shift = 0)
    
    k_x = []
    k_y = []
    for i in range(0,12):
        k_x.append(int(x + 30*a + 15*a*np.cos(i*np.pi*5/6)))
        k_y.append(int(y + 20*a + 15*a*np.sin(i*np.pi*5/6)))
        
    array_k_x = np.array(k_x)
    array_k_y = np.array(k_y)
    
    pts = np.c_[array_k_x,array_k_y.T]
    
    cv2.polylines(img,[pts],True,(255,255,255),1)
    cv2.fillPoly(img, [pts], (255,255,255))
    
    cv2.circle(img,(x+int(30*a),y+int(20*a)),int(8.5*a),(204,40,0),-1)
    cv2.circle(img,(x+int(30*a),y+int(20*a)),int(7*a),(255,255,255),-1)
    
    x_1.append(x)
    y_1.append(y)
    a_1.append(a)

'''祝賀語'''

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Happy Birt",(155,450),font,2.5,(255,255,255),10)
cv2.putText(img,"Happy Birt",(155,450),font,2.5,(204,40,0),5)


cv2.putText(img,"hday Taiwan",(568,450),font,2.5,(255,255,255),10)
cv2.putText(img,"hday Taiwan",(568,450),font,2.5,(0,0,242),5)




cv2.imshow("My Draw",img)
cv2.waitKey(0)
cv2.destroyAllWindows()