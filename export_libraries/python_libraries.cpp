#include "python_libraries.hpp"

namespace PythonLibraries {

double sqrt(double x) { return std::sqrt(x); }
float sqrt(float x) { return std::sqrt(x); }
int sqrt(int x) { return (int)std::sqrt((double)x); }

double sin(double x) { return std::sin(x); }
float sin(float x) { return std::sin(x); }
int sin(int x) { return (int)std::sin((double)x); }

double cos(double x) { return std::cos(x); }
float cos(float x) { return std::cos(x); }
int cos(int x) { return (int)std::cos((double)x); }

double tan(double x) { return std::tan(x); }
float tan(float x) { return std::tan(x); }
int tan(int x) { return (int)std::tan((double)x); }

} // namespace PythonLibraries
