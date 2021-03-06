#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Vertex {
public:
    int id;
    map<int, float> connectedTo;
    char color;
    float dist;
    Vertex *pred;

    Vertex() {
        // w for white, g for grey, b for black
        color = 'w';
        dist = 0;
        pred = NULL;
    }

    Vertex(int key) {
        id = key;
        color = 'w';
        dist = 0;
        pred = NULL;
    }

    void addNeighbour(int nbr, float weight = 1) {
        connectedTo[nbr] = weight;
    }

    vector<int> getConnections() {
        vector<int> keys;
        // Use of iterator to find all keys
        for (map<int, float>::iterator it = connectedTo.begin();
             it != connectedTo.end();
             ++it) {
            keys.push_back(it->first);
        }
        return keys;
    }

    int getId() {
        return id;
    }

    float getWeight(int nbr) {
        return connectedTo[nbr];
    }

    friend ostream &operator<<(ostream &, Vertex &);
};

ostream &operator<<(ostream &stream, Vertex &vert) {
    vector<int> connects = vert.getConnections();
    stream << vert.id << " connects to: ";
    for (unsigned int i = 0; i < connects.size(); i++) {
        stream << connects[i] << ", ";
    }

    return stream;
}

class Graph {
public:
    map<int, Vertex> vertList;
    int numVertices;

    Graph() {
        numVertices = 0;
    }

    Vertex addVertex(int key) {
        numVertices++;
        Vertex newVertex = Vertex(key);
        this->vertList[key] = newVertex;
        return newVertex;
    }

    Vertex *getVertex(int n) {
        return &vertList[n];
    }

    bool contains(int n) {
        for (map<int, Vertex>::iterator it = vertList.begin();
             it != vertList.end();
             ++it) {
            if (it->first == n) {
                return true;
            }
        }
        return false;
    }

    void addEdge(int f, int t, float cost = 1) {
        if (!this->contains(f)) {
            this->addVertex(f);
        }
        if (!this->contains(t)) {
            this->addVertex(t);
        }
        vertList[f].addNeighbour(t, cost);
        vertList[t].addNeighbour(f, cost);

        // cout << "Vertex: " << f << " is connected to: " << t << " with cost: " << cost << endl;
    }

    vector<int> getVertices() {
        vector<int> verts;

        for (map<int, Vertex>::iterator it = vertList.begin();
             it != vertList.end();
             ++it) {
            verts.push_back(it->first);
        }
        return verts;
    }

    friend ostream &operator<<(ostream &, Graph &);
};

ostream &operator<<(ostream &stream, Graph &grph) {
    for (map<int, Vertex>::iterator it = grph.vertList.begin();
         it != grph.vertList.end();
         ++it) {
        stream << grph.vertList[it->first];
        cout << endl;
    }

    return stream;
}

Graph bfs(Graph g, Vertex *start) {
    start->dist = 0;
    start->pred = NULL;
    queue<Vertex *> vertQueue;
    vertQueue.push(start);
    while (vertQueue.size() > 0) {
        Vertex *currentVert = vertQueue.front();
        vertQueue.pop();
        for (unsigned int nbr = 0; nbr < currentVert->getConnections().size(); nbr++) {
            Vertex &next = g.vertList[currentVert->getConnections()[nbr]];
            if (next.color == 'w') {
                    next.dist = currentVert->dist + 1;
                    next.color = 'g';
                    next.pred = currentVert;
                    vertQueue.push(&next);
            }
        }
        currentVert->color = 'b';
    }

    return g;
}

Graph early_exit(Graph g, Vertex *start, Vertex *goal){
    start->dist = 0;
    start->pred = NULL;
    queue<Vertex *> vertQueue;
    vertQueue.push(start);
    while (vertQueue.size() > 0) {
        Vertex *currentVert = vertQueue.front();
        vertQueue.pop();

        if (currentVert->getId() == goal->getId()){
            break;
        }

        cout << currentVert << endl;
        for (unsigned int nbr = 0; nbr < currentVert->getConnections().size(); nbr++) {
            Vertex &next = g.vertList[currentVert->getConnections()[nbr]];
            if (next.color == 'w') {
                    next.dist = currentVert->dist + 1;
                    next.color = 'g';
                    next.pred = currentVert;
                    vertQueue.push(&next);
            }
        }
        currentVert->color = 'b';
    }

    return g;
}

void traverse(Vertex *y) {
    Vertex *x = y;
    int count = 1;

    while (x->pred) {
        cout << x->id << " to " << x->pred->id << endl;
        x = x->pred;

        count++;
    }
}

int coordToNum(int x, int y, int bdSize) {
    // Takes the x y position and returns the id from 0 to (bdSize*2)-1
    int id = 0;
    id += y * bdSize;
    id += x;

    return id;
}

pair<int, int> numToCoord(int id, int bdSize) {
	int x, y;
	x = id % bdSize;
	y = (id - x) / bdSize;

	return make_pair(x, y);
}

bool legalCoord(int xy, int bdSize) {
	if (xy >= 0 && xy < bdSize) {
		return true;
	} else {
		return false;
	}
}

vector<int> genObstacles(int bdSize=20, string nazwap="grid.txt", char obstacleChar=5){	
	//teraz deklarujemy dynamicznie tablice do, kt�rej wczytamyu nasz plik,
	int rows = bdSize+1;
	double **G;
	G = new double*[rows];
	while(rows--) {
		G[rows] = new double[bdSize+1];
	}

	ifstream plik(nazwap.c_str());

	for ( unsigned int i=0;i<bdSize;i++){
		for ( unsigned int j=0;j<bdSize;j++) {
			plik >> G[i][j];
		}
	}  
	plik.close();

	vector<int> obstacles;
	// j is x axis, i is y axis
	for(int i=0;i<bdSize;i++){
		for(int j=0;j<bdSize;j++){
			if ( G[i][j] == obstacleChar){
				obstacles.push_back(coordToNum(j, i, bdSize));
			}
		}
	}

	//na koniec czy�cimy pami�� po naszej tablicy
	for(int i=0;i<bdSize+1;i++){
		delete[] G[i];
	}//czyscimy wiersze
	delete[] G;//zwalniamy tablice wskaznikow do wierszy
    return obstacles;
}

bool passable(int id, int bdSize) {
    vector<int> obstacles = genObstacles();
    if (find(obstacles.begin(), obstacles.end(), id) != obstacles.end()){
        return false;
    } else {
        return true;
    }
}

vector<int> genLegalMoves(int id, int bdSize) {
	pair<int, int> coords = numToCoord(id, bdSize);
	int x = coords.first;
	int y = coords.second;

	vector<int> newMoves;
	vector<pair<int, int>> myVec = {
		{0, -1}, {-1, 0}, {0, 1}, {1, 0}
	};

	for (unsigned int i = 0; i < myVec.size(); i++) {
		int newX = x + myVec[i].first;
		int newY = y + myVec[i].second;
		if (legalCoord(newX, bdSize) && legalCoord(newY, bdSize)) {
            newMoves.push_back(coordToNum(newX, newY, bdSize));
		}
	}

    return newMoves;
}

double heuristic(int start, int goal){
    pair<int, int> startCoords = numToCoord(start, 20);
	int sx = startCoords.first;
	int sy = startCoords.second;

    pair<int, int> goalCoords = numToCoord(goal, 20);
    int gx = goalCoords.first;
    int gy = goalCoords.second;

    return abs(sx - gx) + abs(sy - gy);
}

Graph generateGraph(int bdSize) {
    Graph ktGraph;

    for (int row = 0; row < bdSize; row++) {
        for (int col = 0; col < bdSize; col++) {
            int nodeId = coordToNum(row, col, bdSize);
            vector<int> newPositions = genLegalMoves(nodeId, bdSize);

            for (int i = 0; i < newPositions.size(); i++) {
                int newId = newPositions[i];
                if (passable(nodeId, bdSize) && passable(newId, bdSize)){
                    ktGraph.addEdge(nodeId, newId);
                }
            }
        }
    }

    return ktGraph;
}

int main() {
    Graph grid = generateGraph(20);
    grid = bfs(grid, grid.getVertex(399));
    traverse(grid.getVertex(0));
    // grid = a_star(grid, grid.getVertex(399), grid.getVertex(0));
    // traverse(grid.getVertex(399));
    // early_exit(grid, grid.getVertex(0), grid.getVertex(40));
    // traverse(grid.getVertex(40));

    return 0;
}