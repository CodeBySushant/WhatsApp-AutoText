import pywhatkit as pwk
import pyautogui
import keyboard
import time

phone_number = "+9779860731062"
message = "Hii bsdk!"

# Open chat and send the first message to activate the window
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=False)

time.sleep(3)
# Press enter to send the message
pyautogui.press("enter")
time.sleep(2)

for i in range(999):
    if keyboard.is_pressed('esc'):  # Press 'esc' to stop
        print("Loop stopped by user!")
        break

    pyautogui.typewrite(f"{message} {i + 2}")
    pyautogui.press("enter")
    time.sleep(0.2)

print("Done or stopped!")
