#include <iostream>
using namespace std;
int main() {
  int time;
  cout << "Enter the hour (24hr)";
  cin >> time;
  if (time >= 5 && time <= 11) {
    cout << "Good Morning!" << endl;
  } else if (time >= 12 && time <= 16) {
    cout << "Good Afternoon!" << endl;
  } else if (time >= 17 && time <= 24) {
    cout << "Good Evening!" << endl;
  } else if (time >= 1 && time <= 4) {
    cout << "Good Night!" << endl;
  }

  return 0;
}