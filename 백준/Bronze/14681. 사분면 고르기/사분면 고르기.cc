#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    int X, Y;
    cin >> X >> Y;
    
    cout << (X > 0 ? (Y > 0 ? 1 : 4) : (Y > 0 ? 2 : 3));
    return 0;
}