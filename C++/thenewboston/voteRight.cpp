#include <iostream>
using namespace std;
int main() {
  unsigned int age;
  cout << "Enter the age: ";
  cin >> age;
  if (age > 18) {
    cout << "You are eligible to vote";
  } else {
    cout << "Go and watch poogo: " << endl;
  }
  return 0;
}