import tkinter.ttk as ttk
import tkinter as tk
from int_sett import IntSett


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg=IntSett.bg_color)
        self.to_brute = tk.BooleanVar()
        self.interface_elements_dict = {
            "main_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 24, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Mail spammer v0.2.123.431b231"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "address_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Enter mail server, login, password"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "address_e": {
                "element":
                    tk.Entry(
                        self.root,
                        font=(IntSett.font, 20, "bold"),
                        fg=IntSett.text_color,
                        bg=IntSett.bg_color,
                        width=10
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "login_e": {
                "element":
                    tk.Entry(
                        self.root,
                        font=(IntSett.font, 20, "bold"),
                        fg=IntSett.text_color,
                        bg=IntSett.bg_color,
                        width=10
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "password_e": {
                "element":
                    tk.Entry(
                        self.root,
                        show="*",
                        font=(IntSett.font, 20, "bold"),
                        fg=IntSett.text_color,
                        bg=IntSett.bg_color,
                        width=10
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "database_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Select email database"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "database_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Select",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "entry_l":{
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Enter message"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },

            "entry_field":{
                "element":
                    tk.Text(
                        self.root,
                        font=(IntSett.font, 20),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        width=20,
                        height=6

                    ),
                "params": {
                    "pady": 10,
                    "padx": 10,
                }
            },
            "start_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Start",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "pb": {
                "element":
                    ttk.Progressbar(
                        self.root,
                        mode="determinate",
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                        "ipady": 10,
                        "ipadx": 100
                    },
            },
            "info_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                    ),
                "params":
                    {
                        "padx": 10,
                        "pady": 10,
                    }
            }
        }
