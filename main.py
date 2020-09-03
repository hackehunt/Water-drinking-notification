import time
from plyer import notification
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.spvoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Please drink water sir, it's good for your health")
    notification.notify(
        title="Please Drink Water",
        message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        app_icon = '''icon.ico''',
        timeout = 20
    )
    time.sleep(6)

