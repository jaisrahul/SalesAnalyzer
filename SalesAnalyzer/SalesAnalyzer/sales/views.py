from django.shortcuts import render
from .models import *
import pandas as pd
import os
from wsgiref.util import FileWrapper
from django.conf import settings
from django.http.response import StreamingHttpResponse
import mimetypes
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import random
from random import randint



def home(request):
  item = Sales_info.objects.all().values()
  df = pd.DataFrame(item)
  plt.bar(df["CustomerName"],df["TotalAmount"])
  plt.title('Bar Chart')
  plt.xlabel("customer Name")
  plt.ylabel("Total Amount")
  plt.savefig("V.png")
  
  labels = 'Quantity', 'TotalAmount'
  sizes = [random.randint(10,30), random.randint(30,50)]
  explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
          shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.savefig('pieChart.png',dpi=100)
  mydict = {
    'df': df.to_html(),
    # "Name": ax
  }
  return render(request,'index.html', context = mydict)

def downloadfile(request):
  filename = os.path.join(settings.BASE_DIR, 'csvFiles/sales_data.csv')
  thefile = filename
  filename = os.path.basename(thefile)
  chunk_size = 8192
  response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'),chunk_size),
             content_type = mimetypes.guess_type(thefile)[0])
  response['Content-Length'] = os.path.getsize(thefile)
  response['Content-Disposition'] = "Attachment;filename=%s" % filename
  return response   






