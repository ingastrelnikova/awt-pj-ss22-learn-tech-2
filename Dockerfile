FROM jupyter/scipy-notebook
MAINTAINER jialun<jialun.jiang@campus.tu-berlin.de>
WORKDIR /home/jovyan/work/

# Install Spacy:
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download de_core_news_lg

# Install Tensorflow:
RUN pip install tensorflow==2.9.0
RUN pip install tensorflow_text==2.9.0
RUN pip install tensorflow_hub

# Install Neo4J:
RUN pip install neo4j

# Install RESTful API:
RUN pip install Flask~=2.1.2
RUN pip install flask-restx==0.5.1
RUN pip install werkzeug==2.1.2

# Add Project File:
COPY --chmod=777 ./ /home/jovyan/work/awt-pj-ss22-learn-tech-2

# Expose Port For Jupyter Notebook
EXPOSE 8888

# Expose Port For RESTful API
EXPOSE 5000

