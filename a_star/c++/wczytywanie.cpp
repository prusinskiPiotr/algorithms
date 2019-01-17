#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int coordToNum(int x, int y, int bdSize) {
    // Takes the x y position and returns the id from 0 to (bdSize*2)-1
    int id = 0;
    id += y * bdSize;
    id += x;
    return id;
}

int main (void) {

	cout<<"Wczytywanie danych z pliku\n";

	string nazwap="grid.txt";
	int bdSize=20;
	
	//teraz deklarujemy dynamicznie tablice do, kt�rej wczytamyu nasz plik,
	int rows = bdSize+1;
	double **G;
	G = new double*[rows];
	while(rows--) {
		G[rows] = new double[bdSize+1];
	}
	// cout<<"\n\nNacisnij ENTER aby wczytac tablice o nazwie "<< nazwap;
	// getchar();

	std::ifstream plik(nazwap.c_str());

	for ( unsigned int i=0;i<bdSize;i++){
		for ( unsigned int j=0;j<bdSize;j++) {

			plik >> G[i][j];
		}
	}  
	plik.close();

	vector<int> obstacles;
	// j is x axis, i is y axis
	cout<<"\nWypisujemy na ekran\n\n";
	for(int i=0;i<bdSize;i++){
		for(int j=0;j<bdSize;j++){
			if ( G[i][j] == 5){
				obstacles.push_back(coordToNum(j, i, bdSize));
			}
		}
		// cout<<"\n";
	}
	for (vector<int>::iterator i = obstacles.begin(); i != obstacles.end(); ++i){
    	cout << *i << ' ';
	}

	//na koniec czy�cimy pami�� po naszej tablicy
	for(int i=0;i<bdSize+1;i++){
		delete[] G[i];
	}//czyscimy wiersze
	delete[] G;//zwalniamy tablice wskaznikow do wierszy

	cout<<"\n\nNacisnij ENTER aby zakonczyc";
	getchar();

	return 0;
}
