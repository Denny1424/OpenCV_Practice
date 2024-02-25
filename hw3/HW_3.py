import cv2
import numpy as np

action = input('請輸入你想做的動作\n1 = 輸入T,F生成Tf\n2 = 輸入Tf生成T,F\n：')


if action == '1':
    print('！！！！！！！！注意！！！！！！！！！')
    print('！！！檔名輸入錯誤才有可能跳錯誤！！！')
    T_name = input('請將"T"圖片放在同一資料夾下，並輸入完整檔名(含副檔名)：')
    F_name = input('請將"F"圖片放在同一資料夾下，並輸入完整檔名(含副檔名)：')

    T = cv2.imread(f'{T_name}')
    F = cv2.imread(f'{F_name}')

    print('不用擔心，不是你電腦當掉\n程式是用3迴圈去跑的所以很慢，如果像素點過多就要跑很久')

    C_1,R_1,Z = T.shape
    C_2,R_2,Z_2 = F.shape

    C = min(C_1,C_2)
    R = min(R_1,R_2)

    T = cv2.resize(T, (R, C))
    F = cv2.resize(F, (R, C))


    R34 = np.ones((C,R,Z),dtype = np.uint8)*12
    R12 = np.ones((C,R,Z),dtype = np.uint8)*3
    ab = cv2.bitwise_and(T,R34)
    cd = cv2.bitwise_and(T,R12)



    e = F >> 7
    f = F << 1 >> 7

    for i in range(len(T)):
        if i%100 == 0 : print(f'現在執行第{i}－Column')
        for j in range(len(T[i])):
            for g in range(len(T[i][j])):
                
                if e[i][j][g] == 0:
                    if ab[i][j][g] == 4:
                        T[i][j][g] -= 4
                    if ab[i][j][g] == 8:
                        T[i][j][g] += 4                     
           
                if e[i][j][g] == 1:
                    if ab[i][j][g] == 0:
                        T[i][j][g] += 4
                    if ab[i][j][g] == 12:
                        T[i][j][g] -= 4
                        
                if f[i][j][g] == 0:
                    if cd[i][j][g] == 1:
                        T[i][j][g] -= 1
                    if cd[i][j][g] == 2:
                        T[i][j][g] += 1
                
                if f[i][j][g] == 1:
                    if cd[i][j][g] == 0:
                        T[i][j][g] += 1
                    if cd[i][j][g] == 3:
                        T[i][j][g] -= 1

    print("執行完成")
    cv2.imwrite('Tf.png',T)
    print("已儲存一個名字為 Tf.png 的檔案")
    cv2.imshow('Tf',T)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if action == '2':
    print('！！！！！！！！注意！！！！！！！！！')
    print('！！！檔名輸入錯誤才有可能跳錯誤！！！')
    Tf_name = input('請將"Tf"圖片放在同一資料夾下，並輸入完整檔名(含副檔名)：')
    Tf = cv2.imread(f'{Tf_name}')
    ab = Tf << 4 >> 6
    cd = Tf << 6 >> 6

    a = ab >> 1
    b = ab - (a << 1)
    c = cd >> 1
    d = cd - (c << 1)

    e = cv2.bitwise_xor(a,b)
    f = cv2.bitwise_xor(c,d)

    F = (e << 7) + (f << 6)
    
    print(f'----------------F----------------\n{F}')
    print('此結果為將被藏著的圖還原出來')
    
    cv2.imshow("F",F)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


