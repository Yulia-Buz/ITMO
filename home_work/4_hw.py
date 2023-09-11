# Задача 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self) -> int:
        print(self.width * self.height)

    def perimeter(self) -> int:
       print((self.width + self.height) * 2)

param = Rectangle(2, 3)
param.square()
param.perimeter()
object1 = Rectangle (3,5)
object1.square()
object1.perimeter()
object2 = Rectangle(4,8)
object2.square()
object2.perimeter()
object3 = Rectangle(6,9)
object3.square()
object3.perimeter()

# Задача 2

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self) -> int:
        print(self.a + self.b)

    def multiplication(self) -> int:
        print(self.a * self.b)

    def division(self) -> int:
        print(self.a / self.b)

    def substraction(self) -> int:
        print(self.a - self.b)

param = Math(4, 6)
param.addition()
param.multiplication()
param.division()
param.substraction()

# Задача 3

class Elements:

    type: str = 'Кнопка'
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

    def press(self):
        return('Клик по кнопке - {}'. format(self.text))

Text_box = Elements('Text_box', '')
print(Text_box.text)
print(Text_box.press())
Check_box = Elements('Check_box','')
print(Check_box.text)
print(Check_box.press())
Radio_Button = Elements('Radio_Button','')
print(Radio_Button.text)
print(Radio_Button.press())
Web_Tables = Elements('Web_Tables','')
print(Web_Tables.text)
print(Web_Tables.press())
Buttons = Elements('Buttons','')
print(Buttons.text)
print(Buttons.press())
Links = Elements('Links','')
print(Links.text)
print(Links.press())
Broken_links_Images = Elements('Broken_links_Images','')
print(Broken_links_Images.text)
print(Broken_links_Images.press())
Upload_Download = Elements('Upload_Download','')
print(Upload_Download.text)
print(Upload_Download.press())
Dynamic_properties = Elements('Dynamic_properties','')
print(Dynamic_properties.text)
print(Dynamic_properties.press())

