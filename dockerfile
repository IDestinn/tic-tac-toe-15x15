FROM python:3.10

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "run.py"]

# Команды для создания image-а:
# docker build -t tic-tac-toe .

# Для запуска контейнера используйте следующую команду
# docker run -it --rm tic-tac-toe