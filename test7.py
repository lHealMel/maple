import cv2 as cv
from PIL import ImageGrab
from pynput import keyboard
import pytesseract
import time


def press(key):
    print('Key %s pressed' % key)


def release(key):
    print('Key %s released' % key)
    if key == keyboard.Key.esc:
        return 11


# 화면 지정 캡쳐 후 저장
isDragging = False
x1, y1, x2, y2 = -1, -1, -1, -1
blue, red = (255, 0, 0), (0, 0, 255)


# 마우스 좌표받아서 처리하는 함수
def onMouse(event, x, y, flags, param):
    global isDragging, x1, y1, img
    if event == cv.EVENT_LBUTTONDOWN:  # 왼쪽마우스버튼 눌렀을때
        isDragging = True
        x1 = x
        y1 = y
    elif event == cv.EVENT_MOUSEMOVE:  # 움직일때
        if isDragging:
            img_draw = img.copy()
            # 영역표시
            cv.rectangle(img_draw, (x1, y1), (x, y), blue, 2)
            cv.imshow('img', img_draw)
    elif event == cv.EVENT_LBUTTONUP:  # 왼쪽 마우스버튼 땟을때
        if isDragging:
            isDragging = False
            x2 = x
            y2 = y
            print('x:%d, y%d,w:%d,h:%d' % (x1, y1, x2, y2))

            img_draw = img.copy()
            # 영역표시
            cv.rectangle(img_draw, (x1, y1), (x2, y2), red, 2)
            cv.imshow('img', img_draw)
            # 우->좌 ,하 ->상으로 드래그시 수정
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            while 1:
                roi = img[y1:y2, x1:x2]
                # 파일저장
                cv.imwrite('C:/Users/mtn20/Desktop/save.jpg', roi)
                print('capture')
                tset1 = pytesseract.image_to_string(cv.imread('C:/Users/mtn20/Desktop/save.jpg'))
                tset2 = pytesseract.image_to_string(cv.imread('C:/Users/mtn20/Desktop/save.jpg'), lang='kor')
                print(tset1)
                print(tset2)
                time.sleep(1)
                if release(key) == 11:
                    break


# 스크린샷 찍고저장
img = ImageGrab.grab()
img.save('C:/Users/mtn20/Desktop/screenshot.jpg')

# 찍은 스크린샷 불러오기
img = cv.imread('C:/Users/mtn20/Desktop/screenshot.jpg', cv.IMREAD_COLOR)

cv.imshow('img', img)
cv.setMouseCallback('img', onMouse)
cv.waitKey()
with keyboard.Listener(on_press=press, on_release=release) as listener: listener.join()
cv.destroyAllWindows()
