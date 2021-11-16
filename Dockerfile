FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
COPY ./tokenizer.json /tokenizer.json
COPY ./finalized_model.sav /finalized_model.sav

RUN python3 -m nltk.downloader rslp
RUN python3 -m nltk.downloader stopwords

CMD python3 ./app/main.py
