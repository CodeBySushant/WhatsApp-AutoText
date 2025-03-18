import pywhatkit as pwk

phone_number = "+918271278494"
message = "Hello World!"

# This will open WhatsApp Web and wait for 30 seconds before sending
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=30, tab_close=True, close_time=3)
