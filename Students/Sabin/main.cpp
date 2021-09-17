#include <iostream>
#include <string>
#include "ArgumentManager.h"
#include <fstream>
#include <sstream>
#include <bits/stdc++.h>


template<typename T> 

struct Node {
    
    T currentElem;              // this will be our "data-string" 
    Node* next;                 // this is pointing to the next node and so on/ referencing other nodes
    Node(T _currentElem) : currentElem(_currentElem) {}; // TODO: Define a constructor of how we create our Node 
    Node() {
        next = NULL;
        currentElem = "";
    }
                                

};


//TODO: Make a class called "LinkedList in order to link everything together" 
// The class will contain a private mem vars (utility pointers in order to manage linkedlist) & public getter functions to add sort and remove
 
// ETC... 

template<typename T> 
class LinkedList {
    private: 
    public: 
    Node<T>*  head;       // front of linked 
    Node<T>*  tail;       //end of linked  
    size_t _size;        // unsigned integer to increment list 
    LinkedList(); //defualt constructor
    ~LinkedList(); //destructor 
    bool contains(T currentElem); // returns true if element is in the list/ false if otherwise 
    bool isEmpty();  //checks whether  or not our list is empty returns true if empty false otherwise
    void addBeginning(T );  // add to the beginning of the list 
    void addEnd(T);    // add to the end of the list 
    void addToPos(int loc, T currentElem); //first command function 
    
    void addMiddle(); // add to the middle of the list or somewhere between the list 
    bool checkDuplicates(T line);  //If the sentence is duplicate we remove/ don't include 

    void remove(T currentElem);     // any sentence that contains a certain string will get removed 
    void sortAlpha( );   // sort by the word alphabetically 
    void sortLength(); // sort by shortest to longest length 
    void print(ofstream &outputFile);  //pass in output file of type ofstream and pass it by reference  
    void loadFromFile (T); 

    void add(int idx, T line);

    

};

template<typename T> 
LinkedList<T>::LinkedList() {
    head = nullptr;
    tail = nullptr;  
    _size = 0; 
}

template<typename T> 
bool LinkedList<T>::checkDuplicates(T line) {
    Node<T> *curr; 
    curr = head; 
    while (curr != nullptr ) {
        if (curr->currentElem == line) {
            return false;
        }
        curr = curr->next; 
    }
    return true; 
}

template<typename T> 
void LinkedList<T>::addBeginning (T line) {
    if (line == "" || LinkedList::checkDuplicates(line) == false) {return;}
    Node<T> *newNode = new Node<T>;
    newNode -> currentElem = line;
    newNode -> next = nullptr;  
    if (head == nullptr) {head = newNode;}
    else {
        newNode -> next = head; 
        head = newNode; 
    }
    _size+= 1; 
}

template<typename T> 
void LinkedList<T>::addEnd(T line) {
    if (line == "" || LinkedList::checkDuplicates(line) == false) {return;}
    Node<T> *newNode = new Node<T>; 
    newNode->currentElem = line; 
    if (tail != nullptr) {
        tail->next = newNode; 
    }
    else if (head == nullptr) {
        head = newNode; 
    }
    tail = newNode; 
    _size += 1; 
}

template<typename T> 
void LinkedList<T>::add(int idx, T line) {
    if (idx > -1 && idx <= _size && LinkedList::checkDuplicates(line) && line != "") {
        if (idx == 0) {
            LinkedList::addBeginning(line);
        }
        else if (idx == _size) {
            LinkedList::addEnd(line);
        }
        else {
            Node<T> *newNode = new Node<T>; 
            newNode->currentElem = line;
            int counter = 1;
            Node<T> * nodeBefore = head;
            while (true) {
                if (counter == idx) {
                    newNode->next = nodeBefore->next;
                    nodeBefore->next = newNode;
                    break;
                }
                counter++;
                nodeBefore = nodeBefore->next;
            }
        }
    }
    // Node<T> *curr = head; 
    // cout << "FINAL NODE LIST" << endl; 
    // for (size_t i = 0; i < _size; i++) {
    //     cout <<  curr->currentElem <<endl; 
    //     curr = curr->next;
    // }    
}

//  template<typename T> 
//  void LinkedList<T>::remove(T &currentElem, T delData) {             //TODO: command function: contain the input string and if the string passed it will get removed
//      Node<T> *removeNode = NULL;
//      Temp = head; 
//      curr = head; 
//      while(curr != NULL && curr->currentElem != )
//  }

template<typename T>                    
bool LinkedList<T> ::isEmpty() {
    return ((head == nullptr) && (tail == nullptr));
}

template<typename T> 
void LinkedList<T>::loadFromFile(T in) {
    if (in.is_open()) {
        string line; 
        while (getline(in,line)){
            Node<T> *newNode = new Node<T>;
            in>> newNode-> currentElem;
            addEnd(newNode);
        }
    }
}

template<typename T> 
void LinkedList<T>::print(ofstream &answer) {
    for(Node<T>*newNode = head; newNode != 0; newNode = newNode -> next) {
        cout<<sortAlpha(); 
        cout<< newNode-> currentElem; 
    }
}

template<typename T>
 void LinkedList<T>::sortAlpha() {
     Node<T> *i = head; 
     Node<T> *j; 
     if(!i) 
     return; 
     while (i) {
         j = i->next; 
         while(j) {
             if(i->currentElem[0] > j->currentElem[0]) {
                 swap(i->currentElem,j->currentElem);
             }
             j = j->next; 
         }
         i = i->next;
     }
 }

int main (int argc, char* argv[]) {

    // ArgumentManager am (argc, argv);

    // string input = am.get("input");
    // string output = am.get("output");
    // string command = am.get("command");

    ifstream in ("input21.txt");
    ifstream com ("command22.txt");
    ofstream out ("answer.txt"); 
    LinkedList<string> *cl1 = new LinkedList<string>();

    string line;
    getline(in,line);
    if (line =="Beginning") {
        while(!in.eof()) {
            getline(in,line);
            cl1->addBeginning(line);
        }
    }

    else if (line =="End") {
        while(!in.eof()) {
            getline(in,line);
            cl1->addEnd(line);
        }
    }

    // print node contents
    Node<string>* curr = cl1-> head; 
    for (size_t i = 0; i < cl1->_size; i++) {
        cout <<  curr->currentElem <<endl; 
        if (i == cl1->_size - 1) {
            out << curr->currentElem;
        }
        else {
        out << curr->currentElem + "\n";
        } 
        curr = curr->next;
    }
    
    // Going through command.txt
    while (!com.eof()) {
        int index;
        string sentence;
        string sortType;

        getline(com, line);
        istringstream iss(line);
        string token;
        getline(iss, token, ' ');
        const char * cc = token.c_str();
        if (strcmp(cc, "Add") == 0) {
            // gets the index
            getline(iss, token, ' ');
            int end = token.length() - 2;
            token = token.substr(1, end);
            stringstream temp(token);
            temp >> index;
            
            // gets the sentence
            getline(iss, token);
            end = token.length() - 2;
            sentence = token.substr(1, end);
            
            cl1->add(index, sentence);
        }

        else if (strcmp(cc, "Remove") == 0) {
            // gets the sentence
            getline(iss, token);
            int end = token.length() - 2;
            sentence = token.substr(1, end);
        }
        else if (strcmp(cc, "Sort") == 0) {
            // gets the type of sort
            getline(iss, token);
            int end = token.length() - 2;
            sortType = token.substr(1, end);
        }
        cout << index << sentence << sortType << endl;
    }

    curr = cl1->head; 
    cout << "FINAL NODE LIST" << endl; 
    for (size_t i = 0; i < cl1->_size; i++) {
        cout <<  curr->currentElem <<endl; 
        if (i == cl1->_size - 1) {
            out << curr->currentElem;
        }
        else {
        out << curr->currentElem + "\n";
        } 
        curr = curr->next;
    }
    

    return 0;
}