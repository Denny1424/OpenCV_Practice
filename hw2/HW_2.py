import cv2
import numpy as np
import time
img = cv2.imread("halloween.png")


'''糖果'''

speed = 0.005

def candy(zeros,x,y,a):
    pts_1 = np.array([[int(x+3/4*a),int(y+1/3*a)],[int(x+9/4*a),int(y+5/4*a)],[int(x+6/4*a),int(y+1/3*a)],[int(x+10/4*a),int(y)],\
                    [int(x+6/4*a),int(y-1/3*a)],[int(x+9/4*a),int(y-5/4*a)],[int(x+3/4*a),int(y-1/3*a)]])    
  
    pts_2 = np.array([[int(x-3/4*a),int(y+1/3*a)],[int(x-9/4*a),int(y+5/4*a)],[int(x-6/4*a),int(y+1/3*a)],[int(x-10/4*a),int(y)],\
                    [int(x-6/4*a),int(y-1/3*a)],[int(x-9/4*a),int(y-5/4*a)],[int(x-3/4*a),int(y-1/3*a)]])
    
    cv2.fillPoly(zeros, [pts_1], (0,100,255))
    cv2.fillPoly(zeros, [pts_2], (0,100,255))
    cv2.circle(zeros,(x,y),a,(0,0,255),-1)


xylist = []
n = np.random.randint(20,40)
for i in range(n):
    x = np.random.randint(1,1200)
    y = np.random.randint(1,1200)
    y_step = np.random.randint(2,5)
    x_step = np.random.randint(2,5)
    k = np.random.randint(0,100)
    a = np.random.randint(15,20)
    xylist.append([x,y,x_step,y_step,k,a])



while cv2.waitKey(1) == -1:

    zeros = np.zeros((img.shape), dtype = np.uint8)

    

    for i in range(n):
        
        candy(zeros,xylist[i][0],xylist[i][1],xylist[i][5])
        
        if xylist[i][4]%100 <50:
            xylist[i][0] += xylist[i][2]
        else:
            xylist[i][0] -= xylist[i][2]
        
        if  xylist[i][1] > 1200+a:
            xylist[i][1] = 0
            xylist[i][0] = np.random.randint(1,1200)

        elif xylist[i][4]%50 < 40:
            xylist[i][1] += xylist[i][3]
        elif xylist[i][4]%50 >= 10:
            xylist[i][1] -= int(xylist[i][3]/7)
        xylist[i][4] += 1
        
        
    mk_img = cv2.addWeighted(img,1,zeros,1,0)

        
    cv2.imshow("Bouncing Ball",mk_img)
    time.sleep(speed)

cv2.destroyAllWindows()