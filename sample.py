import tkinter as tk

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    root=tk.Tk()
    root.configure(background='Black')
    f1=tk.LabelFrame(root,text='frame1',background='Red')


    # Frame1
    f1l1 = tk.Entry(f1, text="Open Images")
    f1files = tk.Entry(f1, text='\t\t\t\t')
    f1select = tk.Button(f1, text="select files")
    Imgtopdf = tk.Button(f1, text='Imgtopdf')
    option = str()
    option='Original'
    orignal=tk.Radiobutton(f1,text='Original',variable=option,value='Original',indicatoron=2)
    scanned=tk.Radiobutton(f1,text='Scanned',variable=option,value='Scanned',indicatoron=2)
    f1convert = tk.Button(f1, text='convert')
    f1compress = tk.Button(f1, text='compress')

    f1l1.grid(row=0, column=0, columnspan=2,padx=10,pady=30)
    f1files.grid(row=1, column=0,sticky=tk.NW,padx=10,pady=10)
    f1select.grid(row=1, column=1,sticky=tk.NE,padx=10,pady=10)
    orignal.grid(row=2, column=0, columnspan=2,sticky=tk.NW,padx=10,pady=10)
    scanned.grid(row=3, column=0, columnspan=2,sticky=tk.NW,padx=10,pady=10)
    Imgtopdf.grid(row=4, column=0, columnspan=2,padx=10,pady=30)
    f1convert.grid(row=5,pady=20,columnspan=2)
    f1compress.grid(row=6,pady=20,columnspan=2)

    f1.pack()
    root.geometry('220x220')
    root.mainloop()
