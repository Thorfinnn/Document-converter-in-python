import tkinter.messagebox

import img2pdf as ip
import PyPDF2, docx2pdf, os, cv2, win32com.client, pdf2image
import numpy as np
from tkinter import filedialog
import webbrowser as wb
#C:\Users\croma\PYTHON 2021\.idea=homedirpath
def getHomedirpath():
    return os.getcwd()


homedirpath = getHomedirpath()

if "Temp" not in os.listdir(homedirpath):
    os.mkdir(homedirpath + "\Temp")
def scanner(img_list):
    try:
        for img, i in zip(img_list, range(len(img_list))):
            img = cv2.imread(img, 0)
            dilate = cv2.dilate(cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11), np.zeros((2, 2), np.uint8), iterations=1)
            cv2.imwrite(homedirpath + "\Temp\\" + str(i+1) + ".jpg", dilate)
        scan_copies = [homedirpath + "\Temp\\" + str(f) for f in os.listdir(homedirpath + "\Temp")]
        scan_bytes = ip.convert(scan_copies)
        pdf_file = open(filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")])+ ".pdf".strip(), "wb")
        pdf_file.write(scan_bytes)
        print("pdf created successfully!")
        tkinter.messagebox.showinfo('File created', 'File created succesfully')
        for f in scan_copies:
            os.remove(f)
    except Exception as e:
        print(e)
    finally:
        pdf_file.close()

def fileChooser():
    try:
        #returns a list of files manually selected
        filetypes = (("All files", "*.*"),("Images",("*.jpg", "*.png", "*.png")), ("All Pdf Files", "*.pdf"), ("All Word Files", "*.docx"),("All PPTX Files", "*.pptx"))
        filelist = [file.replace("/", "\\") for file in list(filedialog.askopenfilenames(filetypes=filetypes))]
        return filelist
    except Exception as e:
        print(e)


def imagesToPDFs(img_list):
    print(img_list)
    try:
        #Extracting all bytes from every image.
        img_bytes = ip.convert(img_list)
        #Writing image bytes to blank pdf file.
        temppath=filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")]) + ".pdf".strip()
        pdf_file = open(temppath, "wb")
        #Creating a blank pdf file
        pdf_file.write(img_bytes)
        print("pdf created successfully!",flush=True)
        tkinter.messagebox.showinfo('File created', 'File created succesfully')
        # res=tkinter.messagebox.askquestion('Compress file','Do you want to compress file?')
        # if res == 'yes':
        #     CompressPDF(temppath)

    except Exception as e:
        print("some error occured while creating pdf or else wrong file have been chosen!")
    finally:
        #closing pdf writer
        pdf_file.close()
        return temppath

def mergePDFs(pdflist):
    try:
        tempfile=filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")]) + ".pdf".strip()
        pdf_file = open(tempfile,"wb")
        #creating pdfwriter object with the help to PyPDF2 module
        pdfWriter = PyPDF2.PdfFileWriter()
        #looping through all pdfs
        for pdf in pdflist:
            #creating pdfreader object to reader each pdf page
            pdfReader = PyPDF2.PdfFileReader(pdf)
            #iterating through all pages
            for pageNo in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNo)
                pdfWriter.addPage(pageObj)
        #opening blank pdf file in write binary mode
        pdfWriter.write(pdf_file)
        print("pdf created successfully!",flush=True)
        tkinter.messagebox.showinfo('File created', 'File created succesfully')
        # res = tkinter.messagebox.askquestion('Compress file', 'Do you want to compress file?')
        # if res == 'yes':
        #     CompressPDF(tempfile)
    except Exception as e:
        print(e)
        print("some error occured while creating pdf or else wrong file have been chosen!")
    finally:
        pdf_file.close()
        return tempfile
        
def wordToPDF(filepath):
    try:
        if len(filepath) == 1:
            tempfile= filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")])+".pdf"
            docx2pdf.convert(filepath[0],tempfile)
            print("Pdf created successfully!")
            tkinter.messagebox.showinfo('File created', 'File created succesfully')
        else:
            for docx in range(len(filepath)):
                docx2pdf.convert(filepath[docx], homedirpath + "\Temp\DOCX2PDF" + str(docx+1) + ".pdf")
            tempfiles = [homedirpath + "\Temp\\" + str(f) for f in os.listdir(homedirpath + "\Temp")]
            tempfile=mergePDFs(tempfiles)
            for f in tempfiles:
                os.remove(f)
        # res = tkinter.messagebox.askquestion('Compress file', 'Do you want to compress file?')
        # if res == 'yes':
        #     CompressPDF(tempfile)
    except Exception as e:
        print("Some erro occured!", e)
    finally:
        return tempfile

def pptxToPDF(pptfiles):
    comp_path = None
    try:
        ppt = win32com.client.Dispatch("Powerpoint.Application")
        if len(pptfiles) == 1:
            fpath=pptfiles[0]
            pdf = ppt.Presentations.Open(fpath, WithWindow=False)
            spath = filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")]).replace("/", "\\")
            comp_path = spath
            pdf.SaveAs(spath, 32)
            print("Pdf created successfully!")
            tkinter.messagebox.showinfo('File created', 'File created succesfully')
        else:
            for pptx, i in zip(pptfiles, range(len(pptfiles))):
                ppt = win32com.client.Dispatch("Powerpoint.Application")
                pdf = ppt.Presentations.Open(pptx, WithWindow=False)
                pdf.SaveAs(homedirpath + "\\Temp\\PPTX " + str(i+1) + ".pdf", 32)
                pdf.Close()
            tempfiles = [homedirpath + "\Temp\\" + str(f) for f in os.listdir(homedirpath + "\Temp")]
            spath=mergePDFs(tempfiles)
            comp_path=spath
            for f in tempfiles:
                os.remove(f)
        # res = tkinter.messagebox.askquestion('Compress file', 'Do you want to compress file?')
        # if res == 'yes':
        #     CompressPDF(comp_path)
    except Exception as e:
        pass
    finally:
        pdf.Close()
        ppt.Quit()
        return spath

def pdfSplit(path,page):
    pdfreader = PyPDF2.PdfFileReader(str(path))
    pdfwriter = PyPDF2.PdfFileWriter()
    try:
        #wb.open_new(path)
        pagelist =page.split(",")
        for pageNo in range(len(pagelist)):
            pageObj = pdfreader.getPage(int(pagelist[pageNo])-1)
            pdfwriter.addPage(pageObj)
        pdfile = open(filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")]) + ".pdf", "wb")
        pdfwriter.write(pdfile)
        print("Pdf created successfully!")
        tkinter.messagebox.showinfo('File created', 'File created succesfully')
    except Exception as e:
        print(e)
    finally:
        pdfile.close()

def CompressPDF(pdfpath, compressionlvl=70):#Quality level 50, 100, 150
    print(pdfpath)
    images = []
    filesize = round(os.path.getsize(pdfpath)/1048576,2) #in MB
    print(filesize)
    if filesize < 0.240:
        print("Cannot Compress further!")
    elif compressionlvl < 50 or compressionlvl > 150:
        print("Compression level should be in the range 50-200")
        print("x")
    else:
        try:
            images = pdf2image.convert_from_path(pdfpath, dpi=compressionlvl,
                                                 poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')
            for image, i in zip(images, range(len(images))):
                image.save(os.getcwd() + "\Temp\\img" + str(i) + ".jpeg", "JPEG")
            images = [os.getcwd() + "\Temp\\" + f for f in os.listdir(os.getcwd() + "\Temp\\")]
            imgbytes = ip.convert(images)
            pdfile = open(pdfpath.split(".")[0] + "-compress" + ".pdf", "wb")
            pdfile.write(imgbytes)
            print("PDF file compressed!")
            tkinter.messagebox.showinfo('File created', 'File created succesfully')
            pdfile.close()
        except Exception as e:
            print(e)
        finally:
            for f in images:
                os.remove(f)

def main():
    choice = int(input("1-images to pdf\n2-merge pdfs\n3-docx to pdf\n4-single/multiple ppt to pdf\
                 \n5-split pdf\n6-Compress PDF\n7-exit\nEnter your choice:"))
    if choice == 1:
        choice = int(input("scanned(1) or original(0):"))
        if choice == 1:
            scanner(fileChooser())
        else:
            imagesToPDFs(fileChooser())
    if choice == 2:
        mergePDFs(fileChooser())
    if choice == 3:
        wordToPDF(fileChooser())
    if choice == 4:
        pptxToPDF(fileChooser())
    if choice == 5:
        pdfSplit(fileChooser()[0])
    if choice == 6:
        CompressPDF(fileChooser()[0], 150)
    else:
        exit(0)

