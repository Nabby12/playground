FROM apache/spark-py:latest

ENV SPARK_USER=sparkuser
ENV PYTHONUSERBASE=/app/.local

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

COPY src/app.py .

ENTRYPOINT [ "/opt/spark/bin/spark-submit", "--conf", "spark.jars.ivy=/tmp/.ivy", "--conf", "spark.hadoop.security.authentication=none", "/app/app.py" ]
