#! /bin/env python3


from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import colorchooser
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

master = Tk()
master.geometry("800x277")
master.title("Graph Plotter")
colorUsed = "#fff"


def read_me(txt="data.txt"):
    if os.path.exists("./"+txt):
        f = open(txt,"r")
        lines=f.readlines()
        f.close()
        return lines
    else:
        f = open(txt,"w")
        f.close()
        return ""


def write_me(version,name,path,args,threads,stdin,timestamp,graphs,txt="data.txt"):
    if os.path.exists("./"+txt):
        f = open(txt,"a")
    else:
        f = open(txt,"w")
    if version.isalpha() or name.isnumeric():
        print("Error in parameter")
    f.write(version + ";" + name + ";" + path + ";" + args + ";" + threads + ";" + stdin + ";" +
            timestamp + ";" + graphs + "\n")
    f.close()


def choose_color(color_name):
    color_code = colorchooser.askcolor(title ="Choose color") 
    colorUsed = color_code
    color_name.configure(text=str(colorUsed[1]))


def add_group():
    window = open_new_window("Add a Group")
    top = Frame(window)
    top.pack(side=TOP, fill=BOTH, expand=True)
    bot = Frame(window)
    bot.pack(side=BOTTOM, fill=BOTH, expand=True)
    left = Frame(top)
    left.pack(side=LEFT, fill=BOTH, expand=True)
    right = Frame(top)
    right.pack(side=RIGHT, fill=BOTH, expand=True)
    version = Entry(right)
    version.pack(pady=5)
    group_id = Entry(right)
    group_id.pack(pady=5)
    name = Entry(right)
    name.pack(pady=5)
    args = Entry(right)
    args.pack(pady=5)
    threads = Entry(right)
    threads.pack(pady=5)
    temple = Entry(right)
    temple.pack(pady=5)
    average = Entry(right)
    average.pack(pady=5)
    color_name = Label(right, text=colorUsed)
    color_name.pack(pady=5)
    version_label = Label(left, text="Version:").pack(pady=5)
    group_id_label = Label(left, text="GroupId:").pack(pady=6)
    name_label = Label(left, text="Name:").pack(pady=6)
    args_label = Label(left, text="Args:").pack(pady=6)
    threads_label = Label(left, text="Threads:").pack(pady=6)
    temple_label = Label(left, text="Temple:").pack(pady=6)
    average_label = Label(left, text="Average:").pack(pady=6)
    color_label = Button(left, text="Pick a Color", command=lambda:choose_color(color_name)).pack(pady=5)
    ok_button = Button(bot, text="Confirm", command=lambda: confirm_group_input(window, version.get(), group_id.get(), 
                       name.get(), args.get(), threads.get(), temple.get(), average.get(), color_name.get()))
    ok_button.pack(in_=bot)


def add_test():
    window = open_new_window("Add a Test")
    top = Frame(window)
    top.pack(side=TOP, fill=BOTH, expand=True)
    bot = Frame(window)
    bot.pack(side=BOTTOM, fill=BOTH, expand=True)
    left = Frame(top)
    left.pack(side=LEFT, fill=BOTH, expand=True)
    right = Frame(top)
    right.pack(side=RIGHT, fill=BOTH, expand=True)
    version = Entry(right)
    version.pack(pady=5)
    name = Entry(right)
    name.pack(pady=5)
    path = Entry(right)
    path.pack(pady=5)
    args = Entry(right)
    args.pack(pady=5)
    threads = Entry(right)
    threads.pack(pady=5)
    stdin = Entry(right)
    stdin.pack(pady=5)
    timestamp = Frame(right)
    var = IntVar()
    radio_one = Radiobutton(timestamp, text="true", variable=var, value=1)
    radio_one.pack(side=LEFT)
    radio_two = Radiobutton(timestamp, text="false", variable=var, value=0)
    radio_two.pack(side=RIGHT)
    timestamp.pack(pady=5)
    graphs = Entry(right)
    graphs.pack(pady=5)
    version_label = Label(left, text="Version:").pack(pady=5)
    name_label = Label(left, text="Name:").pack(pady=6)
    path_label = Label(left, text="Path:").pack(pady=6)
    args_label = Label(left, text="Args:").pack(pady=6)
    threads_label = Label(left, text="Threads:").pack(pady=6)
    stdin_label = Label(left, text="Stdin:").pack(pady=6)
    timestamp_label = Label(left, text="Timestamp:").pack(pady=6)
    graphs_label = Label(left, text="Graphs:").pack(pady=6)
    ok_button = Button(bot, text="Confirm",
                       command=lambda: confirm_test_input(window,version.get(), name.get(), path.get(), args.get(),
                                                          threads.get(), stdin.get(), var.get(), graphs.get()))
    ok_button.pack(in_=bot)


def confirm_test_input(to_close,version,name,path,args,threads,stdin,timestamp,graphs):
    write_me(version, name, path, args, threads, stdin, str(
        True if timestamp == 1 else False), graphs, "data_test.txt")
    to_close.destroy()
    master.destroy()
    os.execv(sys.executable, ['python'] + sys.argv)


def confirm_group_input(to_close,version,group_id,name,args,threads,temple,average,color_name):
    write_me(version, group_id, name, args, threads, temple, average, color_name, "group_test.txt")
    to_close.destroy()
    master.destroy()
    os.execv(sys.executable, ['python'] + sys.argv)


def open_new_window(default_title="Default Title"):
    new_window = Toplevel(master)
    new_window.title(default_title)
    new_window.geometry("300x350")
    Label(new_window).pack()
    return new_window


def init_test_frame(frame):
    top = Frame(frame)
    top.pack(side=TOP, fill=BOTH, expand=True)
    bot = Frame(frame)
    bot.pack(side=BOTTOM, fill=BOTH, expand=True)
    add_button = Button(bot, text="Add", command = add_test )
    ok_button = Button(bot, text="Confirm", command = lambda:os.execv(sys.executable, ['python'] + ['main.py'] + [sys.argv]))
    remove_button = Button(bot, text="Remove", command = add_test )
    add_button.pack(in_=bot, side=LEFT)
    ok_button.pack(in_=bot, side=RIGHT)
    remove_button.pack(in_=bot, side=LEFT)
    random_button = Button(bot, text="Random", command = add_test )
    random_button.pack(in_=bot, side=LEFT)
    lines = read_me("data_test.txt")
    tree=ttk.Treeview(top)
    tree["columns"]=("1","2","3","4","5","6","7")
    tree.column("#0", width=100, minwidth=50)
    tree.column("1", width=100, minwidth=50)
    tree.column("2", width=100, minwidth=50)
    tree.column("3", width=100, minwidth=50)
    tree.column("4", width=100, minwidth=50)
    tree.column("5", width=100, minwidth=50)
    tree.column("6", width=100, minwidth=50)
    tree.column("7", width=100, minwidth=50)
    tree.heading("#0",text="Version",anchor=W)
    tree.heading("1", text="Name",anchor=W)
    tree.heading("2", text="Path",anchor=W)
    tree.heading("3", text="Args",anchor=W)
    tree.heading("4", text="Threads",anchor=W)
    tree.heading("5", text="Stdin",anchor=W)
    tree.heading("6", text="Timestamp",anchor=W)
    tree.heading("7", text="Graphs",anchor=W)
    tree.pack()
    i=0
    for line in lines:
        if line.isspace():
            continue
        tmp_line=line.split(";")
        tree.insert("",i,None,text=tmp_line[0], values=tmp_line[1:])


def remove_test():
    window = open_new_window("Remove a Test")
    all = Frame(window)
    all.pack(side=TOP, fill=BOTH, expand=True)
    to_remove = Entry(all)
    to_remove.pack(pady=5)
    to_remove_button =  Button(all, text="Remove", command = lambda:remove_line_function('data_test.txt',to_remove.get()))
    to_remove_button.pack(pady=5)


def remove_line_function(txt,n_line=0):
    lines=read_me(txt)
    new_file=[]
    count=1
    for i in lines:
        if count!=n_line:
            new_file.append(i)
        count+=1
    f = open(txt,"w")
    f.write(new_file)
    f.close


def init_group_by_frame(frame):
    top = Frame(frame)
    top.pack(side=TOP, fill=BOTH, expand=True)
    bot = Frame(frame)
    bot.pack(side=BOTTOM, fill=BOTH, expand=True)
    add_button = Button(bot, text="Add", command = add_group)
    ok_button = Button(bot, text="Confirm", command = lambda:os.execv(sys.executable, ['python'] + ['main.py'] + [sys.argv]))
    remove_button = Button(bot, text="Remove", command = remove_test)
    add_button.pack(in_=bot, side=LEFT)
    ok_button.pack(in_=bot, side=RIGHT)
    remove_button.pack(in_=bot, side=LEFT)
    lines = read_me("data_group.txt")
    tree=ttk.Treeview(top)
    tree["columns"]=("1","2","3","4","5","6","7")
    tree.column("#0", width=100, minwidth=50)
    tree.column("1", width=100, minwidth=50)
    tree.column("2", width=100, minwidth=50)
    tree.column("3", width=100, minwidth=50)
    tree.column("4", width=100, minwidth=50)
    tree.column("5", width=100, minwidth=50)
    tree.column("6", width=100, minwidth=50)
    tree.column("7", width=100, minwidth=50)
    tree.heading("#0", text="Version",anchor=W)
    tree.heading("1",text="Group ID",anchor=W)
    tree.heading("2", text="Name",anchor=W)
    tree.heading("3", text="Args",anchor=W)
    tree.heading("4", text="Threads",anchor=W)
    tree.heading("5", text="Temple",anchor=W)
    tree.heading("6", text="Average",anchor=W)
    tree.heading("7", text="Color",anchor=W)
    tree.pack()
    i=0
    for line in lines:
        if line.isspace():
            continue
        tmp_line=line.split(";")
        tree.insert("",i,None,text=tmp_line[0], values=tmp_line[1:])


def init_draw_frame(frame):
    main = Frame(frame)
    main.pack(side=TOP, fill=BOTH, expand=True)
    figure = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    figure.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    canvas = FigureCanvasTkAgg(figure, master=main)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, main)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def main():
    # notebook init
    notebook = ttk.Notebook(master)
    notebook.pack()

    # widgets construction
    test_frame = Frame(notebook, width = 480, height = 300)
    group_frame = Frame(notebook, width = 480, height = 300)
    draw_frame = Frame(notebook, width = 480, height = 300)

    # packing widgets to parents
    test_frame.pack(fill="both", expand=1)
    group_frame.pack(fill="both", expand=1)
    draw_frame.pack(fill="both", expand=1)

    # adding the frames to the notebook
    notebook.add(test_frame, text = "Test")
    notebook.add(group_frame, text = "Group By")
    notebook.add(draw_frame, text = "Draw")

    # frames initialization
    init_test_frame(test_frame)
    init_group_by_frame(group_frame)
    init_draw_frame(draw_frame)

    # mainLoop
    master.mainloop()


if __name__ == '__main__':
    main()