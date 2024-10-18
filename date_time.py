import datetime
import pyttsx3

def say(text):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    return Time

def get_date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    date = day+"/"+month+"/"+year
    return date

def wishing():
    h=datetime.datetime.now().hour
    if h>=0 and h<12:
        wish="Good Morning Sir!"
    elif h>=12 and h<15:
        wish="Good Afternoon Sir!"
    elif h>=15 and h<19:
        wish="Good Evening Sir!"
    else:
        wish="Good Night Sir!"
    return wish 

if __name__ == "__main__":
    say(wishing())
    say("how can i help you 010")
    print("the time is :",get_time())
    print("The date is :",get_date())

