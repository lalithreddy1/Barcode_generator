from barcode import EAN13   
import pandas as pd
from barcode.writer import ImageWriter 
from PIL import Image,ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import pandas as pd
def barcode_generator(data,folder_to_save):
 w,h=A4
 m=0
 l=0
 d={}
 data=data
 print(data["Barcode No."][0])
 print(len(data))
 a=data["Barcode No."].tolist()
 Previous=data["Delivery Point"][0]
 for i in range(len(data)):
    if data["Delivery Point"][i]!=Previous:
        d[Previous]=[m,l]
        Previous=data["Delivery Point"][i]
        m=0
        l=0
    print(str(a[i]))
    my_code=EAN13(str(a[i]),writer=ImageWriter())
    text=my_code.get_fullcode()
    print("text:"+text)
    block=data["Delivery Point"][i]
    my_code=my_code.render(text=f"{text}\n{block}")
    if data["Category"][i]=="Medium":
        m=m+1
        my_code.save(f'./{folder_to_save}/{data["Delivery Point"][i]}_Medium_{m}.png',writer_options={"center_text":True,"text_distance":50})
    else:
        l=l+1
        my_code.save(f'./{folder_to_save}/{data["Delivery Point"][i]}_Large_{l}.png',writer_options={"center_text":True,"text_distance":50})
    d[Previous]=(m,l)
 return d
