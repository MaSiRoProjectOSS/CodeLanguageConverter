When you convert Python list to C++ code, you must use vector library.
The vector library is included from <vector>. You do not write "#include <vector>". I will write it after you write the code.

For example, Python list
```
arr = [1.0, 2.0, 3.0]
```
must be converted to
```
double arr[] = {1.0, 2.0, 3.0};
std::vector<double> v(arr, arr + sizeof(arr) / sizeof(double));
```
