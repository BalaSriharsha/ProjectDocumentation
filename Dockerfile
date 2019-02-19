FROM ubuntu
MAINTAINER BalaSriharsha Cheeday
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install python3-dev
RUN apt -y install python3-pip
RUN apt -y install apache2
RUN apt -y install net-tools
RUN apt -y install vim
RUN apt -y install systemd
RUN apt -y install git
RUN pip3 install sphinx
RUN mkdir webhookk
WORKDIR webhook
COPY ./webhookk/* ./
RUN chmod +x init_install.sh
RUN ./init_install.sh
RUN cp config.json /etc/webhook/webhook.config
WORKDIR ..
RUN mkdir SphinxDocumentation
WORKDIR SphinxDocumentation
COPY . .
RUN python3 shell.py
RUN echo "ServerName 0.0.0.0" >> /etc/apache2/apache2.conf
CMD ["apache2ctl","-D","FOREGROUND"]