# ===================================================
#                                                   #
#      ____         __                  __ _        #
#     / ___|  __ _ / _| __ _ ___  ___  / _| |_      #
#     \___ \ / _` | |_ / _` / __|/ _ \| |_| __|     #
#      ___) | (_| |  _| (_| \__ \ (_) |  _| |_      #
#     |____/ \__,_|_|  \__,_|___/\___/|_|  \__|     #
#                                                   #
#               Copyright is reserved               #
#          This code is for personal use only.      #
#          Thanks.                                  #
# ===================================================


# ============================ Importing ============================
from tkinter import Tk, Label, Button, Entry as Textbox, Text, Frame, LabelFrame, Listbox, Toplevel, StringVar
from tkinter.ttk import Button as Button_ttk
from tkinter.messagebox import showerror, showinfo

# ============================ Settings ============================

MainWindow = Tk("Text Formatting")
MainWindow.title("Text Formatting")
MainWindow.geometry("1000x600")
MainWindow.resizable(False, False)

About = {
    'Company': 'Safasoft',
    'Appname': 'Text Formatting',
    'Version': 1.0
}

Settings = {
    "Font": "Tahoma",
    "Font_size": 10,
    "rightside_bg": "#E0E0E0"
}

Variables = {}

selected_variable = ""


# ============================ Functions ============================

def add_to_variables(name, value):
    if not name in Variables:
        Variables[f'{name}'] = value
        Variables_list.insert('end', f"{name} = {value}")
    else:
        return "invalid_name_error"


def delete_from_variables(key):
    value = Variables[key]
    index = selected_variable[0]

    Variables.pop(key)
    Variables_list.delete(index)


def edit_the_variable(key, newvalue):
    Variables[f'{key}'] = newvalue
    index_item_edited = selected_variable[0]

    Variables_list.delete(index_item_edited)

    Variables_list.insert(index_item_edited, f"{key} = {newvalue}")


def get_selecteditem_variableL(event):
    index = Variables_list.curselection()[0]
    value = Variables_list.get(index)
    result = (index, value)

    global selected_variable
    selected_variable = result


def add_variable():
    name = Add_Variable_name_textbox.get()
    value = Add_Variable_value_textbox.get()

    if add_to_variables(name, value) == "invalid_name_error":
        showerror("Error", "Invalid Variable Name!")

    Add_Variable_name_textbox.delete(0, 'end')
    Add_Variable_value_textbox.delete(0, 'end')

    print(f"Variables = {Variables}")  # Debug


def delete_variable():
    valueLS = selected_variable[1]
    valueLS = valueLS.replace(" ", "")

    key = valueLS.split("=")[0]
    # value = valueLS.split("=")[1]

    delete_from_variables(key)


def edit_variable():
    def Edit():
        edit_the_variable(key, Value.get())
        EditWindow.destroy()

    valueLS = selected_variable[1]
    valueLS = valueLS.replace(" ", "")

    key = valueLS.split("=")[0]
    value = valueLS.split("=")[1]

    Name = StringVar()
    Value = StringVar()

    Name.set(key)
    Value.set(value)

    EditWindow = Toplevel(MainWindow)
    EditWindow.geometry("250x100")
    EditWindow.title("Edit Variable")
    EditWindow.resizable(False, False)

    Label(EditWindow, text="Name Variable:").grid(row=1, column=1)
    Name_texbox = Textbox(EditWindow, state="disable", textvariable=Name)
    Name_texbox.grid(row=1, column=2)

    Label(EditWindow, text="New Value Variable:").grid(row=2, column=1)
    Value_texbox = Textbox(EditWindow, textvariable=Value)
    Value_texbox.grid(row=2, column=2)

    Button(EditWindow, text="Edit", width=20, command=Edit).grid(row=3, column=1, columnspan=12)

    EditWindow.mainloop()


def export():
    user_text = User_Text.get(1.0, "end")
    generatded_text = user_text

    for key_VN in Variables:
        t_format = "{" + key_VN + "}"
        generatded_text = generatded_text.replace(t_format, Variables[key_VN])

    File_Result = open("result.txt", "w", encoding="utf-8")
    File_Result.write(generatded_text)
    File_Result.close()

    showinfo("Complete", "Text generation done.")


# ============================ Frames ============================
# Right_Side_frame = Frame(MainWindow)
# Right_Side_frame.pack(side="right", fill="y")

rightside_color = Settings["rightside_bg"]

Left_Side_frame = Frame(MainWindow)
Left_Side_frame.pack(side="left", fill="y")

Variable_frame = LabelFrame(MainWindow, text="Variables", bg=rightside_color)
Variable_frame.pack(fill="x")

Add_Variable_frame = LabelFrame(Variable_frame, text="Add Variable", bg=rightside_color)
Add_Variable_frame.pack(fill="x")
# ============================ Widgets ============================
font = Settings["Font"]
font_size = Settings["Font_size"]

User_Text = Text(Left_Side_frame, font=(font, font_size), height=37, width=100)
User_Text.pack()

# # # # # # # # # # # # # add variable # # # # # # # # # # # # #
Label(Add_Variable_frame, text="Name:", bg=rightside_color).place(x="0", y="0")

Add_Variable_name_textbox = Textbox(Add_Variable_frame, width=30)
Add_Variable_name_textbox.pack()

Label(Add_Variable_frame, text="Value:", bg=rightside_color).place(x="0", y="20")

Add_Variable_value_textbox = Textbox(Add_Variable_frame, width=30)
Add_Variable_value_textbox.pack()

btn_add = Button(Add_Variable_frame, text="Add", width=20, height=2, command=add_variable)
btn_add.pack()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

btn_delete = Button(Variable_frame, text="Delete", width=15, command=delete_variable)
btn_delete.pack()

btn_edit = Button(Variable_frame, text="Edit", width=15, command=edit_variable)
btn_edit.pack()

Variables_list = Listbox(Variable_frame, width=40, height=23)
Variables_list.pack()
Variables_list.bind("<<ListboxSelect>>", get_selecteditem_variableL)

Export_Button = Button_ttk(Variable_frame, text="Export", width=30, command=export)
Export_Button.pack()

Label(Variable_frame, text="Safasoft (C)", fg="green", bg=rightside_color).pack()

# ============================ Run ============================

if __name__ == '__main__':
    MainWindow.mainloop()
