import tkinter
import pytube
from webbrowser import open_new
from textwrap import TextWrapper



root = tkinter.Tk()
root.geometry("350x325")
root.title("Py YouTube Downloader")
root. wm_iconbitmap(".icon\\Icon.ico")
root.resizable(0,0)
root.wm_minsize(0,0)

def callback(url):
    open_new(url)

link1 = tkinter.Label(root, text="Open YouTube", fg="red", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://youtube.com/"))

tkinter.Label(root, text="Download any YouTube Video", font="Helvetica").pack()

myVar = tkinter.StringVar()
myVar.set("Enter a valid YouTube Link:")
tkinter.Label(root, textvariable=myVar, width=50).pack(pady=5)

link = tkinter.StringVar()

def download():
    try:
        myVar.set("")
        root.update()
        pytube.YouTube(link.get()).streams.first().download(skip_existing=True, output_path="./Your Downloads")
        w = TextWrapper()
        w.width = 50
        title_wrapped = "\n".join(w.wrap(str(pytube.YouTube(link.get()).title)))
        myVar.set("Download was successfully!\n\n{}".format(title_wrapped))
    except:
        myVar.set("You specified an unvalid link, try again please.\nIt should look like: www.youtube.com/watch?v=7zpxgyG7eGk")

tkinter.Entry(root, textvariable=link, width=40).pack(pady=10)
tkinter.Button(root, text=f"Download Video!", command=download, fg="green", bg="white").pack()
tkinter.Label(root, text="\rThe Downloaded Video will be in the \nsame folder, as this program is.", font=("Helvetica", 8)).pack()
tkinter.Label(root, text="\r-- Developed by ARealWant --\nSource available on GitHub", font=("Helvetica", 8)).pack()

root.mainloop()