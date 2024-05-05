// This program uses ternary operator

#include <iostream>
using namespace std;
int main() {
  int num1, num2;
  cout << "Enter two numbers: ";
  cin >> num1 >> num2;
  int great = (num1 > num2 ? num1 : num2);
  cout << "The greatest number is " << great << endl;
  return 0;
}