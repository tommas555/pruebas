import os
from pikepdf import Pdf
import tkinter as tk
from tkinter import filedialog
import pruebas as pr

#opening a window to select a file
root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()


menu = """Presionar un número para separar el PDF:
1: Separar en grupos de (1)
2: Separar en grupos de (2) 
3: Separar en grupos de (3) 
4: Separar en grupos de (5) 
5: Separar en grupos de (10) 
6: Separar en grupos de (20) 
7: Salir/Cancelar
"""
print(menu)
# capturando el valor de entrada del menú
option = int(input())

# abriendo el pdf y obteniendo el número de paginas para dividirlo
pdf = Pdf.open(filename)
pages = len(pdf.pages)

# iniciando valores para enviar a las funciones y obtener el diccionario de hojas del PDF
Dic_pages = {} 
key = 0
value = 0

# Diccionario que llamas a las funciones crear las listas
switch_semana = {
	1: pr.Separar_grupos_1,
	2: pr.Separar_grupos_2,
	3: pr.Separar_grupos_3,
	4: pr.Separar_grupos_5,
	5: pr.Separar_grupos_10,
	6: pr.Separar_grupos_20
}

# devuelve una lista con las paginas del PDF
Dic_pages = switch_semana.get(option, pr.error)(Dic_pages, pages, key, value)

# make the new splitted PDF files
new_pdf_files = [ Pdf.new() for i in Dic_pages ]
print(f'que es {new_pdf_files}')
# the current pdf file index
new_pdf_index = 0

# iterate over all PDF pages
for n, page in enumerate(pdf.pages):
    if n in list(range(*Dic_pages[new_pdf_index])):
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")
    else:
        # make a unique filename based on original file name plus the index
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}-{new_pdf_index}.pdf"
        # save the PDF file
        new_pdf_files[new_pdf_index].save(output_filename)
        print(f"[+] File: {output_filename} saved.")
        # go to the next file
        new_pdf_index += 1
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")

# save the last PDF file
name, ext = os.path.splitext(filename)
output_filename = f"{name}-{new_pdf_index}.pdf"
new_pdf_files[new_pdf_index].save(output_filename)
print(f"[+] File: {output_filename} saved.")

