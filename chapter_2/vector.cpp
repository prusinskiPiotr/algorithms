#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> vect;
    vector<int> vect2;

    for (int i = 0; i < 1000; i++){
        vect.push_back(i);
    }

    for (int i = 0; i < 1000; i++){
        vect2.push_back(i);
    }

    clock_t begin = clock();
    for (int i = 0; i < 1000; i++){
        vect.erase(vect.begin()+0);
    }
    clock_t end = clock();
    double elapsed_secs = double(end - begin) /CLOCKS_PER_SEC;
    cout << fixed << endl;
    cout << "popzero = " << elapsed_secs << endl;

    clock_t begin2 = clock();
    for (int i = 0; i < 1000; i++){
        vect2.pop_back();
    }
    clock_t end2 = clock();
    double elapsed_secs2 = double(end2 - begin2) /CLOCKS_PER_SEC;
    cout << fixed << endl;
    cout << "popend = " << elapsed_secs2 << endl;

    return 0;
}
