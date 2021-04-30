# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

''' Install Remote Environment Using GRPC '''
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sasrl-env",
    version="1.0.0",
    author="SAS",
    author_email='support@sas.com',
    license='Apache 2.0',
    description="Generate protobuf files in python and C++ to be used for remote access to RL environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.sas.com/RezaNazari/rlenv_grpc.git",
    packages=setuptools.find_packages(),
    install_requires=['grpcio','protobuf','gym'],
    classifiers=["Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
