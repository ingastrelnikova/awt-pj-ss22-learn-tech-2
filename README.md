# SS22 Project Advanced Web Technologies 
## Learning Technologies - Competence Extraction via ML / NLP
<img width="300" alt="TUB" src="https://user-images.githubusercontent.com/24925361/178028367-d6106e60-664a-41d7-940f-46c9e59ed870.png"> <img width="382" alt="FOKUS" src="https://user-images.githubusercontent.com/24925361/178028417-3c6a1740-cf41-4a98-8f3f-735cbfbd9b0b.png">

## Project Architecture
![image](https://user-images.githubusercontent.com/24925361/181214266-02faef6f-4692-45ec-bf81-4c2641c5e483.png)


## Installation (Recommended for ```x86``` Platform)

1. Install Docker according to the instructions on the [Docker website](https://docs.docker.com/get-docker/)

1. Open the terminal and enter:
    ```shell
    sudo docker -v
    ```
    Check if Docker is installed successfully, if not retry the previous step.

1. Unzip ```awt-pj-ss22-learn-tech-2.zip``` and go to the project directory ```/awt-pj-ss22-learn-tech-2```

    Type the following command to build the Docker image from the Dockerfile:
    ```shell
    sudo DOCKER_BUILDKIT=1 docker build -t competence-extraction:1.0 ./
    ```
    All dependencies will be downloaded automatically, which will last for a while.

1. Type the following command and you will see the ```competence-extraction``` image you just built:
    ```shell
    sudo docker images
    ```
    
1. Enter the following command to start a container from this image on port 8080 for Jupyter Notebook and port 5000 for RESTful API:
    ```shell
    sudo docker run --user root -p 8888:8888 -p 5000:5000 competence-extraction:1.0
    ```
    You may need to change port if it is ocuppied. For example, using:
    ```shell
    sudo docker run --user root -p 8888:8888 -p 5001:5000 competence-extraction:1.0
    ```
    or
    ```shell
    sudo docker run --user root -p 8889:8888 -p 5000:5000 competence-extraction:1.0
    ```

1. Use a browser to open the last link given on the terminal so that you can access the source code. 

    **!!! Please save this link for future use !!!**
    
    **All existing datasets have been processed, so you can skip this step and directly view the results using the RESTful API in the next step.** 
    or follow the [intructions](#code) if you want to run the source code. 


1. Use ```Ctrl+C``` (key combinations on the keyboard) to exit the Jupyter Notebook environment, enter
    ```shell
    sudo docker ps -a
    ```
    to find the container that just created and already run the Jupyter Notebook, remember the ```<CONTAINER ID>``` this container.

1. Start the container container again:
    ```shell
    sudo docker start <CONTAINER ID>
    ```

1. Use
    ```shell
    sudo docker exec -it <CONTAINER ID> bash 
    ```
    to enter the terminal of the container

1. Enter
    ```shell
    sudo python awt-pj-ss22-learn-tech-2/src/app.py 
    ```
    to run the RESTful API, and open the first link according to the information on the terminal in the browser.

1. Use ```Ctrl+C``` (key combinations on the keyboard) to close the RESTful API.

1. You can also use the same link (the one you should save) to start Jupyter Notebook again.

1. Finally, enter 
    ```shell
    exit
    ```
    to exit container.

## Installation (Recommended for ```ARM/M1``` Platform)

1. Install [Anaconda environment](https://www.anaconda.com/) first.

1. Download and install [Conda env](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh) for M1
     ```shell
    chmod +x ~/Downloads/Miniforge3-MacOSX-arm64.sh
    sh ~/Downloads/Miniforge3-MacOSX-arm64.sh
    source ~/miniforge3/bin/activate
    ```

1. Some additional installations are also required:

    **Spacy:**
    ```shell
    conda install -c conda-forge spacy
    python -m spacy download de_core_news_lg
    ```

    **Tensorflow:**
    
    Download [tensorflow_text](https://github.com/sun1638650145/Libraries-and-Extensions-for-TensorFlow-for-Apple-Silicon/releases/download/v2.9/tensorflow_text-2.9.0-cp39-cp39-macosx_11_0_arm64.whl)
    ```shell
    conda install -c apple tensorflow-deps
    python -m pip install tensorflow-macos
    python -m pip install tensorflow-metal
    python -m pip install Downloads/tensorflow_text-2.9.0-cp39-cp39-macosx_11_0_arm64.whl
    python -m pip install tensorflow_hub
    ```

    **Neo4J:**
    ```shell
    pip install neo4j
    ```

    **RESTful API:**
    ```shell
    pip install Flask~=2.1.2
    pip install flask-restx==0.5.1
    pip install werkzeug==2.1.2
    ```

    **Jupyter Notebook:**
    ```shell
    conda install -c conda-forge jupyter jupyterlab -y
    ```
    
    **Pandas:**
    ```shell
    conda install pandas
    ```

1. **Use Jupyter Notebook to run source code:**
    ```shell
    cd Downloads/awt-pj-ss22-learn-tech-2/src
    jupyter notebook
    ``` 

    **All existing datasets have been processed, so you can skip this step and directly view the results using the RESTful API in the next step.**

    <span id="code"> In case </span> if you want to test the source code or you have new dataset, there are three different Jupyter Notebooks under the ```src/``` path. You can find a detailed description of them in [AWT_Report_IEEE.pdf](./AWT_Report_IEEE.pdf).
    Here are a few points to highlight:

    * Run each block of code in the Jupyter Notebook in the order of ```Preprocessing.ipynb``` -> ```NLP.ipynb``` -> ```Neo4J.ipynb```, you can see all the intermediate steps.
    * When importing the libraries, if there is an alarm message, it's just because the GPU is not configured for acceleration, which does not affect normal use.
    * By default the control course dataset is used (the input value of the ```import_course``` function in ```Preprocessing.ipynb```, it will take more than an hour to use the full course dataset), if you want to test other datasets, please replace the input parameters of the ```import_course``` function.
    * In ```Neo4J.ipynb```, due to the security settings of the cloud database we use, all local computing data cannot be directly imported into the database. It needs to be uploaded to a publicly accessible HTTP or HTTPS server first. It is recommended to use google drive and create a sharing link. The ```get_google_file``` function in ```Neo4J.ipynb``` will extract the address of the direct access data file from it and upload it to the cloud database.
    * You can also use your own cloud database by replacing ```uri``` ```user``` ```password``` in ```Neo4J.ipynb``` or your own network drive, and upload to the cloud database using a similar method.
    * ```Evaluation.ipynb``` under  ```src/archive```  is only used as a potential evaluation tool and is not actually used.

1. Use ```Ctrl+C``` (key combinations on the keyboard) to exit the Jupyter Notebook environment, enter
    ```shell
    flask run --port=5001
    ```
    to run the RESTful API, and open the first link according to the information on the terminal in the browser.

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
