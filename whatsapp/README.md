Cara menjalankan :

1. Jalankan rest_api/app.py (membuat file antrian ) :
- eksekusi D:\MASTER\whatsappapi\venv\Scripts>activate.bat di command prompt
- pindah current directory ke D:\MASTER\whatsappapi
- eksekusi python rest_api/app.py . Gambaran : (venv) D:\MASTER\whatsappapi>python rest_api/app.py

2. Jalankan worker (mengirim WA) :
- masuk ke D:\MASTER\whatsappapi\worker
- eksekusi: python workerwhatsapp.py

3. Login lewat QR Code di WhatsApp Web yang telah terbuka.

rest_api_demo
=============

This repository contains boilerplate code for a RESTful API based on Flask and Flask-RESTPlus.

The code of this demo app is described in an article on my blog:
http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
