import webbrowser
from tkinter import *

print(webbrowser.get(using=None))

root = Tk()
root.title("영단어 검색 자동화")
root.geometry("500x250+100+100")
root.resizable(True, True)

e = Entry(root, width=45, borderwidth=5, fg="black", bg="white")
e.pack()

e.insert(0, "")

result = webbrowser.get()
print(result)

def Click():
    # 변수 정의
    syn_query = str(e.get()) + " synonym"
    mean_query = str(e.get())
    ex_query = str(e.get()) + " example in sentence"
    krMean_query = str(e.get()) + " 뜻"

    syn_url = "https://www.google.com/search?q=" + syn_query
    mean_url = "https://www.dictionary.com/browse/" + mean_query
    ex_url = "https://www.google.com/search?q=" + ex_query
    krMean_url = "https://search.naver.com/search.naver?query=" + krMean_query

    e.delete(0, END)

    # 동작 실행
    webbrowser.open(krMean_url)
    webbrowser.open(syn_url)
    webbrowser.open(mean_url)
    webbrowser.open(ex_url)

button = Button(root, text="Enter", command=Click, fg="black", bg="white")
button.pack()

root.mainloop()