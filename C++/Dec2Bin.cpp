#include <iostream>
#include <math.h>
using namespace std;
int main()
{

    int n = 56, i = 0, ans = 0;
    while (n != 0)
    /**
     * @param {string} title 
     * 
     */
    {
        // bit nikal lo
        int digit = n & 1;
        ans = (digit * pow(10, i)) + ans;
        // right shift kardo, last shift gets destroyed
        n = n >> 1;
        i++;
    }
    cout << ans;

    return 0;
}