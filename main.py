# ConvertCase Application
#Introduce your text and obtained the text with Upper case, lower case, capitalized casa and alternating case.

from PySimpleGUI import PySimpleGUI as sg
from random import randint

class Convert:
    def __init__(self):
        sg.theme('Reddit')

        #layout
        self.layout = [
            [sg.Text('Text to convert:'), sg.Input(key='text')],  # line1
            [sg.Button('Upper Case'), sg.Button('Lower Case'), sg.Button('Capitalized Case'), sg.Button('Alternating Case')],
            [sg.Output(key='result')],  # line 3
        ]
    
    def start(self):

        # create a window in GUI
        self.w1 = sg.Window('Convert Case').layout(self.layout)

        while True:

            # obtain data
            self.event, value = self.w1.read()
            self.text=value.get('text')

            # window closed
            if self.event == sg.WINDOW_CLOSED:            
                break
            
            # cases
            if self.event == 'Upper Case':
                c.uppercase()

            if self.event == 'Lower Case':
                c.lowercase()

            if self.event == 'Capitalized Case':
                c.capitalize()

            if self.event == 'Alternating Case':
                c.alternating()


    def uppercase(self):
        self.upp=self.text.upper()
        print(self.upp)

    def lowercase(self):
        self.low=self.text.lower()
        print(self.low)

    def capitalize(self):
        for i in range(0,len(self.text)): #find . and put the first letter after in upper case

            if i==0:
                print(self.text[i].upper(),end="")
            else:
                if self.text[i-1]=='.' or (self.text[i-2]=='.' and self.text[i-1]==' ' ):
                    #put upper case
                    print(self.text[i].upper(),end="")
                else:
                    print(self.text[i].lower(),end="")
        print()

    def alternating(self):
        n=randint(1,len(self.text))
        random_l=[]
        for i in range(0,n):
            aux=randint(1,len(self.text))
            random_l.append(aux)

        for i in range(0, len(self.text)):  # randow upper case

            if i in random_l:
                # put upper case
                print(self.text[i].upper(), end="")
            else:
                print(self.text[i].lower(), end="")

c=Convert()
c.start()
