FROM python

RUN mkdir /service
COPY ./requirements.txt /service/
COPY ./smile_lowercase.proto /service/
COPY ./smile_lowercase_frontend.py /service/
COPY ./templates/ /service/templates/
WORKDIR /service

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I . --python_out=. \
              --grpc_python_out=. ./smile_lowercase.proto
EXPOSE 5000
ENV FLASK_APP=smile_lowercase_frontend.py
ENTRYPOINT ["flask","run","--host=0.0.0.0"]              