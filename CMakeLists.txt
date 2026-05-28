cmake_minimum_required(VERSION 3.4)
project(demo)

add_executable(demo sources/demo.cpp)
install(TARGETS demo RUNTIME DESTINATION bin)
