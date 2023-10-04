
# build proto files for python files
python -m grpc_tools.protoc -I=. --python_out=./build --grpc_python_out=./build ./env.proto
echo "Python proto files are created"

# build proto files for C++
export PATH=/bigdisk/lax/renaza/env/grpc/.local/bin:$PATH
export LD_LIBRARY_PATH=/bigdisk/lax/renaza/env/grpc/.local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/bigdisk/lax/renaza/env/grpc/.local/lib64:$LD_LIBRARY_PATH
protoc -I=. --cpp_out=./build --grpc_out=./build --plugin=protoc-gen-grpc=$(which grpc_cpp_plugin) ./env.proto
echo "C++ proto files are created"


