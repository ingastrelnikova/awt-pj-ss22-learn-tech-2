# SS22 Project Advanced Web Technologies 
## Learning Technologies - Competence Extraction via ML / NLP
<img width="300" alt="TUB" src="https://user-images.githubusercontent.com/24925361/178028367-d6106e60-664a-41d7-940f-46c9e59ed870.png"> <img width="382" alt="FOKUS" src="https://user-images.githubusercontent.com/24925361/178028417-3c6a1740-cf41-4a98-8f3f-735cbfbd9b0b.png">

## Project Architecture
![image](https://user-images.githubusercontent.com/24925361/181214266-02faef6f-4692-45ec-bf81-4c2641c5e483.png)

## Installation
The project is based on [Anaconda environment](https://www.anaconda.com/)
and some additional installations are also required:

**Spacy:**
```shell
conda install -c conda-forge spacy
python -m spacy download de_core_news_lg
```

**Tensorflow:**
```shell
pip install tensorflow==2.9.0
pip install tensorflow_text==2.9.0
pip install tensorflow_hub
```

Or you can use our packaged docker image:


## Core Components:
* [Data Preprocessing](./src/Preprocessing.ipynb)
* [Competence Extraction (NLP)](./src/NLP.ipynb)
* [Database Access](./src/Neo4J.ipynb)
* [RESTful API](./src/app.py)

## Helpful Links:
* [Miroboard](https://miro.com/app/board/uXjVO4rE3z4=/)
* [EU-ESCO (Multilingual classification of European Skills, Competences)](https://esco.ec.europa.eu/en)
* [Weiterbildungsdatenbank Berlin/Brandenburg search portal](https://www.wdb-suchportal.de/de)
* [Download link for course description](https://webspace.fokus.fraunhofer.de/index.php/s/4g7isDScGgJFmyK)
* [First Presentation](https://docs.google.com/presentation/d/1Khsn_8M1RbjfMqUFCwPy9wX0nEmaIjShYJDiTsIkKAM/edit#slide=id.g122c239953c_2_10)
* [Second Presentation](https://docs.google.com/presentation/d/1qBtznjY1o8PyaYzvs-UPRpJHfz8Td3pSIfjiIBseZYs/edit#slide=id.g122c239953c_2_16)
* [Third Presentation](https://docs.google.com/presentation/d/10RYty7uy4iDyFTbF-Z_PJPTfI8WNRnBT98rpj2WZr0M/edit#slide=id.g12f87666f53_0_0)
* [Content Documentation](https://docs.google.com/document/d/1mfp5A2DEiTcGTzrYrh6c9gaYeMAisS2vuYwDd_1vQfo/edit?usp=sharing)

## Meeting 29.04.2022
* Get to know each other
* Get an overview about the problem

## Meeting 03.05.2022
* Figure out a possible solution
* Talk about the Miroboard of Jialun
* Neo4J as a graph database

Task: 
* distribution for the first presentation
* Stefan: Introduction and problem statement
* Jialun: Paper Review
* Inga: Potential solution, schedule, next steps

## Meeting 05.05.2022
* Finalizing the presentation

## Meeting 08.05.2022
* Recording of the presentation
Tasks:
* Stefan: Upload presentation and recording

## Meeting 17.05.2022
* Debriefing of the workshop
* Task Distribution
*   -> See Issues

## Meeting 24.05.2022
* Disscussion of problems:
*  -> Display of Umlaute (ä,ö,ü) in XML and CSV files
* Upload of compentecies and course descriptions to the db works
* We have to find a way to connect the nodes
