import grpc
from protos.keymapp_pb2 import SetLayerRequest
from protos.keymapp_pb2_grpc import KeyboardServiceStub

def set_layer(layer: int):
    channel = grpc.insecure_channel("localhost:50051")
    stub = KeyboardServiceStub(channel)
    stub.SetLayer(SetLayerRequest(layer=layer))

if __name__ == "__main__":
    set_layer(1)
