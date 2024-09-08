import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageOps
import pandas as pd
def csv_gen_for_barcodes(data,d,folder_to_save):
 data=data
 d=d
 k=0
 print(d.keys())
 for key in d.keys():
    for i in range(1,1+int(d[key][0])):
        print(f'./{folder_to_save}/{data["Delivery Point"][k]}_Medium_{i}.png')
        image=Image.open(f'./{folder_to_save}/{data["Delivery Point"][k]}_Medium_{i}.png')
        gray=ImageOps.grayscale(image)
        # image=cv2.imread(f'./{folder_to_save}/{data["Delivery Point"][k]}_Medium_{i}.png')
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        barcode = pyzbar.decode(gray)
        for barcode in barcode:
         pass
        print(barcode.data)
        data.loc[k,"Barcode Number"]=str(barcode.data).split("'")[1]
        k=k+1 
    for i in range(1,1+int(d[key][1])):
        image=Image.open(f'./{folder_to_save}/{data["Delivery Point"][k]}_Large_{i}.png')
        gray=ImageOps.grayscale(image)
        barcodes = pyzbar.decode(gray)
        for barcode in barcodes:
            pass
        print(barcode.data)
        data.loc[k,"Barcode Number"]=barcode.data 
        k=k+1
 data.to_csv(f"{folder_to_save}_updated.csv", index=False)

