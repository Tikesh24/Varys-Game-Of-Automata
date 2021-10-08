import datetime
import time

from listener.EventListner import *
from service.FileHandler import *
from service.ImageHandler import *
from service.ScreenShotHandler import main


def get_events():
    mouse_event = start_listner()
    del mouse_event[-1]
    write_file('write_event', mouse_event)

def play_events():
    config = read_file('read_config','')
    path = 'app_data/automata'
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):

            events = read_file('read_event', filename)
            for event in events:
                time.sleep(int(config['wait_time']))

                if 'mouse' == event['device'] and 'click' == event['event']:
                    if 'Button.right' == event['button']:
                        pyautogui.click(button='right', x=event['x'], y=event['y'])
                    elif 'Button.left' == event['button']:
                        pyautogui.click(button='left', x=event['x'], y=event['y'])

                elif 'mouse' == event['device'] and 'move' == event['event']:
                    pyautogui.moveTo(event['x'], event['x'], 0.1)

                elif 'mouse' == event['device'] and 'scroll' == event['event']:
                    print("scroll" + str(event))

                elif 'keyboard' == event['device'] and 'key-press' == event['event']:
                    key = event['key'].strip("''")
                    if "Key" in key:
                        key = key[4:len(key)]
                    print(key)
                    pyautogui.press(key)

                elif 'keyboard' == event['device'] and 'key-write' == event['event']:
                    key = event['key']
                    print(key)
                    pyautogui.write(key)

                elif 'keyboard' == event['device'] and 'key-hotkey' == event['event']:
                    key = str(event['key']).split(",")
                    print(key)
                    pyautogui.hotkey(*key)

                elif 'image' == event['device'] and 'validate' == event['event']:
                    expire = int(event['duration'])
                    now = datetime.datetime.now()
                    expireduration = now + datetime.timedelta(minutes=expire)
                    while now < expireduration:
                        now = datetime.datetime.now()
                        seq = event['valid_seq']
                        # print('waiting...{0}'.format(seq))
                        # arr = read_file('read_validation', seq)
                        isValid = is_valid_image_2(seq)
                        print('Is Valid {0}'.format(isValid))
                        if isValid:
                            break
                        time.sleep(5)
                    if(now > expireduration):
                        print('exiting process')
                        return False
                    time.sleep(2)

def get_validation():
    main()
    # coordinate = get_validation_image_coordinates()
    # print(coordinate)
    # keyboard.wait('s')
    # im = get_screenshot(coordinate)
    # write_file('write_validation', im)

