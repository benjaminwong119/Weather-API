FROM python:3.9 
RUN pip install requests 
RUN pip install pandas
COPY main.py . 
ENTRYPOINT ["python", "main.py"]