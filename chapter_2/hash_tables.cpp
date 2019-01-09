#include <iostream>
#include <ctime>
#include <list>
#include <unordered_map>
using namespace std;

int main(){
    for (int a = 10000; a < 1000001; a = a + 20000){
        clock_t begin = clock();
        list<int> x;
        for (int i=0; i < a; i++){
            x.push_back(i);
        }
        clock_t end = clock();
        double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;

        clock_t begin_ht = clock();
        unordered_map<int, int> y;
        for ( int j = 0; j < a; j++){
            y[j] = NULL;
        }
        clock_t end_ht = clock();
        double elapsed_secs_ht = double(end_ht - begin_ht) / CLOCKS_PER_SEC;

        cout << a << "\t" << elapsed_secs << "\t" << elapsed_secs_ht << endl;
    }

    return 0;
}
