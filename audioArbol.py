import speech_recognition as sr
import turtle

t = turtle.Turtle()
r = sr.Recognizer()

def arbol(i):
    if i < 10:
        print("")
    else:
        t.fd(i)
        t.left(30)
        tree(3 * i / 4)
        t.right(60)
        tree(3 * i / 4)
        t.left(30)
        t.backward(i)

with sr.Microphone() as source:
    print("Te escuchamos: ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        print("Lo que buscas fue: {}".format(text))

        if (text == "arbol" or text == "árbol"):
            t.left(90)
            arbol(100)

    except:
        print("Algo salio mal")
