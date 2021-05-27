FROM python:3.7

RUN pip3 install django

RUN pip3 install django-cors-headers

RUN pip3 install pymysql

RUN pip install django-debug-toolbar

RUN pip install pillow

WORKDIR /app

COPY . .

CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000
