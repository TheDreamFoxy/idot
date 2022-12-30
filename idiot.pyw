import cv2
from ffpyplayer.player import MediaPlayer
import random
import string
from win32api import GetSystemMetrics
import threading
import subprocess

monitor_x = GetSystemMetrics(0)
monitor_y = GetSystemMetrics(1)

def get_random_string(length):
# choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def set_math(n, direction):
    return n + direction

cap = cv2.VideoCapture('./idiot.mp4')
player = MediaPlayer('./idiot.mp4')
val = ''

imshow_name = "Idiot_"+ get_random_string(5)

math_x = random.randrange(0, monitor_x)
math_y = random.randrange(0, monitor_y)

direction_x = random.randrange(15, 50)
direction_y = random.randrange(15, 50)

while(cap.isOpened()):

    ret, frame = cap.read()
    framee, val = player.get_frame()

    if val != 'eof' and framee is not None:
        img, t = framee
        # display img

    #cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    math_x = set_math(math_x, direction_x)
    math_y = set_math(math_y, direction_y)

    if math_x > monitor_x or math_x < 0:
        if(direction_x > 0):
            direction_x = -random.randrange(15, 50)
            math_x = math_x + (direction_x + 1)
        else:
            direction_x = random.randrange(15, 50)
            math_x = math_x + (direction_x + 1)

    if math_y > monitor_y or math_y < 0:
        if(direction_y > 0):
            direction_y = -random.randrange(15, 50)
            math_y = math_y + (direction_y + 1)
        else:
            direction_y = random.randrange(15, 50)
            math_y = math_y + (direction_y + 1)

    if ret:
        cv2.imshow(imshow_name, frame)
        cv2.moveWindow(imshow_name, math_x, math_y)
        print((math_x, math_y))
    else:
       player.seek(-10)
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
       continue

    if cv2.waitKey(80) & 0xFF == ord('q'):
        threading.Thread(target=doit).start()
        continue

    try:
        cv2.getWindowProperty(imshow_name, 0)
    except:
        subprocess.Popen("cmd /c py idiot.pyw", creationflags=0x08000000)
        
cap.release()
cv2.destroyAllWindows()