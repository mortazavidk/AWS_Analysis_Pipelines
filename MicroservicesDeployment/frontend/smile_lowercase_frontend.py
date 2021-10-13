import os

from flask import Flask, render_template
import grpc

from smile_lowercase_pb2 import LowerSmileRequest
from smile_lowercase_pb2_grpc import LowrSmilesStub

app=Flask (__name__)

_smile_lowercase_host = os.getenv("SMIELOWERCASE_HOST","localhost")
_smile_lowercase_channel = grpc.insecure_channel (f"{_smile_lowercase_host}:50051")
_smile_lowercase_client = LowrSmilesStub(_smile_lowercase_channel)

@app.route("/")
def render_homepage():
    _smile_lowercase_request = LowerSmileRequest (user_id =1)
    _smile_lowercase_response = _smile_lowercase_client.lowersmile(_smile_lowercase_request)
    return render_template(
        "homepage.html",
        lowersmile=_smile_lowercase_response.LowerSmiles
    )
app.run(host='0.0.0.0', port = 5000)    