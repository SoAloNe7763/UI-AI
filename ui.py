from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import textwrap
from aift import setting
from aift.multimodal import textqa
setting.set_api_key('Li1PLpPipwxF3k0LHgr1hcMnJSVgiVGI')

GUI = Tk()
GUI.title('โปรแกรมช่วยคิดเมนูอาหาร by SAL')
GUI.geometry('700x600')
GUI.state('zoomed')
style = ttk.Style()
style.configure('My.TButton', font=('TH Saraban New', 24))

def AIreply():
    print('AI กำลังตอบ...')
    result = textqa.generate('กินอะไรดีเที่ยงนี้')
    text = result['content']
    wrapped_text = textwrap.fill(text, width=50)

    v_result.set(wrapped_text)

B1 = ttk.Button(GUI,text='วันนี้กินอะไรดี?', style='My.TButton' ,command=AIreply)
B1.pack(pady=30,ipadx=30, ipady=20)

v_result = StringVar()
v_result.set('-----output-----')
L1 = ttk.Label(GUI,textvariable=v_result,font=(None,40))
L1.pack()

GUI.mainloop()