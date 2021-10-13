FROM python

RUN mkdir /service
COPY ./requirements.txt /service/
COPY ./smile_lowercase.proto /service/
COPY ./smile_lowercase_API.py /service/
WORKDIR /service

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I . --python_out=. \
              --grpc_python_out=. ./smile_lowercase.proto
EXPOSE 50051
ENTRYPOINT ["python","smile_lowercase_API.py"]              