#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

int main()
{
  const char* path = std::getenv("LOG_PATH");
  const std::string log_path = path ? path : "log.txt";

  std::ofstream log(log_path, std::ios::app);
  if (!log) {
    std::cerr << "cannot open log file" << std::endl;
    return 1;
  }

  std::string line;
  while (std::getline(std::cin, line)) {
    log << line << std::endl;
  }

  return 0;
}
