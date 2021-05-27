import os
from wand.image import Image


def convert_pdf_to_jpg(filename):
    pdf_list = []
    os.chdir(filename)
    for i in os.listdir():
        if ".pdf" in i:
            pdf_list.append(i)
    sorted(pdf_list)
    t = 0
    print(pdf_list)
    for i in pdf_list:
        with Image(filename=i) as img:
            with img.convert('jpeg') as converted:
                converted.save(filename=i.split(".")[0] + '.jpg')
                t = t + 1


convert_pdf_to_jpg(os.getcwd())


