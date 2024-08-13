#ifndef PYTHON_MATH_HPP
#define PYTHON_MATH_HPP

#include <cmath>
#include <vector>

namespace PythonMath {

/* abs */
double abs(double x);
std::vector<double> abs(std::vector<double> x);
float abs(float x);
std::vector<float> abs(std::vector<float> x);
int abs(int x);
std::vector<int> abs(std::vector<int> x);

/* fmod */
double fmod(double x, double y);
std::vector<double> fmod(std::vector<double> x, double y);
float fmod(float x, float y);
std::vector<float> fmod(std::vector<float> x, float y);
int fmod(int x, int y);
std::vector<int> fmod(std::vector<int> x, int y);

/* sqrt */
double sqrt(double x);
std::vector<double> sqrt(std::vector<double> x);
float sqrt(float x);
std::vector<float> sqrt(std::vector<float> x);
int sqrt(int x);
std::vector<int> sqrt(std::vector<int> x);

/* exp */
double exp(double x);
std::vector<double> exp(std::vector<double> x);
float exp(float x);
std::vector<float> exp(std::vector<float> x);
int exp(int x);
std::vector<int> exp(std::vector<int> x);

/* log */
double log(double x);
std::vector<double> log(std::vector<double> x);
float log(float x);
std::vector<float> log(std::vector<float> x);
int log(int x);
std::vector<int> log(std::vector<int> x);

/* log10 */
double log10(double x);
std::vector<double> log10(std::vector<double> x);
float log10(float x);
std::vector<float> log10(std::vector<float> x);
int log10(int x);
std::vector<int> log10(std::vector<int> x);

/* pow */
double pow(double x, double y);
std::vector<double> pow(std::vector<double> x, double y);
float pow(float x, float y);
std::vector<float> pow(std::vector<float> x, float y);
int pow(int x, int y);
std::vector<int> pow(std::vector<int> x, int y);

/* sin */
double sin(double x);
std::vector<double> sin(std::vector<double> x);
float sin(float x);
std::vector<float> sin(std::vector<float> x);
int sin(int x);
std::vector<int> sin(std::vector<int> x);

/* cos */
double cos(double x);
std::vector<double> cos(std::vector<double> x);
float cos(float x);
std::vector<float> cos(std::vector<float> x);
int cos(int x);
std::vector<int> cos(std::vector<int> x);

/* tan */
double tan(double x);
std::vector<double> tan(std::vector<double> x);
float tan(float x);
std::vector<float> tan(std::vector<float> x);
int tan(int x);
std::vector<int> tan(std::vector<int> x);

/* asin */
double asin(double x);
std::vector<double> asin(std::vector<double> x);
float asin(float x);
std::vector<float> asin(std::vector<float> x);
int asin(int x);
std::vector<int> asin(std::vector<int> x);

/* acos */
double acos(double x);
std::vector<double> acos(std::vector<double> x);
float acos(float x);
std::vector<float> acos(std::vector<float> x);
int acos(int x);
std::vector<int> acos(std::vector<int> x);

/* atan */
double atan(double x);
std::vector<double> atan(std::vector<double> x);
float atan(float x);
std::vector<float> atan(std::vector<float> x);
int atan(int x);
std::vector<int> atan(std::vector<int> x);

/* atan2 */
double atan2(double y, double x);
std::vector<double> atan2(std::vector<double> y, std::vector<double> x);
float atan2(float y, float x);
std::vector<float> atan2(std::vector<float> y, std::vector<float> x);
int atan2(int y, int x);
std::vector<int> atan2(std::vector<int> y, std::vector<int> x);

/* sinh */
double sinh(double x);
std::vector<double> sinh(std::vector<double> x);
float sinh(float x);
std::vector<float> sinh(std::vector<float> x);
int sinh(int x);
std::vector<int> sinh(std::vector<int> x);

/* cosh */
double cosh(double x);
std::vector<double> cosh(std::vector<double> x);
float cosh(float x);
std::vector<float> cosh(std::vector<float> x);
int cosh(int x);
std::vector<int> cosh(std::vector<int> x);

/* tanh */
double tanh(double x);
std::vector<double> tanh(std::vector<double> x);
float tanh(float x);
std::vector<float> tanh(std::vector<float> x);
int tanh(int x);
std::vector<int> tanh(std::vector<int> x);

} // namespace PythonMath

#endif // PYTHON_MATH_HPP
