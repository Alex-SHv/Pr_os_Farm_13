import tkinter as tk
import threading
import time
import os

plants = [
    {
        "id": 1,
        "name": "Помидор",
        "baseGrowTime": 6,
        "img": "Images\tomato"
    },
    {
        "id": 2,
        "name": "Огурец",
        "baseGrowTime": 5,
        "img": "Images\cucumber"            
    },
    {
        "id": 3,
        "name": "Морковь",
        "baseGrowTime": 3,
        "img": "Images\carrot" 
    },
]

class FieldCell:
    def __init__(self, root, x, y, index, barn, game):
        self.state = "empty"   
        self.plant = None
        self.fertilizer = None
        self.barn = barn
        self.game = game

        self.btn = tk.Button(root, text=f"Грядка {index+1}", bg="sienna4", fg="white",
                             command=self.on_click)
        self.btn.place(x=x, y=y, width=160, height=50)

        self.label = tk.Label(root, text="Стадия: пусто", font=("Arial", 12))
        self.label.place(x=x, y=y+55, width=160, height=25)

    def on_click(self):
        if self.state == "empty":
            self.game.open_plant_select(self)

        elif self.state == "ready":
            self.collect()

    def grow_timer(self, t):
        time.sleep(t)
        self.state = "ready"
        self.btn.config(bg="green4", fg="white", text=f"{self.plant['name']} (готово)")
        self.label.config(text="Стадия: созрело")


    def collect(self):
        self.barn.add_item(self.plant["name"])

        self.state = "empty"
        self.btn.config(bg="sienna4", fg="white", text=f"Грядка {self.index+1}")
        self.label.config(text="Стадия: пусто")

        self.plant = None
        self.fertilizer = None

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ферма")
        self.root.geometry("900x600")

        self.money = 50
        self.inventory = {}   

        tk.Button(self.root, text="Открыть магазин", font=("Arial", 14)).place(x=700, y=30)

        self.money_label = tk.Label(self.root, text=f"Баланс: {self.money}₴", font=("Arial", 16))
        self.money_label.place(x=700, y=80)

        self.inv_label = tk.Label(self.root, text="Удобрения: -", font=("Arial", 14))
        self.inv_label.place(x=700, y=120)

        def open_plant_select(self, field):
            win = tk.Toplevel(self.root)
            win.title("Посадка")
            win.geometry("300x400")

            tk.Label(win, text="Выберите растение:", font=("Arial", 14)).pack(pady=10)

        self.root.mainloop()

Game()