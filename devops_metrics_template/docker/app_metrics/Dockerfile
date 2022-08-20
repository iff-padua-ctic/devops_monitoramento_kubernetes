FROM python:3.9.13-slim-bullseye

RUN  apt-get clean -y &&  apt-get update -y &&   apt-get upgrade -y &&  apt-get install -y locales


#Timezone
RUN apt-get install tzdata
ENV TZ=America/Sao_Paulo
RUN echo $TZ | tee /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

#seta o locale para pt_br
RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8


####################  app  ######################
WORKDIR /app

COPY ./custom_files/metrics.py ./
COPY ./custom_files/requirements.txt  ./
COPY ./custom_files/init.sh  ./

RUN python -m pip install --upgrade pip
RUN python -m pip install -U --no-cache-dir -r  requirements.txt
RUN mkdir -p /home/work_dir && chmod -R 777 /home/work_dir
RUN chmod 777  init.sh


ENTRYPOINT [ "/app/init.sh" ]



#docker build -t iffpadua/metrics:1.1 .