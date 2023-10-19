import random
from tkinter import *
from tkinter import messagebox
from firebase_admin import *
from firebase_admin import db

global room_id
room_id = False
# Kurulumlar
cred = credentials.Certificate(
    {
        #Verileriniz
    }
)
initialize_app(cred, {"databaseURL": "<firebase-rtdb-urlniz>"})
ref = db.reference("tags")

window = Tk()
window.resizable(False, False)
window.title("Sohbet Odaları")


#Fonksiyonlar
class HintedEntry(Entry):
    def __init__(self, master=None, hint="", color="grey"):
        super().__init__(master)
        self.hint = hint
        self.hint_color = color
        self.default_fg = self["fg"]
        self.insert(0, self.hint)
        self["fg"] = self.hint_color

        self.bind("<FocusIn>", self.clear_hint)
        self.bind("<FocusOut>", self.reset_hint)

    def clear_hint(self, *args):
        if self["fg"] == self.hint_color:
            self.delete(0, "end")
            self["fg"] = self.default_fg

    def reset_hint(self, *args):
        if not self.get():
            self.insert(0, self.hint)
            self["fg"] = self.hint_color
def on_data_added(event):
    global msg_box
    if type(event.data) != str and event.data != None:
        for anahtar, deger in event.data.items():
            msg_box.config(state=NORMAL)
            msg_box.insert(END, f"{deger}\n")
            msg_box.config(state=DISABLED)
    else:
        msg_box.config(state=NORMAL)
        msg_box.insert(END, f"{event.data}\n")
        msg_box.config(state=DISABLED)

def mesaj_gonder():
    security = True
    splitted = msg_send_entry.get().split(" ")
    dosya_adı = os.getcwd()+ r"\karaliste-cr@ooguz.txt" 
    with open(dosya_adı, "r") as dosya:
        metin_listesi = dosya.read().splitlines()
    for i in metin_listesi:
        for a in splitted:
            if a == i:
                security = False
    if security == True:
        ref2.push(msg_user_entry.get() + ": " + msg_send_entry.get())
        msg_send_entry.delete(0, END)
    else:
        messagebox.showerror(title="NSFW Tespit Edildi", message="Mesajınızı gözden geçirin!")


def create():
    global msg_box
    global msg_user_entry
    global ref2
    global msg_send_entry
    global window2
    def check():
        global tags_data
        global room_id
        tags_data = ref.get()
        room_id = random.randint(0, 100000)
        idvar = False
        if tags_data:
            for i in tags_data:
                if room_id == i:
                    idvar = True
            if not idvar:
                return True
        else:
            return False

    if check():
        import requests
        import json

        tags_data.append(room_id)
        data = {
            "tags": tags_data,
        }

        url = f"https://<firebase-rtdb-urlniz>/.json?auth=<web-apı-anahtarınız>"

        response = requests.patch(url, data=json.dumps(data))

        if response.status_code == 200:
            window.destroy()
            window2 = Tk()
            window2.resizable(False, False)
            suc_title = Label(window2, text="Oda Kurma Başarılı", font=("Bold", 16))
            suc_title.grid(row=0, column=0, columnspan=3)
            room_id_des = Label(window2, text="Oda Kodunuz: " + str(room_id))
            room_id_des.grid(row=1, column=0, columnspan=3)
            msg_box = Text(window2, height=20, width=40, state=DISABLED)
            msg_box.grid(row=2, column=0, columnspan=3)
            msg_user_entry = HintedEntry(window2, hint="Kullanıcı Adı Girin...")
            msg_user_entry.grid(row=3, column=0)
            msg_send_entry = HintedEntry(window2, hint="Mesaj Girin...")
            msg_send_entry.grid(row=3, column=1)
            msg_send_button = Button(window2, text="Gönder", command=mesaj_gonder)
            msg_send_button.grid(row=3, column=2)
            ref2 = db.reference("messages/" + str(room_id))
            ref2.push("Sistem: Oda kuruldu!")
            ref2.listen(on_data_added)
            window2.protocol("WM_DELETE_WINDOW", cikis_yapildi)
            window2.mainloop()
        else:
            print("Failed to save data")
def cikis_yapildi():
    if msg_user_entry.get() != "Kullanıcı Adı Girin...":
        ref2.push("Sistem: " + msg_user_entry.get() + " ayrıldı.")
    else:
        ref2.push("Sistem: <Anonim> ayrıldı.")    
    window2.destroy()
    os._exit(1)
# Arayüzü Kur
title = Label(window, text="Sohbet Odaları", font=("Bold", 16))
description = Label(window, text="Oda kur, odaya katıl veya global odalara giriş yap.")
blank_1 = Label()
create_frame = Frame(window)
create_text = Label(create_frame, text="Oda Oluştur")
create_button = Button(create_frame, text="Oluştur", command=create)
blank_2 = Label(window, font=("Arial", 4))
join_frame = Frame(window)
join_text = Label(join_frame, text="Odaya Katıl")
join_entry = HintedEntry(join_frame, hint="Oda Kodunuzu Girin...")
blank_3 = Label(window, font=("Arial", 4))
button_global = Button(text="Global Odalara Katılın", width=35)

def roomjoin():
    global window2
    global msg_box
    global msg_user_entry
    global ref2
    global msg_send_entry
    def check():
        global tags_data
        global room_id
        tags_data = ref.get()
        room_id = int(join_entry.get())
        idvar = False
        if tags_data:
            for i in tags_data:
                if room_id == i:
                    idvar = True
        if idvar:
                return True
        else:
            return False
    x = check()
    if x:
        window.destroy()
        window2 = Tk()
        window2.resizable(False, False)
        suc_title = Label(window2, text="Odaya Giriş Başarılı", font=("Bold", 16))
        suc_title.grid(row=0, column=0, columnspan=3)
        room_id_des = Label(window2, text="Oda Kodunuz: " + str(room_id))
        room_id_des.grid(row=1, column=0, columnspan=3)
        msg_box = Text(window2, height=20, width=40, state=DISABLED)
        msg_box.grid(row=2, column=0, columnspan=3)
        msg_user_entry = HintedEntry(window2, hint="Kullanıcı Adı Girin...")
        msg_user_entry.grid(row=3, column=0)
        msg_send_entry = HintedEntry(window2, hint="Mesaj Girin...")
        msg_send_entry.grid(row=3, column=1)
        msg_send_button = Button(window2, text="Gönder", command=mesaj_gonder)
        msg_send_button.grid(row=3, column=2)
        ref2 = db.reference("messages/" + str(room_id))
        ref2.push("Sistem: Odaya biri katıldı!")
        ref2.listen(on_data_added)
        window2.protocol("WM_DELETE_WINDOW", cikis_yapildi)
        window2.mainloop()
    else:
        messagebox.showerror(title="Oda bulunamadı!",message="Oda silinmiş veya yok!")
join_button = Button(join_frame, text="Odaya Katıl", command=roomjoin)
# Pack İşlemleri
title.grid(row=0, column=0, columnspan=3)
description.grid(row=1, column=0, columnspan=3)
blank_1.grid(row=2, column=0, columnspan=2)
create_frame.grid(row=2, column=0)
create_button.grid(row=4, column=0)
create_text.grid(row=2, column=0)
blank_2.grid(row=2, column=1, columnspan=2)
join_frame.grid(row=2, column=2)
join_button.grid(row=4, column=2)
join_text.grid(row=2, column=2)
join_entry.grid(row=3, column=2)
blank_3.grid(row=5, column=0, columnspan=2)
button_global.grid(row=6, column=0, columnspan=3)
# Loop
window.mainloop()
