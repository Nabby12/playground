FROM apache/spark-py:latest

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

COPY src/app.py .

CMD [ "/opt/spark/bin/spark-submit", "/app/app.py" ]
