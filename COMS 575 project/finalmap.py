import cv2
import numpy as np
from time import sleep
backsub = cv2.BackgroundSubtractorMOG()
capture = cv2.VideoCapture("C:\\Python27\\videoA11.mp4")
# dic={'road_1':60, 'road_2': 45, 'road_3':30. 'road_4':15}
best_id=0
i = 0
car_w=0
car_e=0
car_n=0
car_s=0
count=0
l=0
t=0
lst=[]

def check():
    count=0
    car_w=0
    car_e=0
    car_s=0
    car_n=0
    if capture:
        while True:

            ret, frame = capture.read()
            if ret:
                # count=count+1
                
                fgmask = backsub.apply(frame, None, 0.01)
                contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
                # print count
            # kernel = np.ones((1,1),np.uint8)
            
            # fgmask = cv2.dilate(fgmask,kernel,iterations = 10000)
            # fgmask = cv2.erode(fgmask,kernel,iterations = 10)

                try: hierarchy = hierarchy[0]
                except: hierarchy = []
                for contour, hier in zip(contours, hierarchy):
                    area = cv2.contourArea(contour)
                    (x,y,w,h) = cv2.boundingRect(contour)
                    if w > 10 and h > 10:
                        # print "x",x
                        # print "y",y
                        print "x: ",x
                        print "y :", y 

                    # figure out id
                        # best_id+=1
                        if 137<x<139 and y==310 or 137<x<139 and y==264:
                            car_w=car_w+1
                        
                        elif 523<x<525 and y==264 or 535<x<537 and y==310:
                            car_w=car_w-1  

                        
                    # car_w=float(car_w/5.6)
                    # print car_w
                    

                    # print "car_westq",car_w
                        if 737<x<739 and y==218 or 737<x<739 and y==172:
                            car_e=car_e+1

                        elif 283<x<285 and y==172 or 263<x<265 and y==218:
                            car_e=car_e-1

                        # car_e=float(car_e/10)    


                        # print"car_east",car_e

                        if 568<x<570 and y==172 or 463<x<465 and y==403:     
                            #y=169"
                            car_s=car_s+1
                        elif 508<x<510 and y==109:
                           
                            car_s=car_s-1    
                        # car_s=float(car_s/10)    
                        # print"car_south",car_s 
                        if 371<x<373 and y==60 or 418<x<420 and y==60:
                            car_n=car_n+1
                        if 367<x<369 and y==402 or 371<x<373 and y==329:
                            car_n=car_n-1    
                        # car_n=float(car_n/10)


                        

                        # print "car_north",car_n            


                        # if area> 90:
                        
                        cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 1)

                # print "car_w","car_e","car_s","car_n",car_w/5.6,car_e,car_s,car_n      
                cv2.putText(frame, str('cars_West:'), (80,100), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
                cv2.putText(frame, str(int(car_w/5)), (170,100), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)

                cv2.putText(frame, str('cars_East:'), (300,100), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
                cv2.putText(frame, str(int(car_e/5)), (400,100), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
                cv2.putText(frame, str('car_south:'), (70,500), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
                cv2.putText(frame, str(int(car_s/5)), (170,500), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)

                cv2.putText(frame, str('car_north:'), (70,60), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
                cv2.putText(frame, str(int(car_n/5)), (170,60), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
                    # for i in range(0,car_w):
                    #     car_w=car_w-1
                    # cv2.putText(frame, str(int(car_w)), (170,100), cv2.FONT_HERSHEY_SIMPLEX,
                            # 0.5, (255, 0, 255), 2)    


                # g=int(car_w/5.6)
                # print g
            # print(best_id)        
            cv2.imshow("Track", frame)

            # cv2.imshow("background sub", frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        counter_w= int(car_w/5)
        counter_e= int(car_e/5)
        counter_s=int(car_s/5)
        counter_n=int(car_n/5)
        dic = {}
        dic["West"]    = counter_w
        dic["North"] = counter_n
        dic["East"]      = counter_e
        dic["South"]  = counter_s
        print(dic)               
        pairs = sorted(dic.items(), key=lambda pair: pair[1], reverse=True)
        print(pairs)                
        vals = [v for k,v in pairs]
        print(vals)               
        keys = [k for k,v in pairs] 
        print(keys)
        numsum = sum(list(vals))
        print numsum
        Time=120
        b=int(Time/numsum)

        print"Green light time for Road ", keys[0],vals[0]*b
        print"Green light time for Road ", keys[1],vals[1]*b
        print"Green light time for Road ", keys[2],vals[2]*b
        print"Green light time for Road ", keys[3],vals[3]*b


        # for i in range(0,vals[0]*b):
        #     g= 10 - i
        #     sleep(1)
        # print g
        # cv2.putText(frame, str((g)), (170,500), cv2.FONT_HERSHEY_SIMPLEX,
        #                     0.5, (255, 0, 255), 2)

check()        


        # lst.append(counter_w)
        # lst.append(counter_n)
        # lst.append(counter_e)
        # lst.append(counter_s)
        # lst.sort(reverse=True)

        # dic={'counter_w' : counter_w ,
        #      'counter_n'  : counter_n,
        #      'counter_e'  : counter_e,
        #      'counter_s'   :counter_s
        #      }

        # lst.append(dic)
        # print dic     


        # print lst
        # lst[0]=dic[0];
        # lst[1]=dic[1];
        # lst[2]=dic[2];
        # lst[3]=dic[3];

        
                




# def check1():
#     if capture:
#         while True:

#             ret, frame = capture.read()
#             if ret:
#                 fgmask = backsub.apply(frame, None, 0.01)
#                 contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,
#                                                cv2.CHAIN_APPROX_NONE)
#             # kernel = np.ones((1,1),np.uint8)
            
#             # fgmask = cv2.dilate(fgmask,kernel,iterations = 10000)
#             # fgmask = cv2.erode(fgmask,kernel,iterations = 10)

#                 try: hierarchy = hierarchy[0]
#                 except: hierarchy = []
#                 for contour, hier in zip(contours, hierarchy):
#                     area = cv2.contourArea(contour)
#                     (x,y,w,h) = cv2.boundingRect(contour)
#                 check()    
#                 for i in range(0,10):
#                     g= 10 - i
#                     sleep(1)
#                 cv2.putText(frame, str((g)), (170,500), cv2.FONT_HERSHEY_SIMPLEX,
#                             0.5, (255, 0, 255), 2)


#                 # cv2.putText(frame, str('cars_West:'), (80,100), cv2.FONT_HERSHEY_SIMPLEX,
#                             # 0.5, (255, 0, 255), 2)    

# check1()S