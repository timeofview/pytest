from tkinter import *


master = Tk()
master.geometry("300x300")
master.title("Graph Plotter")


def open_new_window(default_title="Default Title"):
    new_window = Toplevel(master)
    new_window.title(default_title)
    new_window.geometry("200x200")
    Label(new_window).pack()

#parallelo?
def open_client_setter_window():
    new_window = Toplevel(master)
    new_window.title("Client Setter")
    new_window.geometry("300x400")
    ipLabel = Label(new_window, text="Ip:").pack(pady=5)
    ip = Entry(new_window).pack(pady=5)
    #ip.grid(row=0, column=1)
    portLabel = Label(new_window, text="Port:").pack(pady=5)
    port = Entry(new_window).pack(pady=5)
    #port.grid(row=1, column=1)
    text_file_number = Label(new_window, text="Files.txt number: ").pack(pady=5)
    num_file = Entry(new_window).pack(pady=5)
    char_per_text_file_number = Label(new_window, text="Chars per .txt number: ").pack(pady=5)
    char_num_file = Entry(new_window).pack(pady=5)
    is_on = IntVar()
    radio_buttons = Label(new_window, text="Multithread: ").pack(pady=5)
    Radiobutton(new_window, text="On", variable=is_on, value=1).pack(pady=5)
    Radiobutton(new_window, text="Off", variable=is_on, value=0).pack(pady=5)
    Button(new_window, text="Confirm", command=print_my_data).pack(pady=10)


def open_server_setter_window():
    new_window = Toplevel(master)
    new_window.title("Server Setter")
    new_window.geometry("200x200")
    ipLabel = Label(new_window, text="Ip:").pack(pady=10)
    ip = Entry(new_window).pack(pady=10)
    #ip.grid(row=0, column=1)
    portLabel = Label(new_window, text="Port:").pack(pady=10)
    port = Entry(new_window).pack(pady=10)
    #port.grid(row=1, column=1)
    Button(new_window, text="Confirm", command=print_my_data).pack(pady=10)


def print_my_data():
    print("hey")


def elaborate():
    #File txt
    print("ciao")


if __name__ == '__main__':
    serverLabel = Label(master, text="Click this bottom to set-up Server")
    serverLabel.pack(pady=10)
    serverButton = Button(master, text="Server", command=open_server_setter_window)
    serverButton.pack(pady=10)
    clientLabel = Label(master, text="Click this bottom to set-up Client")
    clientLabel.pack(pady=10)
    clientButton = Button(master, text="Client", command=open_client_setter_window)
    clientButton.pack(pady=10)
    okLabel = Label(master, text="Click this button to Graph")
    okLabel.pack(pady=10)
    okButton = Button(master, text="Confirm", command=elaborate)
    okButton.pack(pady=10)
    master.mainloop()
