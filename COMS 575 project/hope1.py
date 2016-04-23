import cv2
import numpy as np
backsub = cv2.BackgroundSubtractorMOG()
capture = cv2.VideoCapture("C:\\Python27\\videoA5.mp4")
# dic={'road_1':60, 'road_2': 45, 'road_3':30. 'road_4':15}
best_id=0
i = 0
car_w=0
car_e=0
car_n=0
car_s=0
l=0
lst=[]

def check():
    car_w=0
    car_e=0
    car_s=0
    car_n=0
    if capture:
        while True:

            ret, frame = capture.read()
            if ret:
                fgmask = backsub.apply(frame, None, 0.01)
                contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
            # kernel = np.ones((1,1),np.uint8)
            
            # fgmask = cv2.dilate(fgmask,kernel,iterations = 10000)
            # fgmask = cv2.erode(fgmask,kernel,iterations = 10)

                try: hierarchy = hierarchy[0]
                except: hierarchy = []
                for contour, hier in zip(contours, hierarchy):
                    area = cv2.contourArea(contour)
                    (x,y,w,h) = cv2.boundingRect(contour)
                    if w > 10 and h > 10:
                    # print "x: ",x
                    # print "y :", y 

                    # figure out id
                        # best_id+=1
                        if 83<x<85:
                            car_w=car_w+1
                        
                    # car_w=float(car_w/5.6)
                    # print car_w
                    

                    # print "car_west",car_w
                        if 391<x<393:
                            car_e=car_e+1
                        # car_e=float(car_e/10)    


                        # print"car_east",car_e

                        if 283<x<285 and y==554:
                            car_s=car_s+1
                        # car_s=float(car_s/10)    
                        # print"car_south",car_s 
                        if 205<x<207 and y==95:
                            car_n=car_n+1
                        # car_n=float(car_n/10)
                        

                        # print "car_north",car_n            


                        if area> 90:
                        
                            cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 1)

                # print "car_w","car_e","car_s","car_n",car_w/5.6,car_e,car_s,car_n      
                    cv2.putText(frame, str('cars_West:'), (80,100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)
                    cv2.putText(frame, str(int(car_w/5.6)), (170,100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)

                    cv2.putText(frame, str('cars_East:'), (300,100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)
                    cv2.putText(frame, str(int(car_e/10)), (400,100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)
                    cv2.putText(frame, str('car_south:'), (70,500), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)
                    cv2.putText(frame, str(int(car_s/11)), (170,500), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)

                    cv2.putText(frame, str('car_north:'), (70,60), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)
                    cv2.putText(frame, str(int(car_n/10)), (170,60), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 0, 255), 2)

                # g=int(car_w/5.6)
                # print g
            # print(best_id)        
            cv2.imshow("Track", frame)

            # cv2.imshow("background sub", frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        counter_w= int(car_w/5.6)
        counter_e= int(car_e/10)
        counter_s=int(car_s/11)
        counter_n=int(car_n/10)
        dic = {}
        dic["West"]    = counter_w
        dic["North"] = counter_n
        dic["East"]      = counter_e
        dic["South"]  = counter_s
        print(dic)               # {'Square': 3, 'Oval': 2, 'Triangle': 1, 'Rectangle': 4}

        # Sort list of key,value pairs in descending order
        pairs = sorted(dic.items(), key=lambda pair: pair[1], reverse=True)
        print(pairs)                # [('Rectangle', 4), ('Square', 3), ('Oval', 2), ('Triangle', 1)]

        # Get your list, in descending order
        vals = [v for k,v in pairs]
        print(vals)                 # [4, 3, 2, 1]

        # Get the keys of that list, in the same order
        keys = [k for k,v in pairs] # ['Rectangle', 'Square', 'Oval', 'Triangle']
        print(keys)
        # lst.append(counter_w)
        # lst.append(counter_n)
        # lst.append(counter_e)
        # lst.append(counter_s)
        # lst.sort(reverse=True)

        dic={'counter_w' : counter_w ,
             'counter_n'  : counter_n,
             'counter_e'  : counter_e,
             'counter_s'   :counter_s
             }

        lst.append(dic)
        print dic     


        # print lst
        # lst[0]=dic[0];
        # lst[1]=dic[1];
        # lst[2]=dic[2];
        # lst[3]=dic[3];

        
                


check()
