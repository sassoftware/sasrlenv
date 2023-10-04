# Prerequirement

## Python
For building the grpc proto files for python, you need to install grpcio-tools using 

`pip install grpcio-tools`

**Note**: After generating the two .py files, we need to change the relative path of env_pb2.py in env_pb2_grpc.py, so the sasrlenv package can find it.

# C++
You need to assign the location to find `protoc` executable: 

`export PATH=/bigdisk/lax/renaza/env/grpc/.local/bin:$PATH`

In this example, we have built grpc from source in a given directory and the `protoc` is under the `.local/bin` directory.
