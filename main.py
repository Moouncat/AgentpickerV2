from tkinter import *
import random
import mouse
import keyboard
from time import sleep

win = Tk()

win_width = 500
win_height = 200
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width / 2) - (win_width / 2)
y = (screen_height / 2) - (win_height / 2)
win.geometry(f"{win_width}x{win_height}+{int(x)}+{int(y)}")

win.title("AgentpickerV2")
win.iconbitmap('icon.ico')
win.minsize(500, 200)
win.maxsize(500, 200)


def new_hotkey():
    global enter_hotkey, hotkey_win
    hotkey_win = Toplevel(win)
    hotkey_win.iconbitmap('icon.ico')

    hotkey_win_width = 200
    hotkey_win_height = 100
    hotkey_x = (screen_width / 2) - (hotkey_win_width / 2)
    hotkey_y = (screen_height / 2) - (hotkey_win_height / 2)
    hotkey_win.geometry(f"{hotkey_win_width}x{hotkey_win_height}+{int(hotkey_x)}+{int(hotkey_y)}")

    hotkey_win.config(bg="#0C1824")
    hotkey_win.minsize(200, 100)
    hotkey_win.maxsize(200, 100)

    enter_hotkey = Entry(hotkey_win, width=27, relief=GROOVE, bg="#FF5152")
    enter_hotkey.place(relx=0.1, rely=0.35)

    hotkey_label = Label(hotkey_win, text="Enter your new hotkey", bg="#0C1824", fg="white", font=("Candara Light", 12))
    hotkey_label.place(relx=0.125, rely=0.07)

    submit = Button(hotkey_win, text="submit", bg="#FF5152", fg="#0C1824", command=change_hotkey, textvariable=hotkey)
    submit.place(relx=0.39, rely=0.65)


def pick_agent():
    if mode == 0:
        random_number = random.randint(0, len(agents) - 1)
        print(f"You got {agents[random_number]} as Agent")
        print(f"Click x at {replication_cords[random_number][0]} and y at {replication_cords[random_number][1]}")
        mouse.move(replication_cords[random_number][0], replication_cords[random_number][1])
        sleep(0.2)
        mouse.click()
        sleep(0.2)
        mouse.move(956, 810)
        sleep(0.2)
        mouse.click()
    if mode == 1:
        random_number = random.randint(0, len(agents) - 1)
        print(f"You got {agents[random_number]} as Agent")
        print(f"Click x at {agent_cords[random_number][0]} and y at {agent_cords[random_number][1]}")
        mouse.move(agent_cords[random_number][0], agent_cords[random_number][1])
        sleep(0.2)
        mouse.click()
        sleep(0.2)
        mouse.move(956, 810)
        sleep(0.2)
        mouse.click()


def change_hotkey():
    global enter_hotkey, hotkey_win
    hotkey = enter_hotkey.get()
    if hotkey != "":
        keyboard.add_hotkey(hotkey, pick_agent)
        canvas.itemconfig(status_text, text=f"Press {hotkey} to roll a random agent")
        hotkey_win.destroy()
    else:
        enter_hotkey.config(bg="yellow")


def change_replication():
    global mode
    mode = 0


def change_normal():
    global mode
    mode = 1


mode = 1

hotkey = "alt+a"
keyboard.add_hotkey(hotkey, pick_agent)

bg = PhotoImage(file="BG.png")
canvas = Canvas(win, width=500, height=200, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.create_text(250, 40, text="AgentpickerV2", font=("Fiesta", 22), fill="white")
status_text = canvas.create_text(250, 75, text=f"Press {hotkey} to roll a random agent",
                                 font=("Candara Light", 12), fill="white")

agents = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Jett', 'KAY/O', 'Killjoy',
          'Neon', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']

agent_cords = [[625, 923], [710, 923], [795, 921], [870, 927], [955, 923], [1043, 921],
               [1125, 920], [1213, 922], [1295, 924], [622, 1006], [706, 1004], [788, 1003],
               [872, 1004], [961, 1007], [1046, 1007], [1124, 1007], [1206, 1003], [1294, 1006]]

replication_cords = [[667, 836], [752, 838], [833, 837], [915, 837], [1001, 835], [1089, 836],
                     [1169, 835], [1249, 836], [665, 924], [749, 918], [833, 920], [915, 922],
                     [1002, 921], [1090, 923], [1172, 922], [1253, 922], [668, 1003], [749, 1007]]

info_text = Label(win, bg="#0C1824", fg="white", anchor=CENTER)
info_text.place(relx=0.5, rely=0.85, anchor=CENTER)

change_button = Button(win, text="Change hotkey", command=new_hotkey, bg="#FF5152", fg="#0C1824", height=2, width=12)
change_button.place(relx=0.1, rely=0.55)

agent_view = Button(win, text="Normal", height=2, bg="#FF5152", fg="#0C1824",
                    width=12, command=change_normal)
agent_view.place(relx=0.4, rely=0.55)
replication_view = Button(win, text="Replication", height=2, bg="#FF5152", fg="#0C1824",
                          width=12, command=change_replication)
replication_view.place(relx=0.7, rely=0.55)

win.mainloop()
