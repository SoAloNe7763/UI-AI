from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import textwrap
from aift import setting
from aift.multimodal import textqa

# ตั้งค่า API KEY
setting.set_api_key('Li1PLpPipwxF3k0LHgr1hcMnJSVgiVGI')

# สร้าง GUI
GUI = Tk()
GUI.title('โปรแกรมช่วยคิดเมนูอาหาร by SAL')
GUI.geometry('700x600')
GUI.state('zoomed')

# ตั้งค่า style ปุ่ม
style = ttk.Style()
style.configure('My.TButton', font=('TH Saraban New', 24))

# ฟังก์ชันที่ทำงานเมื่อกดปุ่ม
def AIreply():
    user_input = v_input.get()
    if user_input.strip() == '':
        v_result.set('กรุณาพิมพ์คำถามก่อน')
        return
    print('AI กำลังตอบ...')
    result = textqa.generate(user_input)
    text = result['content']
    wrapped_text = textwrap.fill(text, width=50)
    v_result.set(wrapped_text)

# กล่องข้อความ input
v_input = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_input, font=('TH Sarabun New', 24), width=50)
E1.pack(pady=20)

# ปุ่มเรียก AI
B1 = ttk.Button(GUI, text='ถาม AI', style='My.TButton', command=AIreply)
B1.pack(pady=30, ipadx=30, ipady=20)

# แสดงผลลัพธ์
v_result = StringVar()
v_result.set('-----output-----')
L1 = ttk.Label(GUI, textvariable=v_result, font=('TH Sarabun New', 24), wraplength=1000, justify='left')
L1.pack(padx=20, pady=20, anchor='w')

# เริ่ม GUI
GUI.mainloop()
