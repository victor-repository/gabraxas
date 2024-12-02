FROM python:3

WORKDIR /app

COPY /app .
RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 5000

CMD [ "python3", "./app.py" ]
