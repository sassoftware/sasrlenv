python_client:
	python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./env.proto
# cd /bigdisk/lax/renaza/env/grpc/tools/distrib/python/grpcio_tools/grpc_tools
# python -m grpc_tools.protoc -I=/u/renaza/dmine8938/sasrlenv/sasrl_env/common/ --python_out=/u/renaza/dmine8938/sasrlenv/sasrl_env/common/ --grpc_python_out=/u/renaza/dmine8938/sasrlenv/sasrl_env/common/ /u/renaza/dmine8938/sasrlenv/sasrl_env/common/env.proto
# Add protoc executable to your PATH
# e.g., export PATH=/bigdisk/lax/renaza/env/grpc/.local/bin:$PATH
cpp_client:
	protoc -I=. --cpp_out=. --grpc_out=. --plugin=protoc-gen-grpc=$(which grpc_cpp_plugin) ./env.proto

