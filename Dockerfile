FROM python:3.8.2
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
COPY ./__temp_app__ /__temp_app__
COPY ./db /db
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]