import pandas as pd
import numpy as np
import Barcode_generator
from barcode.writer import ImageWriter 
from PIL import Image,ImageDraw
from barcode import EAN13  
import pyzbar.pyzbar as pyzbar
import PDF_Format_maker
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import CSV_Gen_for_barcode_numbers
import tkinter as tk
from tkinter import filedialog
import os
def main():
  filepath=filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
  if filepath:
    try:
        data= pd.read_csv(filepath)
        print(data)
    except Exception as e:
        print("Error reading CSV:", e)
  root = tk.Tk()
  folder_to_save=filepath.split("/")[-1].strip(".csv")
  os.makedirs(f"./{folder_to_save}",exist_ok=True)
  os.makedirs(f"./{folder_to_save}_large",exist_ok=True)
  os.makedirs(f"./{folder_to_save}_medium",exist_ok=True)
  #note we need to write a logic for creating folder
  data_breif=Barcode_generator.barcode_generator(data,folder_to_save)
  PDF_Format_maker.pdf_format_maker(data,data_breif,folder_to_save)
  CSV_Gen_for_barcode_numbers.csv_gen_for_barcodes(data,data_breif,folder_to_save)


if __name__=="__main__":
    # Create a DataFrame with random data
    main()
   
    