import speech_recognition as sr
import os
import shutil

def voice():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("say anything " )
        audio = r.listen(source)

    try:
        get = r.recognize_google(audio)
        #print(get)
    except UnknownValueError :
        print("error")

    g = get
    print(g)
    for root , dir , files in os.walk(r'C:\Users\ZAHRA\Desktop\067-XY-Plotter-Drawing-Robot\.SVG IMAGES'):
        for file in files:
            if file.startswith(g):
                source=(os.path.join(root,file))
                print(source)

    emp=os.listdir(r'C:\Users\ZAHRA\Desktop\067-XY-Plotter-Drawing-Robot\GCTRL\talha')
    destination = r'C:\Users\ZAHRA\Desktop\067-XY-Plotter-Drawing-Robot\GCTRL\talha'
    #print (renaming)
    print(emp)
    if len(emp)==0:
       shutil.copy(source,destination)
    else:
        shutil.rmtree('talha')
        os.makedirs('talha')
        dest=shutil.copy(source,destination)
       #os.rename(r'C:\Users\ZAHRA\Desktop\067-XY-Plotter-Drawing-Robot\GCTRL\talha\OLD file name.file type',r'file path\NEW file name.file type')
    print("proceed to processing")

voice()
