# ConvertCase Application
#Introduce your text and obtained the text with Upper case, lower case, capitalized casa and alternating case.

from random import randint

class Convert:
    def __init__(self):
        pass

    def menu(self):
        self.text=input('Insert the text to convert: ')

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

    def alternating(self):
        n=randint(1,len(self.text))
        random_l=[]
        for i in range(0,n):
            aux=randint(1,len(self.text))
            random_l.append(aux)
        print(random_l)

        for i in range(0, len(self.text)):  # find . and put the first letter after in upper case

            if i == random_l.index(i):
                # put upper case
                print(self.text[i].upper(), end="")
            else:
                print(self.text[i].lower(), end="")



c=Convert()

c.menu()

c.capitalize()
c.alternating()
