import pywhatkit as pwk
import pyautogui
import time

phone_number = "+918271278494"
message = "Hello World!"

# Send message instantly with a short wait time
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=20, tab_close=True)

# Wait a few seconds to make sure the message is typed
time.sleep(5)

# Press Enter to send it
pyautogui.press("enter")

print("Message sent successfully!")
