from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import pandas as pd
def form1(file,pdf,district,delivery_point,item,category,sub_category,quantity,canvas):
 print(file)
 x_position, y_position = (5, 480) 
 image = ImageReader(fileName=str(file))
 width, height = image.getSize() 
 district=district
 delivery_point=delivery_point
 item=item
 category=category
 sub_category=sub_category
 quantity=quantity
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(5, 800, 'District')
 canvas.drawString(120, 800,":"+district)
 canvas.setFont("Helvetica-Bold",size=15)
 canvas.drawString(5, 750, 'Delivery Point')
 canvas.drawString(120, 750,":"+delivery_point)
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(5, 700, 'Item')
 canvas.drawString(120, 700,":"+item)
 canvas.drawString(5, 650, 'Category')
 canvas.drawString(120,650,":"+category)
 canvas.drawString(5, 600, 'Sub Category')
 canvas.drawString(120,600,":"+sub_category)
 canvas.drawString(5, 550, 'Quantity')
 canvas.drawString(120,550,":"+quantity)
 canvas.drawImage(image, x_position, y_position, width=150, height=60, mask='auto')
def form2(file,pdf,district,delivery_point,item,category,sub_category,quantity,canvas):
 print(file)
 image = ImageReader(fileName=str(file))
 width, height = image.getSize() 
 x_position, y_position = (310, 480) 
 district=district
 delivery_point=delivery_point
 item=item
 category=category
 sub_category=sub_category
 quantity=quantity
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(310, 800, 'District')
 canvas.drawString(430, 800,":"+district)
 canvas.setFont("Helvetica-Bold",size=15)
 canvas.drawString(310, 750, 'Delivery Point')
 canvas.drawString(430, 750,":"+delivery_point)
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(310, 700, 'Item')
 canvas.drawString(430, 700,":"+item)
 canvas.drawString(310, 650, 'Category')
 canvas.drawString(430, 650,":"+category)
 canvas.drawString(310, 600, 'Sub Category')
 canvas.drawString(430, 600,":"+sub_category)
 canvas.drawString(310, 550, 'Quantity')
 canvas.drawString(430, 550,":"+quantity)
 canvas.drawImage(image, x_position, y_position, width=150, height=60, mask='auto')
def form3(file,pdf,district,delivery_point,item,category,sub_category,quantity,canvas):
 print(file)
 image = ImageReader(fileName=str(file))
 width, height = image.getSize() 
 x_position, y_position = (5,110) 
 district=district
 delivery_point=delivery_point
 item=item
 category=category
 sub_category=sub_category
 quantity=quantity
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(5, 430, 'District')
 canvas.drawString(120, 430,":"+district)
 canvas.setFont("Helvetica-Bold",size=15)
 canvas.drawString(5, 380, 'Delivery Point')
 canvas.drawString(120,380,":"+delivery_point)
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(5, 330, 'Item')
 canvas.drawString(120,330,":"+item)
 canvas.drawString(5, 280, 'Category')
 canvas.drawString(120,280,":"+category)
 canvas.drawString(5, 230, 'Sub Category')
 canvas.drawString(120,230,":"+sub_category)
 canvas.drawString(5, 180, 'Quantity')
 canvas.drawString(120,180,":"+quantity)
 canvas.drawImage(image, x_position, y_position, width=150, height=60, mask='auto')
def form4(file,pdf,district,delivery_point,item,category,sub_category,quantity,canvas):
 print(file)
 image = ImageReader(fileName=str(file))
 width, height = image.getSize() 
 x_position, y_position = (310, 110) 
# Draw the text on the canvas
 district=district
 delivery_point=delivery_point
 item=item
 category=category
 sub_category=sub_category
 quantity=quantity
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(310, 430, 'District')
 canvas.drawString(430,430,":"+district)
 canvas.setFont("Helvetica-Bold",size=15)
 canvas.drawString(310, 380, 'Delivery Point')
 canvas.drawString(430, 380,":"+delivery_point)
 canvas.setFont("Helvetica",size=15)
 canvas.drawString(310, 330, 'Item')
 canvas.drawString(430, 330,":"+item)
 canvas.drawString(310, 280, 'Category')
 canvas.drawString(430, 280,":"+category)
 canvas.drawString(310, 230, 'Sub Category')
 canvas.drawString(430, 230,":"+sub_category)
 canvas.drawString(310, 180, 'Quantity')
 canvas.drawString(430, 180,":"+quantity)
 canvas.drawImage(image, x_position, y_position, width=200, height=60, mask='auto')


def pdf_format_maker(data,data_breif,folder_to_save): 
 w,h=A4
 print(w,h)
 data=data
 print(data["District"])
 n=0
 l=[]
 o=0
 d=data_breif
 for key in d.keys():
  print(d.keys())
  print(key)
  o=0
  k=d[key][0]//4
  print("k"+str(k))
  for i in range(1+int(d[key][0]//4)):
    print(1+int(d[key][0]//4))
    print("i="+str(i))
    pdf=f"{folder_to_save}_medium/{key}_Medium{i}.pdf"
    c = canvas.Canvas(pdf,pagesize=A4)
    if(o<k*4):
      for j in range(1,5):
       globals()[f"form{j}"](f"{folder_to_save}/{data['Delivery Point'][n]}_Medium_{o+1}.png",pdf,data["District"][n],data["Delivery Point"][n],data["Item"][n],data["Category"][n],data["Sub Category"][n],str(data["Qty"][n]),c)
       o=o+1
       n=n+1
       print("n="+str(n))
      c.save()
      
    else:
     if(o<=d[key][0]):
      for j in range(1,1+d[key][0]-int(k)*4):
        print(d[key][0]-int(k)*4)
        print(j)
        globals()[f"form{j}"](f'{folder_to_save}/{data["Delivery Point"][n]}_Medium_{o+1}.png',pdf,data["District"][n],data["Delivery Point"][n],data["Item"][n],data["Category"][n],data["Sub Category"][n],str(data["Qty"][n]),c)
        o=o+1
        n=n+1
      c.save()
  o=0
  k=d[key][1]//4
  for i in range(1+int(d[key][1]//4)):
    print(1+int(d[key][1]//4))
    print("i="+str(i))
    pdf=f"{folder_to_save}_large/{key}_Large{i}.pdf"
    c = canvas.Canvas(pdf,pagesize=A4)
    if(o<k*4):
      for j in range(1,5):
       globals()[f"form{j}"](f"{folder_to_save}/{data['Delivery Point'][n]}_Large_{o+1}.png",pdf,data["District"][n],data["Delivery Point"][n],data["Item"][n],data["Category"][n],data["Sub Category"][n],str(data["Qty"][n]),c)
       o=o+1
       n=n+1
       print("n="+str(n))
      c.save()
      
    else:
     if(o<=d[key][1]):
      for j in range(1,1+d[key][1]-int(k)*4):
        print(d[key][0]-int(k)*4)
        print(j)
        globals()[f"form{j}"](f'{folder_to_save}/{data["Delivery Point"][n]}_Large_{o+1}.png',pdf,data["District"][n],data["Delivery Point"][n],data["Item"][n],data["Category"][n],data["Sub Category"][n],str(data["Qty"][n]),c)
        o=o+1
        n=n+1
      c.save()
