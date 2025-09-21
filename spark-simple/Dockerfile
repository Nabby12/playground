FROM apache/spark-py:latest

WORKDIR /app

ENV PATH=/opt/spark/bin:${PATH}

COPY src/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

COPY src/app.py .

CMD [ "spark-submit", "/app/app.py" ]
