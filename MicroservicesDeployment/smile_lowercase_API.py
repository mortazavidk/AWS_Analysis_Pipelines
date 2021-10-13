from concurrent import futures 

import grpc

from smile_lowercase_pb2 import (
    LowerSmile,
    LowerSmileResponse
)

import smile_lowercase_pb2_grpc
smilelist = [LowerSmile(user_id=1,message="smile1"),LowerSmile(user_id=2,message="smile2")]

class LowrSmileService(smile_lowercase_pb2_grpc.LowrSmilesServicer):
    def lowersmile(self, request, context):
        return LowerSmileResponse(LowerSmiles=smilelist) 

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smile_lowercase_pb2_grpc.add_LowrSmilesServicer_to_server(LowrSmileService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
if __name__ == "__main__":
    serve()