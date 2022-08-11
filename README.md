## T5Model
The model entails a text-to-text framework enabling multiple relevant uses cases including machine translation, document summarization, question answering, and classification tasks (e.g., sentiment analysis). 

*Reference : https://huggingface.co/t5-base

# Repo
- This repo primarily focuses on the implementation of text translation component of the the T5 model



## Setup and run docker image
- clone repository
- docker build -t <imagename> -f Dockerfile . 
- docker run --name <imagename> -p 8000:8000 <imagename>

