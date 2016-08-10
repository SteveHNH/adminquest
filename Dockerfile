FROM fedora:latest
MAINTAINER tsadams@gmail.com
RUN dnf install -y python git && dnf clean all
RUN git clone https://www.github.com/stevehnh/adminquest.git && cd adminquest/adminquest
ENTRYPOINT ["/usr/bin/python", "adminquest/adminquest/launch.py"]
