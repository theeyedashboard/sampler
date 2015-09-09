FROM python
RUN pip install Flask
RUN mkdir /sampler
COPY main.py /sampler/
WORKDIR /sampler/
CMD ["python", "main.py"]
EXPOSE 80
