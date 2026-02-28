FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV VERSION=dev
EXPOSE 8080

USER 1001
CMD ["python", "app.py"]
