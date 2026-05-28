# lab08

Laboratory work VIII: Docker.

This laboratory work is dedicated to deployment automation and application management using Docker.

## Task

The project contains a small C++ logger application. The application reads text from standard input and writes it to a log file. The path to the log file is passed through the `LOG_PATH` environment variable inside the Docker container.

## Project structure

```text
.
├── CMakeLists.txt
├── Dockerfile
├── .travis.yml
└── sources
    └── demo.cpp
