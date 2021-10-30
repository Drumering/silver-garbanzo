import cv2 as cv
import os
from time import sleep
from windowcapture import WindowCapture
from vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# COLCOAR O NOME DA JANELA DO JOGO AQUI
wincap = WindowCapture('MuZago Season 6')

vision = Vision()


while(True):
    sleep(1)
    
    screenshot = wincap.get_screenshot()

    if vision.checkMsgOnScreen(screenshot[135:190, 210:420], 'first_message'):
        print('checagem de captcha!')
        print('lock and two enters')
        sleep(6)

        screenshot = wincap.get_screenshot()

        while not vision.checkMsgOnScreen(screenshot[323:338, 400:479], 'second_message'):
            print('enter')
            sleep(1)
            screenshot = wincap.get_screenshot()

        while vision.checkMsgOnScreen(screenshot[323:338, 400:479], 'second_message'):
            result = vision.findNumbers(screenshot[172:185, 237:261])
            to_send = ''.join(result) + 'ee'
            print(to_send, 'three numbers and two enters')
            sleep(5)
            screenshot = wincap.get_screenshot()

        print('unlock')
    else:
        print('nothing..')



    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
