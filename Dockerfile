FROM texlive/texlive
RUN apt-get update && apt-get -y install python3-pip
RUN pip3 install tox

