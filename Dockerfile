FROM python:3.11

# 
COPY ./requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV MY_VARIABLE_1 "FastAPI"
ENV MY_VARIABLE_2 "Dockerrr"

# 
COPY . .

EXPOSE 8000

# 
CMD ["uvicorn", "main:app"]