#include <iostream>

#include "make_example.H"
#include "githash.H"

int main() {

  double x, y, z;

  x = 1.0;
  y = 2.0;

  compute(x, y, z);

  print_result(z);

  double radius = 3;
  double area;
  area = cal_area(radius);
  std::cout << "The area of a circle with radius = 3 is "<<area<<std::endl;

  std::cout << "code version " << gitstuff() << std::endl;
}

