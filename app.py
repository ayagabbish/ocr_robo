from ast import While
import pytesseract
import cv2 as cv
import YB_Pcb_Car  
import time

car = YB_Pcb_Car.YB_Pcb_Car()
car.Ctrl_Servo(1, 90) 
time.sleep(0.5)
    
car.Ctrl_Servo(2, 90) 
time.sleep(0.5)
cap = cv.VideoCapture(0)

def get_ocr(cap):
    img_rgb = cv.cvtColor(cap,cv.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)


while True:
    is_success,frame = cap.read()
    if not is_success:
        print('fail to capture image.')
        break
    cv.imshow('OCR Strean', frame)
    k = cv.waitKey(1)
    if k%256 == 32:
        cv.imwrite("img.jpg",frame)
        print('image captured')
        t = get_ocr(frame)
        print (t)
        if "Happy" in t:
            car.Ctrl_Servo(1, 90) 
            time.sleep(0.5)
    
            car.Ctrl_Servo(2, 0) 
            time.sleep(0.5)
            car.Ctrl_Servo(2, 90) 
            time.sleep(0.5)
        if "Sad" in t:
            car.Ctrl_Servo(1,180)
            time.sleep(0.5)
            car.Ctrl_Servo(2,90)
            time.sleep(0.5)
            car.Ctrl_Servo(1,90)
            time.sleep(0.5)
            

            cv.waitKey(0)
            