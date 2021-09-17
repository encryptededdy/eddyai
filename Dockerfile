FROM python:3.8
WORKDIR /app
ADD . /app
RUN cp ./gpt2tc /bin
RUN pip install -r requirements.txt
CMD python gpt2bot.py
