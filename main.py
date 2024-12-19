from tkinter import *
FONT_S = ("Mono", 16, "bold")
FONT_B = ("Mono", 23)
FONT_U = ("Mono", 16)
BG_COLOR = "#D7C0AE"
TEXT_COLOR = "#4F709C"
TITLE_COLOR = "#213555"

water_percentage = {
    "water": 1,
    "milk": 0.87,
    "creme": 0.65,
    "honey": 0.2,
    "c_milk": 0.35,
    "egg": 0.75
}


# ----------------------- convert ------------------------------------#
def convert(liquid):
    flower = flower_et.get()
    hydration = hydration_et.get()
    total = round(int(flower)*int(hydration)/100, 2)

    already_have = {
        "water": int(water_et.get()),
        "milk": int(milk_et.get()),
        "creme": int(creme_et.get()),
        "egg": int(egg_et.get()),
        "honey": int(honey_et.get()),
        "c_milk": int(c_milk_et.get())
     }

    total_now = 0
    for n in already_have:
        total_now += round(already_have[n] * water_percentage[n], 2)

    answer = round((total-total_now)/water_percentage[liquid], 2)
    answer_lb.config(text=f"You need {answer}g {liquid}.", font=FONT_B, fg=TITLE_COLOR)


# -----------------------RESET---------------------------------------#
def reset():
    all_enter = (flower_et, hydration_et, water_et, milk_et, creme_et, egg_et, honey_et, c_milk_et)
    for n in all_enter:
        n.delete(0, END)
    answer_lb.config(text="")


# -----------------------UI SETUP------------------------------------- #
window = Tk()
window.title("Liquid Convert")
window.config(pady=50, padx=50, bg=BG_COLOR)

flower_lb = Label(text="Flower :", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT_S)
flower_lb.grid(column=0, row=0, sticky=E)
flower_et = Entry(width=5, highlightthickness=0)
flower_et.focus()
flower_et.grid(column=1, row=0, sticky=E)
f_unit = Label(text="g", font=FONT_U, bg=BG_COLOR)
f_unit.grid(column=2, row=0, sticky=W)

hydration_lb = Label(text="Hydration :", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_S)
hydration_lb.grid(column=0, row=1, sticky=E)
hydration_et = Entry(width=5, highlightthickness=0)
hydration_et.grid(column=1, row=1, sticky=E)
hydration_unit = Label(text="%", font=FONT_U, bg=BG_COLOR)
hydration_unit.grid(column=2, row=1, sticky=W)

intro = Label(text="You already have : ", font=FONT_B, pady=10, fg=TITLE_COLOR, bg=BG_COLOR)
intro.grid(column=0, row=2, columnspan=4, sticky=W)

water_lb = Label(text="Water :", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT_S)
water_lb.grid(column=0, row=3, sticky=E)
water_et = Entry(width=5, highlightthickness=0)
water_et.grid(column=1, row=3, sticky=E)
water_unit = Label(text="g     ", font=FONT_U, bg=BG_COLOR)
water_unit.grid(column=2, row=3, sticky=W)

milk_lb = Label(text="Milk :", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT_S)
milk_lb.grid(column=3, row=3, sticky=E)
milk_et = Entry(width=5, highlightthickness=0)
milk_et.grid(column=4, row=3, sticky=E)
milk_unit = Label(text="g     ", font=FONT_U, bg=BG_COLOR)
milk_unit.grid(column=5, row=3, sticky=W)

creme_lb = Label(text="Creme :", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT_S)
creme_lb.grid(column=6, row=3, sticky=E)
creme_et = Entry(width=5, highlightthickness=0)
creme_et.grid(column=7, row=3, sticky=E)
creme_unit = Label(text="g     ", font=FONT_U, bg=BG_COLOR)
creme_unit.grid(column=8, row=3, sticky=W)

egg_lb = Label(text="Egg :", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT_S)
egg_lb.grid(column=9, row=3, sticky=E)
egg_et = Entry(width=5, highlightthickness=0)
egg_et.grid(column=10, row=3, sticky=E)
egg_unit = Label(text="g     ", font=FONT_U, bg=BG_COLOR)
egg_unit.grid(column=11, row=3, sticky=W)

honey_lb = Label(text="Honey :", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT_S)
honey_lb.grid(column=12, row=3, sticky=E)
honey_et = Entry(width=5, highlightthickness=0)
honey_et.grid(column=13, row=3, sticky=E)
honey_unit = Label(text="g     ", font=FONT_U, bg=BG_COLOR)
honey_unit.grid(column=14, row=3, sticky=W)

c_milk_lb = Label(text="Condensed Milk :", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT_S)
c_milk_lb.grid(column=15, row=3, sticky=E)
c_milk_et = Entry(width=5, highlightthickness=0)
c_milk_et.grid(column=16, row=3, sticky=E)
c_milk_unit = Label(text="g     ", font=FONT_U, bg=BG_COLOR)
c_milk_unit.grid(column=17, row=3, sticky=W)

cue = Label(text="Which one do you want to add more?", font=FONT_B, pady=10, fg=TITLE_COLOR, bg=BG_COLOR)
cue.grid(column=0, row=4, columnspan=5, sticky=W)

water_bt = Button(text="Water", width=10, highlightthickness=0, highlightbackground=BG_COLOR,
                  command=lambda: convert(liquid="water"))
water_bt.grid(column=0, row=5, columnspan=2, sticky=E)

milk_bt = Button(text="Milk", width=10, highlightthickness=0, highlightbackground=BG_COLOR,
                 command=lambda: convert(liquid="milk"))
milk_bt.grid(column=2, row=5, columnspan=2, sticky=W)

creme_bt = Button(text="Creme", width=10, highlightthickness=0, highlightbackground=BG_COLOR,
                  command=lambda: convert(liquid="creme"))
creme_bt.grid(column=4, row=5, columnspan=2, sticky=W)

egg_bt = Button(text="Egg", width=10, highlightthickness=0, highlightbackground=BG_COLOR,
                command=lambda: convert(liquid="egg"))
egg_bt.grid(column=6, row=5, columnspan=2, sticky=W)

honey_bt = Button(text="Honey", width=10, highlightthickness=0, highlightbackground=BG_COLOR,
                  command=lambda: convert(liquid="honey"))
honey_bt.grid(column=8, row=5, columnspan=2, sticky=W)

c_milk_bt = Button(text="Condensed milk", width=10, highlightthickness=0, highlightbackground=BG_COLOR,
                   command=lambda: convert(liquid="c_milk"))
c_milk_bt.grid(column=10, row=5, columnspan=2, sticky=W)

answer_lb = Label(bg=BG_COLOR, fg=TITLE_COLOR, highlightthickness=0)
answer_lb.grid(column=0, row=6, columnspan=8, padx=10, pady=30, sticky=W)

reset_bt = Button(text="RESET", width=12, height=2, highlightthickness=0, highlightbackground=BG_COLOR, command=reset)
reset_bt.grid(column=0, row=7, columnspan=3, sticky=W)

window.mainloop()

