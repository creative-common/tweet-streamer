FROM python:3

WORKDIR /home/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /home/app/start.sh
RUN /home/app/start.sh

FROM python:3

WORKDIR /home/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /home/app/start.sh
RUN /home/app/start.sh

FROM python:3

WORKDIR /home/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /home/app/start.sh
RUN /home/app/start.sh

FROM python:3

WORKDIR /home/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /home/app/start.sh
RUN /home/app/start.sh

FROM python:3

WORKDIR /home/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /home/app/start.sh
RUN /home/app/start.sh

