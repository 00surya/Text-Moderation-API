FROM python:3.8-slim
# Use the python latest image
COPY . ./
# Copy the current folder content into the docker image
RUN pip install flask gunicorn detoxify
# Install the required packages of the application
CMD gunicorn --bind :$PORT app:app
# Bind the port and refer to the app.py app