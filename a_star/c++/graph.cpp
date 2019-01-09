#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Vertex{
	public:
		int id;
		map<int, int> connectedTo;

		Vertex(){
		}

		Vertex(int key){
			id = key;
		}

		void addNeighbour(int nbr, int weight = 0){
			connectedTo[nbr] = weight;
		}

};