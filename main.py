import tkinter as tk

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('PyCharm')
    root=tk.Tk()
    root.configure(background='Black')
    root.geometry('1500x500')
    root.minsize(1500,500)
    root.maxsize(1500,500)
    f1=tk.LabelFrame(root,text='frame1',background='Red',height=200,width=700)
    f2 = tk.LabelFrame(root,text='frame2', background='Green',height=200,width=700)
    f3 = tk.LabelFrame(root,text='frame3', background='Yellow',height=200,width=700)
    f4=tk.LabelFrame(root,text='frame4',background='Cyan',height=200,width=f1.__getitem__('width'))
    # Frame1
    #All f1l1 are labels on top
    #labels goes on with increasing numbers

    f1l1 = tk.Label(f1, text="Open Images")
    f1files = tk.Entry(f1, text='\t\t\t',state='disabled')
    f1select = tk.Button(f1, text="select files")
    Imgtopdf = tk.Button(f1, text='Imgtopdf')
    option = str()
    option='Original'
    orignal=tk.Radiobutton(f1,text='Original',variable=option,value='Original',indicatoron=1)
    scanned=tk.Radiobutton(f1,text='Scanned',variable=option,value='Scanned',indicatoron=1)
    f1convert = tk.Button(f1, text='convert')
    f1compress = tk.Button(f1, text='compress')

    f1l1.grid(row=0, column=0, columnspan=2,sticky=tk.NW,padx=10,pady=30)
    f1files.grid(row=1, column=0,sticky=tk.NW,padx=10,pady=10)
    f1select.grid(row=1, column=1,sticky=tk.NE,padx=10,pady=10)
    orignal.grid(row=2, column=0, columnspan=2,sticky=tk.NW,padx=10,pady=10)
    scanned.grid(row=3, column=0, columnspan=2,sticky=tk.NW,pady=10,padx=10)
    Imgtopdf.grid(row=4, column=0, columnspan=2,padx=10,sticky=tk.NW,pady=10)
    f1convert.grid(row=5,padx=10,pady=10,columnspan=2,sticky=tk.NW)
    f1compress.grid(row=6,padx=10,pady=10,columnspan=2,sticky=tk.NW)
    #Frame2
    f2l1 = tk.Label(f2, text="Open docx files")
    f2files = tk.Entry(f2, text='\t\t\t',state='disabled')
    f2select = tk.Button(f2, text="select files")
    f2convert = tk.Button(f2, text='convert')
    f2compress=tk.Button(f2,text='compress')

    f2l1.grid(row=0, column=0, columnspan=2,padx=10,pady=30,sticky=tk.NW)
    f2files.grid(row=1, column=0, sticky=tk.NW,padx=10,pady=10)
    f2select.grid(row=1, column=1, sticky=tk.NE,pady=10)
    f2convert.grid(row=2,pady=10,padx=10,columnspan=2,sticky=tk.NW)
    f2compress.grid(row=3,pady=10,padx=10,columnspan=2,sticky=tk.NW)

    # Frame3
    f3l1 = tk.Label(f3, text="Open pptx files")
    f3files = tk.Entry(f3, text='\t\t\t',state='disabled')
    f3select = tk.Button(f3, text="select files")
    f3convert = tk.Button(f3, text='convert')
    f3compress = tk.Button(f3, text='compress')

    f3l1.grid(row=0, column=0, columnspan=2,padx=10,pady=30,sticky=tk.NW)
    f3files.grid(row=1, column=0, sticky=tk.NW,padx=10,pady=10)
    f3select.grid(row=1, column=1, sticky=tk.NE,pady=10)
    f3convert.grid(row=2,pady=10,padx=10,columnspan=2,sticky=tk.NW)
    f3compress.grid(row=3,pady=10,padx=10,columnspan=2,sticky=tk.NW)

    # Frame4
    f4l1 = tk.Label(f4, text="Open pdf files")
    f4files1 = tk.Entry(f4, text='\t\t\t',state='disabled')
    f4select1 = tk.Button(f4, text="select files")
    merge = tk.Button(f4, text='Merge')
    f4l2 = tk.Label(f4, text="Open pdf file")
    f4files2 = tk.Entry(f4, text='\t\t\t',state='disabled')
    f4select2 = tk.Button(f4, text="select files")
    f4l3=tk.Label(f4,text='Enter pg nos')
    pages=tk.Entry(f4,text='\t\t\t')
    split = tk.Button(f4, text='Split')

    f4l1.grid(row=0, column=0, columnspan=2,padx=10,pady=30,sticky=tk.NW)
    f4files1.grid(row=1, column=0, sticky=tk.NW,padx=10,pady=10)
    f4select1.grid(row=1, column=1, sticky=tk.NW,pady=10)
    merge.grid(row=2,padx=10,pady=10,columnspan=2,sticky=tk.NW)
    f4l2.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NW)
    f4files2.grid(row=4, column=0, sticky=tk.NW,padx=10,pady=10)
    f4select2.grid(row=4, column=1, sticky=tk.NW,pady=10)
    f4l3.grid(row=5,column=0,padx=10,pady=10,sticky=tk.NW)
    pages.grid(row=5,column=1,sticky=tk.W)
    split.grid(row=6,padx=10,pady=10,columnspan=2,sticky=tk.NW)

    f1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
    f2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

    f4.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
    f3.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
    root.mainloop()
'''
    f1.grid(row=0,column=0)
    f2.grid(row=0,column=1)
    f3.grid(row=0,column=2)
    f4.grid(row=0,column=3)
'''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
