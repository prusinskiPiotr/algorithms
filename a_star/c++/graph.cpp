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


class Graph{
	public:
		map<int, Vertex> vertList;
		int numVertices;

		Graph(){
			numVertices = 0;
		}

		Vertex addVertex(int key){
			numVertices++;
			Vertex newVertex = Vertex(key);
			this->vertList[key] = newVertex;
			return newVertex;
		}

		Vertex *getVertex(int n){
			for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it){
				if (it->first == n){
					// forced to use pointer due to possibility of returning NULL
					Vertex *vpntr = &vertList[n];
					return vpntr;
				} else{
					return NULL;
				}
			}
		}

		bool contains(int n){
			for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it){
				if (it->first == n){
					return true;
				}
			}
		}

		void addEdge(int f, int t, int cost = 0){
			if (!this->contains(f)){
				cout << f << " was not found, adding!" << endl;
				this->addVertex(f);
			}
			if (!this->contains(t)){
				cout << t << " was not found, adding!" << endl;
				this->addVertex(t);
			}
			vertList[f].addNeighbour(t, cost);
		}

		vector<int> getVertices() {
			vector<int> verts;

			for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it){
				verts.push_back(it->first);
			}
			return verts;
		}

		friend ostream &operator<<(ostream&, Graph&);
};

ostream &operator<<(ostream &stream, Graph &grph){
	for (unsigned int i = 0; i < grph.vertList.size(); i++){
		stream << grph.vertList[i];
	}

	return stream;
}
