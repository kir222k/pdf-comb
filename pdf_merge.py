import os
from tkinter import filedialog
from tkinter import *
from def_get_list_lst_files import list_files_x
from PyPDF2 import PdfFileMerger, PdfFileReader
# import argparse
# import sys
import sys

# ---------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder = os.path.normpath(sys.argv[1])
        print(sys.argv[1])
    else:
        folder = filedialog.askdirectory()
# print(folder)

# ---------------------------
def pfd_merge(input_folder, input_pdf_list, output_pdf):
    merged_pdf = PdfFileMerger()
    for document_name in input_pdf_list:
        merged_pdf.append(PdfFileReader(os.path.join(input_folder, document_name), 'rb'))
    merged_pdf.write(output_pdf)

# ---------------------------
list_of_files=os.listdir(folder)
print('list_of_files: ', list_of_files)

# ---------------------------
list_of_files_sort=list_files_x([os.path.splitext(x)[0] for x in list_of_files])
print('list_of_files_sort: ', list_of_files_sort)

for fl in list_of_files_sort:
    # for lk in fl:
    flp=[os.path.join(folder,(x)+".pdf") for x in fl]
    flp = [(folder+ "\\"+(x) + ".pdf") for x in fl]
    print(flp)
    nn= os.path.join(folder, fl[0] + "_.pdf")
    # # print(fl)
    print(flp[0])

    pfd_merge(folder, flp, nn)

    for mm in flp:
        os.remove(mm)
    os.rename(nn, os.path.join(folder, fl[0] + ".pdf"))

input("Press Enter to exit")

print("\nEnd")
print("\nEnd2")
print("\nEnd")
# print('\nend2')
