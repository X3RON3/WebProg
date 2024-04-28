FROM python:3.12.3

RUN mkdir mysite
WORKDIR /mysite

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY mysite/ .

EXPOSE 5000

CMD ["python" ,"manage.py", "runserver", "0.0.0.0:5000"]