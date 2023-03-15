from pyautogui import hotkey
from time import sleep
from keyboard import is_pressed
helplist = ['\\t', '\\n', '\\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
cont1, cont2, cont3, cont4 = -1, -1, -1, -1
key_dict = {}

def dict_sorter(splitted_starter, splitted_trigger):
    keystroke = str(splitted_starter).replace("[", "").replace("]", "")

    triger = str(splitted_trigger).replace("[", "").replace("]", "")
    key_dict[keystroke] = triger

def stroke():
    global splitted_starter
    global cont1
    starter = input("Please type key combination you want to simulate in format of CTRL,V or CTRL V. \nYou can use /help to show keynames : ")
    starter = starter.lower()

    if starter == "/help":
        for i in range(0, len(helplist), 10):
            print(helplist[i:i + 10])
        print("\n")
        return -1
    else:
        if " " in starter:
            starter = starter.replace(" ",",")
        splitted_starter = starter.split(",")

    for i in splitted_starter:
        if i not in helplist:
            print(str(i), " is not available. Please select keystroke from known keys")
            print("\n")
            return -1

    if str(splitted_starter).replace("[","").replace("]","") in key_dict:
        print("\n"+"You can't use same keystroke combination for trigger and simulation")
        print("\n")
        return -1

    print("You have selected", splitted_starter, "as keystroke combination")
    return 1


def sim():
    global splitted_trigger
    global cont2
    print("\n")
    trigger = input("Please type key combination you want to trigger the keystroke. \nYou can use /help to show keynames : ")
    trigger = trigger.lower()

    if trigger == "/help":
        for i in range(0, len(helplist), 10):
            print(helplist[i:i+10])
        print("\n")
        return -1
    else:
        if " " in trigger:
            trigger = trigger.replace(" ", ",")
        splitted_trigger = trigger.split(",")

    for i in splitted_trigger:
        if i not in helplist:
            print(str(i), " is not available. Please select keystroke from known keys")
            print("\n")
            return -1


    print("You have selected", splitted_trigger, "as keystroke trigger combination")
    return 1


def again():
    global cont3
    global cont4
    again = input("Do you want to simulate another keystroke? Y/N : ")
    if again == "Y" or again == "y":
        return 1
    elif again == "N" or again == "n":
        cont3 = 1
        cont4 = 1
    else:
        print("Please select Y or N")
        return -1
    return

def start():
    pass

while cont4 == -1:
    cont1, cont2, cont3, cont4 = -1, -1, -1, -1

    while cont1 == -1:
        cont1 = stroke()
    while cont2 == -1:
        cont2 = sim()
    dict_sorter(splitted_starter, splitted_trigger)
    while cont3 == -1:
        cont3 = again()

while True:
    for combo in key_dict:
        combo_ans = key_dict[combo].replace("'", "").replace(" ", "")
        combo = combo.replace("'", "").replace(" ", "")

        if combo.count(",") == 0:
            if is_pressed(combo):
                if combo_ans.count(",") == 0:
                    hotkey(combo_ans)
                elif combo_ans.count(",") == 1:
                    hotfirst, hotsecond = combo_ans.split(",")
                    hotkey(hotfirst, hotsecond)
                elif combo_ans.count(",") == 2:
                    hotfirst, hotsecond, hotthird = combo_ans.split(",")
                    hotkey(hotfirst, hotsecond, hotthird)
            sleep(0.01)

        elif combo.count(",") == 1:
            first, second = combo.split(",")
            print(first, second)
            if is_pressed(first) and is_pressed(second):
                if combo_ans.count(",") == 0:
                    hotkey(combo_ans)
                elif combo_ans.count(",") == 1:
                    hotfirst, hotsecond = combo_ans.split(",")
                    hotkey(hotfirst, hotsecond)
                elif combo_ans.count(",") == 2:
                    hotfirst, hotsecond, hotthird = combo_ans.split(",")
                    hotkey(hotfirst, hotsecond, hotthird)
            sleep(0.01)

        elif combo.count(",") == 2:
            first, second, third = combo.split(",")
            if is_pressed(first) and is_pressed(second) and is_pressed(third):
                if combo_ans.count(",") == 0:
                    hotkey(combo_ans)
                elif combo_ans.count(",") == 1:
                    hotfirst, hotsecond = combo_ans.split(",")
                    hotkey(hotfirst, hotsecond)
                elif combo_ans.count(",") == 2:
                    hotfirst, hotsecond, hotthird = combo_ans.split(",")
                    hotkey(hotfirst, hotsecond, hotthird)
            sleep(0.01)




