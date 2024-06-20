# llamaindex

### Installation guide

1 - create your python environment:
    ```
    python3 -m venv venv
    ```

2 - switch to your python env
    ```
    source venv/bin/activate #mac/linux
    venv/Scripts/activate #windows
    ```

3 - install requirements
    ```
    pip3 install -r requirements.txt
    ```

4 - create your .env file with the OPENAI_API_KEY (as in the .env example)

5 - create a data/ directory where you upload your pdf file

6 - run the script with `python3 rag.py`