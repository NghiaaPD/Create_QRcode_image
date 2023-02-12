from tkinter import*
import qrcode as qr
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import cv2
import numpy as np

system = Tk()
system.geometry("1000x850")
system.title("chương trình tạo mã QRcode")
# system.configure(bg="#58C8F5")
background = Image.open("Nam.png")
background_size=background.resize((1000,900))
background_ImageTk = ImageTk.PhotoImage(background_size)
background_Label = Label(system,image=background_ImageTk)
background_Label.place(x=0,y=0)



Label_Main = Label(system,text="Đầu vào",font=("Arial Bold",15),bg="#000000",fg="white",height=1)
Label_Main.place(relx=.1,rely=.04)

Main_input = Text(system,width=40,height =5,font=("Lato-Black",10))
Main_input.place(relx=.0, rely=.1)



Label_Name = Label(system,text="Tên",font=("Arial Bold",15),bg="#000000",fg="white",height=1)
Label_Name.place(relx=.35,rely=.04)

Name_input = Text(system,width=20,height =5, font=("Lato-Black",10))
Name_input.place(relx=.3, rely=.1)


Format_Label = Label(system,text="Chọn định dạng ảnh QR",font=("Arial bold",15),bg="#000000",fg="white",height=1)
Format_Label.place(relx=.1, rely=.3)

Format_choose = Combobox(system, width = 27)
Format_choose['values'] = ('.png',
                          '.jpg',
                          '.webp',
                        )
Format_choose.place(relx = .1, rely=.35)
Format_choose.current()

def delete():
    Main_input.delete(0.0,END)
    Name_input.delete(0.0,END)
Delete_button = Button(system,text="Delete",font=("Arial Bold",10),bg="#000000",fg="white", command = delete)
Delete_button.place(relx=.2, rely=.2)

def make_QR():
    data = Main_input.get(0.0,END)
    img = qr.make(data)
    img.save(str(Name_input.get(0.0,END)).strip('\n') + str(Format_choose.get()))
Start_button = Button(system,text="Create a QR picture",font=("Arial Bold",10),bg="#000000",fg="white", command=make_QR)
Start_button.place(relx=.05,rely=.2)

def make_QR_split():
    data = Main_input.get(0.0,END)
    img = qr.make(data)
    img.save(str(Name_input.get(0.0,END)).strip('\n') + str(Format_choose.get()))

    # Chuyển đổi PIL Image sang numpy array
    image_split = np.array(img.getdata(), dtype=np.uint8).reshape(img.size[1], img.size[0])
    height, width = image_split.shape[:2]

    # Cắt bức ảnh thành 10 phần
    part1 = image_split[0:height // 2, 0:(width // 5)]
    part2 = image_split[0:height // 2, (width // 5):(2 * width // 5)]
    part3 = image_split[0:height // 2, (2 * width // 5):(3 * width // 5)]
    part4 = image_split[0:height // 2, (3 * width // 5):(4 * width // 5)]
    part5 = image_split[0:height // 2, (4 * width // 5):width]

    part6 = image_split[height // 2:height, 0:(width // 5)]
    part7 = image_split[height // 2:height, (width // 5):(2 * width // 5)]
    part8 = image_split[height // 2:height, (2 * width // 5):(3 * width // 5)]
    part9 = image_split[height // 2:height, (3 * width // 5):(4 * width // 5)]
    part10 = image_split[height // 2:height, (4 * width // 5):width]

    # Lưu 2 phần cắt được vào 2 tập tin khác nhau
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "1" + str(Format_choose.get()), part1)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "2" + str(Format_choose.get()), part2)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "3" + str(Format_choose.get()), part3)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "4" + str(Format_choose.get()), part4)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "5" + str(Format_choose.get()), part5)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "6" + str(Format_choose.get()), part6)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "7" + str(Format_choose.get()), part7)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "8" + str(Format_choose.get()), part8)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "9" + str(Format_choose.get()), part9)
    cv2.imwrite(str(Name_input.get(0.0, END)).strip('\n') + "10" + str(Format_choose.get()), part10)




Result_button_2 = Button(system,text="Tạo ảnh QR đã được cắt",font=("Arial Bold",10),bg="#000000",fg="white", command=make_QR_split)
Result_button_2.place(relx=.05,rely=.25)


system = mainloop()
