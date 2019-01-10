#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
using namespace std;


class Vertex {
    public:
        string id;
        map<string, float> connectedTo;
        // add for bfs algorithm
        char color;
        float dist;
        Vertex *pred;

        Vertex(){
            // w for white, g for grey, b for black
            color = 'w';
            dist = 0;
            pred = NULL;
        }

        Vertex(string key){
            id = key;
            color = 'w';
            dist = 0;
            pred = NULL;
        }

        void addNeighbour(string nbr, float weight = 1){
            connectedTo[nbr] = weight;
        }

        vector<string> getConnections(){
            vector<string> keys;
            // Use of iterator to find all keys
            for (map<string, float>::iterator it = connectedTo.begin();
            it != connectedTo.end();
            ++it){
                keys.push_back(it->first);
            }
            return keys;
        }

        string getId(){
            return id;
        }

        float getWeight(string nbr){
            return connectedTo[nbr];
        }

        friend ostream &operator<<(ostream&, Vertex&);
};

ostream &operator<<(ostream &stream, Vertex &vert){
    vector<string> connects = vert.getConnections();
    stream << vert.id << " -> ";
    for (unsigned int i=0; i < connects.size(); i++){
        stream << connects[i] << endl << "\t";
    }

    return stream;
}
