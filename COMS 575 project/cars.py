import cv2
backsub = cv2.BackgroundSubtractorMOG()
capture = cv2.VideoCapture("C:\Python27\cars1.mov")
best_id=0
car=0
CARS=0
i = 0
if capture:
  while True:

    ret, frame = capture.read()
    if ret:
        fgmask = backsub.apply(frame, None, 0.01)
        contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
        
        for i in contours:
            M = cv2.moments(i)
            cx = int(M['m10']/(M['m00']+0.01))
            cy = int(M['m01'])/(M['m00']+0.01)
            area = cv2.contourArea(i)
            print area

            (x,y,w,h) = cv2.boundingRect(i)
            if w > 20 and h > 20:
                # figure out id
                best_id+=1

                cv2.rectangle(fgmask, (x,y), (x+w,y+h), (255, 0, 0), 2)
                print x
                if 11<x<13:
                    car=car+1
                elif 1251<x<1253 :
                    CARS=CARS+1    
        # cv2.putText(frame, str(best_id), (x,y-5), cv2.FONT_HERSHEY_SIMPLEX,
        #             0.5, (255, 0, 0), 2)
        cv2.putText(fgmask, str('cars:'), (20,100), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 255), 2)
        cv2.putText(fgmask, str(car), (70,100), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 255), 2)

        cv2.putText(fgmask, str('CARS:'), (70,400), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
        cv2.putText(fgmask, str(CARS), (110,400), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)
        print(best_id)     

        if car>CARS:
            cv2.circle(fgmask,(200,200), 20, (255,255,0), -1)
        elif CARS>car:    
            cv2.circle(fgmask,(700,400), 20, (255,255,0), -1)

        # cv2.imshow("Track", frame)
        cv2.imshow("background sub", fgmask)
    key = cv2.waitKey(10)
    if key == ord('q'):
            break