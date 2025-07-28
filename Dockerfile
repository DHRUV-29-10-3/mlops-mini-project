# base image 
FROM python:3.10

# set the working directory
WORKDIR /app

# copy the file into /app 
COPY  flask_app/ /app/
COPY  models/vectorizer.pkl /app/models/vectorizer.pkl

# copy the requirements file 
RUN pip install  -r requirements.txt
RUN python -m nltk.downloader stopwords wordnet

# expose the port 
EXPOSE 5000

# command to run the app 
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
