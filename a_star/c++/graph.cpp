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

		vector<int> getConnections(){
			vector<int> keys;
			// use the iterator to find all keys
			for (map<int, int>::iterator it = connectedTo.begin();
				it != connectedTo.end();
				++it){
					keys.push_back(it->first);
			}
			return keys;
		}	

		int getId(){
			return id;
		}

		int getWeight(int nbr){
			return connectedTo[nbr];
		}

		friend ostream &operator<<(ostream&, Vertex&);
};

ostream &operator<<(ostream &stream, Vertex &vert){
	vector<int> connects = vert.getConnections();
	for(unsigned int i = 0; i < connects.size(); i++){
		stream << "( " << vert.id << " , " << connects[i] << " ) \n"; 
	}
	return stream;
}
