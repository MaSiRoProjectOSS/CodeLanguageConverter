#include "python_math.hpp"

namespace PythonMath {

/* abs */
double abs(double x) { return std::abs(x); }

std::vector<double> abs(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::abs(x[i]);
  }
  return result;
}

float abs(float x) { return std::abs(x); }

std::vector<float> abs(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::abs(x[i]);
  }
  return result;
}

int abs(int x) { return std::abs(x); }

std::vector<int> abs(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::abs(x[i]);
  }
  return result;
}

/* fmod */
double fmod(double x, double y) { return std::fmod(x, y); }

std::vector<double> fmod(std::vector<double> x, double y) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::fmod(x[i], y);
  }
  return result;
}

float fmod(float x, float y) { return std::fmod(x, y); }

std::vector<float> fmod(std::vector<float> x, float y) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::fmod(x[i], y);
  }
  return result;
}

int fmod(int x, int y) { return (int)std::fmod((double)x, (double)y); }

std::vector<int> fmod(std::vector<int> x, int y) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::fmod((double)x[i], (double)y);
  }
  return result;
}

/* sqrt */
double sqrt(double x) { return std::sqrt(x); }

std::vector<double> sqrt(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::sqrt(x[i]);
  }
  return result;
}

float sqrt(float x) { return std::sqrt(x); }

std::vector<float> sqrt(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::sqrt(x[i]);
  }
  return result;
}

int sqrt(int x) { return (int)std::sqrt((double)x); }

std::vector<int> sqrt(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::sqrt((double)x[i]);
  }
  return result;
}

/* exp */
double exp(double x) { return std::exp(x); }

std::vector<double> exp(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::exp(x[i]);
  }
  return result;
}

float exp(float x) { return std::exp(x); }

std::vector<float> exp(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::exp(x[i]);
  }
  return result;
}

int exp(int x) { return (int)std::exp((double)x); }

std::vector<int> exp(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::exp((double)x[i]);
  }
  return result;
}

/* log */
double log(double x) { return std::log(x); }

std::vector<double> log(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::log(x[i]);
  }
  return result;
}

float log(float x) { return std::log(x); }

std::vector<float> log(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::log(x[i]);
  }
  return result;
}

int log(int x) { return (int)std::log((double)x); }

std::vector<int> log(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::log((double)x[i]);
  }
  return result;
}

/* log10 */
double log10(double x) { return std::log10(x); }

std::vector<double> log10(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::log10(x[i]);
  }
  return result;
}

float log10(float x) { return std::log10(x); }

std::vector<float> log10(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::log10(x[i]);
  }
  return result;
}

int log10(int x) { return (int)std::log10((double)x); }

std::vector<int> log10(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::log10((double)x[i]);
  }
  return result;
}

/* pow */
double pow(double x, double y) { return std::pow(x, y); }

std::vector<double> pow(std::vector<double> x, double y) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::pow(x[i], y);
  }
  return result;
}

float pow(float x, float y) { return std::pow(x, y); }

std::vector<float> pow(std::vector<float> x, float y) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::pow(x[i], y);
  }
  return result;
}

int pow(int x, int y) { return (int)std::pow((double)x, (double)y); }

std::vector<int> pow(std::vector<int> x, int y) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::pow((double)x[i], (double)y);
  }
  return result;
}

/* sin */
double sin(double x) { return std::sin(x); }

std::vector<double> sin(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::sin(x[i]);
  }
  return result;
}

float sin(float x) { return std::sin(x); }

std::vector<float> sin(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::sin(x[i]);
  }
  return result;
}

int sin(int x) { return (int)std::sin((double)x); }

std::vector<int> sin(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::sin((double)x[i]);
  }
  return result;
}

/* cos */
double cos(double x) { return std::cos(x); }

std::vector<double> cos(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::cos(x[i]);
  }
  return result;
}

float cos(float x) { return std::cos(x); }

std::vector<float> cos(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::cos(x[i]);
  }
  return result;
}

int cos(int x) { return (int)std::cos((double)x); }

std::vector<int> cos(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::cos((double)x[i]);
  }
  return result;
}

/* tan */
double tan(double x) { return std::tan(x); }

std::vector<double> tan(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::tan(x[i]);
  }
  return result;
}

float tan(float x) { return std::tan(x); }

std::vector<float> tan(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::tan(x[i]);
  }
  return result;
}

int tan(int x) { return (int)std::tan((double)x); }

std::vector<int> tan(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::tan((double)x[i]);
  }
  return result;
}

/* asin */
double asin(double x) { return std::asin(x); }

std::vector<double> asin(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::asin(x[i]);
  }
  return result;
}

float asin(float x) { return std::asin(x); }

std::vector<float> asin(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::asin(x[i]);
  }
  return result;
}

int asin(int x) { return (int)std::asin((double)x); }

std::vector<int> asin(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::asin((double)x[i]);
  }
  return result;
}

/* acos */
double acos(double x) { return std::acos(x); }

std::vector<double> acos(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::acos(x[i]);
  }
  return result;
}

float acos(float x) { return std::acos(x); }

std::vector<float> acos(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::acos(x[i]);
  }
  return result;
}

int acos(int x) { return (int)std::acos((double)x); }

std::vector<int> acos(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::acos((double)x[i]);
  }
  return result;
}

/* atan */
double atan(double x) { return std::atan(x); }

std::vector<double> atan(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::atan(x[i]);
  }
  return result;
}

float atan(float x) { return std::atan(x); }

std::vector<float> atan(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::atan(x[i]);
  }
  return result;
}

int atan(int x) { return (int)std::atan((double)x); }

std::vector<int> atan(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::atan((double)x[i]);
  }
  return result;
}

/* atan2 */
double atan2(double y, double x) { return std::atan2(y, x); }

std::vector<double> atan2(std::vector<double> y, std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::atan2(y[i], x[i]);
  }
  return result;
}

float atan2(float y, float x) { return std::atan2(y, x); }

std::vector<float> atan2(std::vector<float> y, std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::atan2(y[i], x[i]);
  }
  return result;
}

int atan2(int y, int x) { return (int)std::atan2((double)y, (double)x); }

std::vector<int> atan2(std::vector<int> y, std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::atan2((double)y[i], (double)x[i]);
  }
  return result;
}

/* sinh */
double sinh(double x) { return std::sinh(x); }

std::vector<double> sinh(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::sinh(x[i]);
  }
  return result;
}

float sinh(float x) { return std::sinh(x); }

std::vector<float> sinh(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::sinh(x[i]);
  }
  return result;
}

int sinh(int x) { return (int)std::sinh((double)x); }

std::vector<int> sinh(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::sinh((double)x[i]);
  }
  return result;
}

/* cosh */
double cosh(double x) { return std::cosh(x); }

std::vector<double> cosh(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::cosh(x[i]);
  }
  return result;
}

float cosh(float x) { return std::cosh(x); }

std::vector<float> cosh(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::cosh(x[i]);
  }
  return result;
}

int cosh(int x) { return (int)std::cosh((double)x); }

std::vector<int> cosh(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::cosh((double)x[i]);
  }
  return result;
}

/* tanh */
double tanh(double x) { return std::tanh(x); }

std::vector<double> tanh(std::vector<double> x) {
  std::vector<double> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::tanh(x[i]);
  }
  return result;
}

float tanh(float x) { return std::tanh(x); }

std::vector<float> tanh(std::vector<float> x) {
  std::vector<float> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = std::tanh(x[i]);
  }
  return result;
}

int tanh(int x) { return (int)std::tanh((double)x); }

std::vector<int> tanh(std::vector<int> x) {
  std::vector<int> result(x.size());
  for (int i = 0; i < x.size(); i++) {
    result[i] = (int)std::tanh((double)x[i]);
  }
  return result;
}

} // namespace PythonMath
