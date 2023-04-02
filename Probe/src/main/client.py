from service_methods.grpc_bin import survey6_pb2_grpc
from service_methods.grpc_bin import survey6_pb2
import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import time
import grpc

def run():
    with grpc.insecure_channel('localhost:32001') as channel:
        stub = survey6_pb2_grpc.ClientConnectionStub(channel)
        t = datetime.datetime.now().timestamp()
        seconds = int(t)
        nanos = int(t % 1 * 1e9)
        proto_timestamp = Timestamp(seconds=seconds, nanos=nanos)
        heartbeat_request = survey6_pb2.HeartbeatSender(request_epoch_time = proto_timestamp, host_name="Viraj")
        heartbeat_reply = stub.Heartbeat(heartbeat_request)
        print("Heartbeat ack status: ")
        print(heartbeat_reply)

if __name__ == "__main__":
    run()