import tkinter as tk
from PIL import ImageTk,Image
from DOC_CVT import *
# Press the green button in the gutter to run the script.
filelist=list()
curpath=[]
cur=None
curfile=''
scan=False
def org():
    scan=False
def sc():
    scan=True
def fileselect(files):
    global curpath,filelist,cur,curfile
    # for s in filelist:
    #     s.configure(state='normal')
    #     s.delete(0,tk.END)
    #     s.insert(0,'\t\t\t')
    #     s.configure(state='disabled')
    for s in [f1files, f2files, f3files,compfiles, f4files1, f4files2]:
        if not s==files:
            s.configure(state='normal')
            s.delete(0,tk.END)
            s.insert(0,'\t\t\t')
            s.configure(state='disabled')
    files.configure(state='normal')
    files.delete(0,tk.END)
    curpath.clear()
    curpath=fileChooser()
    files.delete(0,tk.END)
    print(curpath)
    files.insert(0,curpath)
    files.configure(state='disabled')
    cur=files
    curfile=curpath
    if files==f4files2:
        wb.open_new(str(curpath[0]))

def convert(frame):
    global curfile,scanned
    if cur==frame:
        if frame==f1files and option.get()==2:
            scanner(curpath)
        elif frame==f1files:
            curfile=imagesToPDFs(curpath)
        elif frame==f2files:
            curfile=wordToPDF(curpath)
        elif frame==f3files:
            curfile=pptxToPDF(curpath)
        elif frame==f4files1:
            curfile=mergePDFs(curpath)
        elif frame==f4files2:
            curfile=pdfSplit(curpath[0],pages.get())
        elif frame==compfiles:
            CompressPDF(curpath)


def comp(frame):
    global curfile
    print(frame)
    if cur==frame:
        CompressPDF(str(curfile[0]))

if __name__ == '__main__':

    root=tk.Tk()
    windowIncon = ImageTk.PhotoImage(Image.open('converter.jpeg'))
    root.iconphoto(False, windowIncon)
    root.configure(background='Black')
    root.geometry('1500x550')
    root.resizable(width=False, height=False)
    root.title("Document Converion Tool")
    f1=tk.LabelFrame(root,text='Images to PDF',background='light blue',height=200,width=700, font='georgia 12 bold')
    f2 = tk.LabelFrame(root,text='DOCX To PDF', background='light blue',height=200,width=700, font='georgia 12 bold')
    f3 = tk.LabelFrame(root,text='PPTX To PDF', background='light blue',height=200,width=700, font='georgia 12 bold')
    f4=tk.LabelFrame(root,text='SPLIT & MERGE PDF',background='light blue',height=200,width=f1.__getitem__('width'), font='georgia 12 bold')
    # Frame1
    #All f1l1 are labels on top
    #labels goes on with increasing numbers

    f1l1 = tk.Label(f1, text="Open Images", font='georgia 12 bold', bg='light blue')
    f1files = tk.Entry(f1,state='disabled', width=25)
    foldericon = ImageTk.PhotoImage(Image.open('file.jpeg').resize((40,40)))
    f1select = tk.Button(f1, text="select files", font='georgia 12 bold', pady=5, image=foldericon, compound=tk.RIGHT,command=lambda:fileselect(f1files))
    option = tk.IntVar()
    option.set(1)
    orignal=tk.Radiobutton(f1,text='Original',variable=option,value=1,indicatoron=1, font='georgia 12 bold',command=org)
    scanned=tk.Radiobutton(f1,text='Scanned',variable=option,value=2,indicatoron=1, font='georgia 12 bold',command=sc)
    print(option.get())
    imgtopdficon = ImageTk.PhotoImage(Image.open('img2pdf.jpeg').resize((60,60)))
    f1convert = tk.Button(f1, text='convert', padx=15, pady=5, font='georgia 12 bold', image=imgtopdficon, compound=tk.RIGHT,command=lambda:convert(f1files))
    compresspdficon = ImageTk.PhotoImage(Image.open('compress.jpeg').resize((60,60)))
    #f1compress = tk.Button(f1, text='compress', padx=15, pady=5, font='georgia 12 bold', image=compresspdficon, compound=tk.RIGHT,command=lambda:comp(f1files))

    f1l1.grid(row=0, column=0, columnspan=2,sticky=tk.NW,padx=10,pady=30)
    f1files.grid(row=1, column=0,sticky=tk.NW,padx=10,pady=10)
    f1select.grid(row=1, column=1,sticky=tk.NE,padx=10,pady=10)
    orignal.grid(row=2, column=0, columnspan=2,sticky=tk.NW,padx=10,pady=10)
    scanned.grid(row=3, column=0, columnspan=2,sticky=tk.NW,pady=10,padx=10)
    f1convert.grid(row=5,padx=10,pady=10,columnspan=2,sticky=tk.NW)
    #f1compress.grid(row=6,padx=10,pady=10,columnspan=2,sticky=tk.NW)
    #Frame2
    f2l1 = tk.Label(f2, text="Open docx files", font='georgia 12 bold', bg='light blue')
    f2files = tk.Entry(f2, text='\t\t\t',state='disabled', width=25)
    f2select = tk.Button(f2, text="select files", font='georgia 12 bold', pady=5, image=foldericon, compound=tk.RIGHT,command=lambda:fileselect(f2files))
    docx2pdficon = ImageTk.PhotoImage(Image.open('docx.jpeg').resize((60,60)))
    f2convert = tk.Button(f2, text='convert', padx=15, pady=5, font='georgia 12 bold', image=docx2pdficon, compound=tk.RIGHT,command=lambda:convert(f2files))
    f2compress=tk.Button(f2,text='compress', padx=15, pady=5, font='georgia 12 bold', image=compresspdficon, compound=tk.RIGHT,command=lambda:comp(compfiles))
    f2l2 = tk.Label(f2, text="Open pdf files to compress", font='georgia 12 bold', bg='light blue')
    compfiles = tk.Entry(f2, text='\t\t\t', state='disabled', width=25)
    compselect = tk.Button(f2, text="select files", font='georgia 12 bold', pady=5, image=foldericon, compound=tk.RIGHT,command=lambda: fileselect(compfiles))

    f2l1.grid(row=0, column=0, columnspan=2,padx=10,pady=30,sticky=tk.NW)
    f2files.grid(row=1, column=0, sticky=tk.NW,padx=10,pady=10)
    f2select.grid(row=1, column=1, sticky=tk.NE,pady=10)
    f2convert.grid(row=2,pady=10,padx=10,columnspan=2,sticky=tk.NW)
    f2l2.grid(row=3, column=0, columnspan=2,padx=10,pady=30,sticky=tk.NW)
    compfiles.grid(row=4, column=0, sticky=tk.NW,padx=10,pady=10)
    compselect.grid(row=4, column=1, sticky=tk.NE, pady=10)
    f2compress.grid(row=5,pady=10,padx=10,columnspan=2,sticky=tk.NW)
    # Frame3
    f3l1 = tk.Label(f3, text="Open pptx files", font='georgia 12 bold', bg='light blue')
    f3files = tk.Entry(f3, text='\t\t\t',state='disabled', width=25)
    f3select = tk.Button(f3, text="select files", font='georgia 12 bold', pady=5, image=foldericon, compound=tk.RIGHT,command=lambda:fileselect(f3files))
    pptxtopdficon = ImageTk.PhotoImage(Image.open('pptx.jpeg').resize((60,60)))
    f3convert = tk.Button(f3, text='convert', padx=15, pady=5, font='georgia 12 bold', image=pptxtopdficon, compound=tk.RIGHT,command=lambda:convert(f3files))
    #f3compress = tk.Button(f3, text='compress', padx=15, pady=5, font='georgia 12 bold', image=compresspdficon, compound=tk.RIGHT,command=lambda:comp(f3files))

    f3l1.grid(row=0, column=0, columnspan=2,padx=10,pady=30,sticky=tk.NW)
    f3files.grid(row=1, column=0, sticky=tk.NW,padx=10,pady=10)
    f3select.grid(row=1, column=1, sticky=tk.NE,pady=10)
    f3convert.grid(row=2,pady=10,padx=10,columnspan=2,sticky=tk.NW)
    #f3compress.grid(row=3,pady=10,padx=10,columnspan=2,sticky=tk.NW)

    # Frame4
    f4l1 = tk.Label(f4, text="Open pdf files", font='georgia 12 bold', bg='light blue')
    f4files1 = tk.Entry(f4, state='disabled', font='georgia 12 bold', width=20)
    f4select1 = tk.Button(f4, text="select files", font='georgia 12 bold', pady=5, image=foldericon, compound=tk.RIGHT,command=lambda:fileselect(f4files1))
    mergepdficon = ImageTk.PhotoImage(Image.open('merge.jpeg').resize((60,60)))
    merge = tk.Button(f4, text='Merge', padx=15, pady=5, font='georgia 12 bold', image=mergepdficon, compound=tk.RIGHT,command=lambda:convert(f4files1))
    f4l2 = tk.Label(f4, text="Open pdf file", font='georgia 12 bold', bg='light blue')
    f4files2 = tk.Entry(f4, state='disabled', font='georgia 12 bold', width=20)
    f4select2 = tk.Button(f4, text="select files", pady=5, image=foldericon, compound=tk.RIGHT, font='georgia 12 bold',command=lambda:fileselect(f4files2))
    f4l3=tk.Label(f4,text='Enter page numbers (,) sepeaerated:', font='georgia 12 bold', bg='light blue')
    pages=tk.Entry(f4, width=20)
    splitpdficon = ImageTk.PhotoImage(Image.open('split.jpeg').resize((60,60)))
    split = tk.Button(f4, text='Split', padx=15, pady=5, font='georgia 12 bold', image=splitpdficon, compound=tk.RIGHT,command=lambda:convert(f4files2))

    f4l1.grid(row=0, column=0, columnspan=2,padx=10,pady=30,sticky=tk.NW)
    f4files1.grid(row=1, column=0, sticky=tk.NW, pady=10)
    f4select1.grid(row=1, column=1, sticky=tk.NW, pady=10)
    merge.grid(row=2,padx=10,pady=5, columnspan=2,sticky=tk.NW)
    f4l2.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NW)
    f4files2.grid(row=4, column=0, sticky=tk.NW,padx=10,pady=10)
    f4select2.grid(row=4, column=1, sticky=tk.NW,pady=10)
    f4l3.grid(row=5,column=0, pady=10,sticky=tk.NW)
    pages.grid(row=5, column=1, sticky=tk.W)
    split.grid(row=6,padx=10, columnspan=2,sticky=tk.NW)

    f1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
    f2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

    f4.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
    f3.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

    root.mainloop()
filelist = [f1files, f2files, f3files,compfiles, f4files1, f4files2]

'''
    f1.grid(row=0,column=0)
    f2.grid(row=0,column=1)
    f3.grid(row=0,column=2)
    f4.grid(row=0,column=3)
'''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
