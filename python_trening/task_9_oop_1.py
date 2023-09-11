from task_9_checks import Checks
class Input(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('search', 'start')
print(search.loc)
print(search.text)

class Button(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

brr = Button('Брр', 'Брбр')
aaa = Button('Аааа', 'Аа')
print(brr.text)
print(brr.loc)
print(aaa.text)
print(aaa.loc)

class Title(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

brr = Title('Брр', 'Брбр')
aaa = Title('Аааа', 'Аа')
print(brr.text)
print(brr.loc)
print(aaa.text)
print(aaa.loc)

class Link(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

brr = Link('Брр', 'Брбр')
aaa = Link('Аааа', 'Аа')
print(brr.text)
print(brr.loc)
print(aaa.text)
print(aaa.loc)

print(search.check_text())
print(brr.check_text())
print(aaa.check_text())
