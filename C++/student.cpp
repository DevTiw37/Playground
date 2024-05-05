// Experiment 1
/* WAP to creat a class student with data members name, branch and marks of 5 subjects and member functions input(), calculate() and output(). */
// Print the total and percentage of students marks.

#include <iostream>
using namespace std;
class student
{
private:
    char name[20], branch[20];
    int BCE, BME, BCEM, Phy, Maths;
    float per, total;

public:
    void input();
    void compute();
    void output();
    void result();
};
void student::input()
{
    cout << "\nEnter the name of the student : ";
    cin >> name;
    cout << "Enter the Branch : ";
    cin >> branch;
    cout << "Enter marks of BCE, BME, BCEM, Physics and Mathematics : ";
    cin >> BCE >> BME >> BCEM >> Phy >> Maths;
}
void student::compute()
{
    total = BCE + BME + BCEM + Phy + Maths;
    per = (total / 500) * 100;
}

void student::output()
{
    cout << "\n The name of the student is : " << name;
    cout << "\n Branch of the student is : " << branch << endl;
    cout << "\n Marks in BCE = " << BCE;
    cout << "\n Marks in BME = " << BME;
    cout << "\n Marks in BCEM = " << BCEM;
    cout << "\n Marks in Physics = " << Phy;
    cout << "\n Marks in Mathematics = " << Maths << endl;
    cout << "\n Total marks = " << total;
    cout << "\n Total Percentage = " << per << "%" << endl;
    if (BCE < 20)
    {
        cout << " Result = Fail, better luck next time.";
    }
    else if (BME < 20)
    {
        cout << " Result = Fail, better luck next time.";
    }
    else if (BCEM < 20)
    {
        cout << " Result = Fail, better luck next time.";
    }
    else if (Phy < 20)
    {
        cout << " Result = Fail, better luck next time.";
    }
    else if (Maths < 20)
    {
        cout << " Result = Fail, better luck next time.";
    }
    else
    {
        cout << " Result = Pass, Congratulations!";
    }
}

int main()
{
    student s1;
    s1.input();
    s1.compute();
    s1.output();
    return 0;
}
