# sasrl-env

## Overview
This package is used for communicating with a remote python environment of SAS customers. It uses the google remote procedure call (gRPC) to provide a fast communication.   

### Installation
The sasrl-env package needs to be installed using the following command:
  - pip install sasrl-env

### Starting an environment server
In the python environment, the installed package needs to be imported and started using the following lines of codes:
  - from sasrl_env import runServer
  - runServer.start(#PORT_NUMBER)

**Notes**: 
- If you do not specify a port when running the server, the environment controller will assign an available port automatically.
- If the specified port is not free, it will increment the port numbers until finding the first available port.
## Contributing
We welcome your contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit contributions to this project.

## License
This project is licensed under the [Apache 2.0 License](LICENSE).

## Supported version:
* protoc 3.13.0
* grpc 1.34.1

## Additional Resources
* Documentation links
* Blog posts
* SAS Communities
