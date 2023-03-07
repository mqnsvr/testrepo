class A:
    def __init__(self, attr1):
        self.attr1 = attr1

class B(A):
    def b_method(self):
        pass

class C(A):
    def c_method(self):
        pass

class D(B,C):
    def __init__(self, attr1, attr2):
        super().__init__(attr1)
        self.__attr2 = attr2

x = D("attr1", "attr2")

'''
Kommentare: 
In der Klausur gabe es ebenfalls 4 Punkte.
Diese Beispiellösung stellt nur eine Variante dar. 
Das "pass" bei B und C kann in der Klausur (Handschriftlich) auch ander
dargestellt werden. ... "pass" ist aber schnell und einfach, sollte also gentutz werden.

'''

'''
Alternative mit Default-Wert für das Attribut in A
... wobei UML die Angabe von Default-Werten zulässt, die Lösung oben also etwas
"richtiger" ist als diese. In der Klausur würde ich jedoch auch hierauf bei
gegebener Aufgabenstellung volle Punktzahl geben.

class A:
    def __init__(self, attr1 = None):
        self.attr1 = attr1

class B(A):
    def b_method(self):
        pass

class C(A):
    def c_method(self):
        pass

class D(B,C):
    def __init__(self, attr2):
        super().__init__()
        self.__attr2 = attr2

x = D("attr2")
'''
