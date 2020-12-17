from tkinter import filedialog as fd
import tkinter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
from interface_elements import Interface


class Program:
    def __init__(self):
        self.i = Interface()
        self.path = ""
        self.elements = self.i.interface_elements_dict
        self.to_brute = self.i.to_brute

        self.ADDRESS_ENTRY = self.elements["address_e"]["element"]
        self.LOGIN_ENTRY = self.elements["login_e"]["element"]
        self.PASSWORD_ENTRY = self.elements["password_e"]["element"]
        self.MESSAGE_FIELD = self.elements["entry_field"]["element"]
        self.INFORMATION_LABEL = self.elements["info_l"]["element"]

    def pack_elements(self):
        for key in self.elements.keys():
            elem = self.elements[key]["element"]
            params = self.elements[key]["params"]
            elem.pack(**params)
            if "list" in key:
                list_params = self.elements[key]["list_params"]
                list_items = self.elements[key]["list_items"]
                for list_item in list_items:
                    elem.insert(0, list_item)
                elem.select_set(0)
                elem.configure(**list_params)

    def openfile(self, event):
        self.path = fd.askopenfilename()

    def attack(self):
        server_address = self.ADDRESS_ENTRY.get()
        login = self.LOGIN_ENTRY.get()
        password = self.PASSWORD_ENTRY.get()
        message = self.MESSAGE_FIELD.get("1.0", tkinter.END)
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'plain'))
        if server_address == "" and login == "" and password == "":
            self.INFORMATION_LABEL["text"] = f"Enter all values!"
        else:
            if self.path == "":
                self.INFORMATION_LABEL["text"] = f"Select file!"
            else:
                with open(self.path, "r",  encoding="utf-8") as f:
                    email_list = f.read().split("\n")
                    server = smtplib.SMTP(server_address)
                    server.starttls()
                    server.login(login, password)
                    for email in email_list:
                        server.sendmail(login, email, msg.as_string())
                        self.INFORMATION_LABEL["text"] = f"Message to {email}\n sent!"
                    server.quit()
                    self.INFORMATION_LABEL["text"] = f"Done!"

    def start(self, event):
        threading.Thread(target=self.attack).start()

    def mainloop(self):
        self.pack_elements()
        self.elements["database_b"]["element"].bind("<Button-1>", self.openfile)
        self.elements["start_b"]["element"].bind("<Button-1>", self.start)
        self.i.root.mainloop()
