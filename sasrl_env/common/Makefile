python_client:
	python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./env.proto

# Add protoc executable to your PATH
# e.g., export PATH=/bigdisk/lax/rl/grpc/.local/bin:$PATH
cpp_client:
	protoc -I=. --cpp_out=. --grpc_out=. --plugin=protoc-gen-grpc=$(which grpc_cpp_plugin) ./env.proto

