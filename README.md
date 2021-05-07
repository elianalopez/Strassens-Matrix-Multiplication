# Strassens-Matrix-Multiplication

## Tools Utilized

* VSCode
* Python 3.8.5

### Python Libraries

* NumPy

## Installation 

```
pip3 install numpy
```

## Strassen's Method
The purpose of Strassen’s method is to reduce the number of recursive calls within matrix multiplication to 7. Strassen’s divide matrices to sub-matrices of size N/2 x N/2. Down below we see 7 submatrices (p1,p2,...,p7) the size of N/2 x N/2.

```python
    p1 = s1 * a11
    p2 = s2 * b22
    p3 = s3 * b11
    p4 = s4 * a22
    p5 = s5 * s6
    p6 = s7 * s8
    p7 = s9 * s10
```
