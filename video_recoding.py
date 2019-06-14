import numpy as np
import cv2
import time
import csv

cap = cv2.VideoCapture(2)
label = ["run", "stop", "turn_left", "turn_right"]
label_map = {i:v for v,i in enumerate(label)}

label_list = []

curr = "stop"
start = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if start:
        t = time.time()
        file_name = "frame%d.jpg" % t
        label_list.append((label_map[curr], file_name))
        cv2.imwrite("img/" + file_name, frame)
        
    cv2.imshow('capture', frame)

    print("curr: " + curr)
    if cv2.waitKey(1) == ord('a'):
        print('Start Recoding ... ')
        start = True
    elif cv2.waitKey(1) == ord('z'):
        curr = "run"
    elif cv2.waitKey(1) == ord('x'):
        curr = "stop"
    elif cv2.waitKey(1) == ord('c'):
        curr = "turn_left"
    elif cv2.waitKey(1) == ord('v'):
        curr = "turn_right"
    elif cv2.waitKey(1) == ord('q'):
        print('Stop Recoding ... ')
        start = False
        break

with open('label.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(label_list)

cap.release()
cv2.destroyAllWindows()
