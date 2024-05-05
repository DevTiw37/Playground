#include <iostream>
using namespace std;
int main() {
  int a, b;
  cout << "Enter any two numbers: ";
  cin >> a >> b;
  if (a > b) {
    cout << a << " is greater than " << b << endl;
  } else if (a == b) {
    cout << a << " is equal to " << b << endl;
  } else if (a < b) {
    cout << a << "is lesser than " << b << endl;
  } else {
    cout << "Invalid" << endl;
  }

  return 0;
}