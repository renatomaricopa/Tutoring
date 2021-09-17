#include <iostream>
#include <string>
#include "ArgumentManager.h"
#include <fstream>


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
    // private: 
    public: 
    Node<T>*  head;       // front of linked 
    Node<T>*  tail;       //end of linked  
    size_t _size;        // unsigned integer to increment list 
    LinkedList(); //defualt constructor
    ~LinkedList(); //destructor 
    bool contains(T currentElem); // returns true if element is in the list/ false if otherwise 
    bool isEmpty();  //checks whether  or not our list is empty returns true if empty false otherwise
    void addFront(T );  // add to the beginning of the list 
    void addEnd(T);    // add to the end of the list 
    void addToPos(int loc, T currentElem); //first command function 

    void addMiddle(); // add to the middle of the list or somewhere between the list 
    bool checkDuplicates(T location);  //If the sentence is duplicate we remove/ don't include 

    void remove(T currentElem);     // any sentence that contains a certain string will get removed 
    void sortAlpha( );   // sort by the word alphabetically 
    void sortLength(); // sort by shortest to longest length 
    void print(ofstream &outputFile);  //pass in output file of type ofstream and pass it by reference  
    void loadFromFile (T); 

    

};

template<typename T> 
 LinkedList<T>::LinkedList() {
     head = nullptr;
     tail = nullptr;  
     _size = 0; 
 }

template <typename T>
bool LinkedList<T>::checkDuplicates (T location){
    Node<T> *curr = head;
    while (curr != nullptr) {
        if (curr->currentElem == location) {
            return false;
        }
        cout << curr->currentElem << endl;
        curr = curr->next;
    }
    return true;
}

template<typename T> 
 void LinkedList<T>::addFront (T location) {
     if (location == "" || LinkedList::checkDuplicates(location) == false) {return;}
     Node<T> *tmp;                            //Creating the dynamic allocation and put the address
     tmp = new Node<T>;                       // into tmp 

     tmp -> currentElem = location;           //Fill node 
     tmp -> next = nullptr; 
     // Linking to existing linked list 
     if(head == nullptr) {
         head = tmp; 
     }
     else  {
         tmp -> next = head;               // the head is always the new tmp 
          head = tmp; 

     }
     _size+= 1; 
 }

 template<typename T> 
 void LinkedList<T>::addEnd(T location) {
     Node<T> *tmp; 
     tmp = new Node<T>; 
     tmp -> currentElem = location; 
     if(tail != nullptr) {
         tail -> next = tmp; 
     }
     if(head == nullptr) {
         head = tmp; 
     }
     tail = tmp; 
     _size += 1; 

 }
 template<typename T> 
 void LinkedList<T>::remove(T currentElem) {             //TODO: command function: contain the input string and if the string passed it will get removed
     Node<T> *removeNode; 
     removeNode = new Node<T> ;
     removeNode  -> currentElem = currentElem; //Fix this 


 }
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

    ArgumentManager am (argc, argv);

    string input = am.get("input");
    string output = am.get("output");
    string command = am.get("command");

    ifstream in ("input21.txt");
    ifstream com ("command21.txt");
    ofstream out ("answer.txt"); 
    LinkedList<string> *cl1 = new LinkedList<string>();


    
    while(!in.eof()) {
        string line;
        getline(in,line);
        cl1->addFront(line);
        cl1->sortAlpha();
    }
     Node<string>* curr = cl1->head;
    for (int i = 0; i < cl1->_size; i++) {
        cout << curr->currentElem << endl;
        out << curr->currentElem + "\n";
        curr = curr->next;  
    }
    return 0;
}