import tkinter
import time
from PIL import Image, ImageTk

FNT = ("Times New Roman", 20)



class Warrior_And_Magician:
    def __init__(self, name, life, x, y, imgfile, tagname):
        self.name = name
        self.life = life
        self.lmax = life
        self.x = x
        self.y = y
        img = Image.open(imgfile).resize((240, 350))
        self.img = ImageTk.PhotoImage(img)
        self.tagname = tagname
        self.attack_mode = 'sword attack'

    def draw(self):
        x = self.x
        y = self.y
        canvas.create_image(x, y, image=self.img, tag=self.tagname)
        canvas.create_text(x, y+200, text=self.name, font=FNT, fill="red",
                           tag=self.tagname)
        canvas.create_text(x, y+230, text=self.classname, font=FNT,
                           fill="blue", tag=self.tagname)
        canvas.create_text(x, y+260, text=f"HP: {self.life}/{self.lmax}",
                           font=FNT, fill="lime", tag=self.tagname)

    def attack(self):
        dir = 1
        if self.x >= 400:
            dir = -1
        for i in range(5):  # Attack (Move)
            canvas.coords(self.tagname, self.x+i*10*dir, self.y)
            canvas.update()
            time.sleep(0.1)
        canvas.coords(self.tagname, self.x, self.y)


    def damage(self):
        for i in range(5):  # Image flash
            self.draw()
            canvas.update()
            time.sleep(0.1)
            canvas.delete(self.tagname)
            canvas.update()
            time.sleep(0.1)
        self.life = self.life - 30
        if self.life > 0:
            self.draw()
        else:
            print(self.name+"被打敗了...")

class Warrior(Warrior_And_Magician):
    def __init__(self, name, life,x,y,imgfile,tagname):
        super().__init__(name,life,x,y,imgfile,tagname)
        self.classname = 'Warrior'
        self.attack_mode = 'sword attack'

class Magician(Warrior_And_Magician):
    def __init__(self, name, life,x,y,imgfile,tagname):
        super().__init__(name,life,x,y,imgfile,tagname)
        self.classname = 'Magician'
        self.attack_mode = 'magic attack'       


root = tkinter.Tk()
root.title("Homework 2: Game Character Inheritance")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

character0 = Warrior("Alex", 200, 200, 280, "Warrior_0.webp", "LC")
character1 = Magician("Bob", 160, 600, 280, "Magician_0.webp", "RC")
character = [character0, character1]
character[0].draw()
character[1].draw()


def click_left():
    character[0].attack()
    character[1].damage()


def click_right():
    character[1].attack()
    character[0].damage()


btn_left = tkinter.Button(text=character0.attack_mode+"→",
                          command=click_left)
btn_left.place(x=160, y=560)
btn_right = tkinter.Button(text="←"+character1.attack_mode,
                           command=click_right)
btn_right.place(x=560, y=560)

root.mainloop()


#留言板