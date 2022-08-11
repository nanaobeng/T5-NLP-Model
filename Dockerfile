# 
FROM python:3.10

# 
WORKDIR /code


COPY ./  /code

RUN pip install poetry


RUN poetry config virtualenvs.create false \
    && poetry install

# 


# 
CMD ["python","main.py"]
