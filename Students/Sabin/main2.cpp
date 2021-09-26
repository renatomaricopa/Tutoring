#include <iostream>
#include <string>
#include "ArgumentManager.h"
#include <fstream>
#include <sstream>
#include <cstring> 



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
    void addBeginning(T line);  // add to the beginning of the list 
    void addEnd(T line);    // add to the end of the list 
    void add(int idx, T line); //first command function 

   
    bool checkDuplicates(T line );  //If the sentence is duplicate we remove/ don't include 
    void removeBeginning();
    void removeEnd();
    void remove(T line);     // any sentence that contains a certain string will get removed 
    void sortAlpha();   // sort by the word alphabetically 
    void sortLength(); // sort by shortest to longest length 
    void print(ofstream &out);  //pass in output file of type ofstream and pass it by reference  
    void loadFromFile (T); 

    

};

template<typename T> 
 LinkedList<T>::LinkedList() {
     head = nullptr;
     tail = nullptr;  
     _size = 0; 
 }
 template<typename T>
 LinkedList<T>::~LinkedList() {



 }
template<typename T> 
bool LinkedList<T>::checkDuplicates(T line ) {
    Node<T> *curr; // dont need to assign any memory on the heap 
    curr = head; // set curr  to head 

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

     if(line == "" || LinkedList::checkDuplicates(line) == false ) {
         return; 
     }
     Node<T> *tmp;                            //Creating the dynamic alline and put the address
     tmp = new Node<T>;                       // into tmp 

     tmp -> currentElem = line;           //Fill node 
     tmp -> next = nullptr; 
     // Linking to existing linked list 
     if(head == nullptr) {
         head = tmp; 
         tail = tmp;
     }
     else  {
         tmp -> next = head;               // the head is always the new tmp 
          head = tmp; 

     }
     _size++; 
 }

 template<typename T> 
 void LinkedList<T>::addEnd(T line) {
      if(line == "" || LinkedList::checkDuplicates(line) == false ) {
         return; 
     }
     Node<T> *tmp; 
     tmp = new Node<T>; 
     tmp -> currentElem = line; 
     if(tail != nullptr) {
         tail -> next = tmp; 
     }
     if(head == nullptr) {
         head = tmp; 
     }
     tail = tmp; 
     _size ++; 

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
            Node<T> * curr = head;
            while (curr != nullptr) {
                curr = curr->next;
            }
            _size++;
        }
    }
}

template<typename T> 
void LinkedList<T>::remove(T line) {
    Node<T> * prev = nullptr, *temp = head;
    while (temp != nullptr) {
        string data = temp->currentElem;
        if (data.find(line) != string::npos) {
            Node<T> * n = temp->next;
            if (prev == nullptr) {
                head = head->next;
            }
            else {
                prev->next = n;
            }
            delete temp;
            _size--;
            temp = n;
        }
        else {
            prev = temp;
            temp = temp->next;
        }
    }
    if (head == nullptr) {
        tail = nullptr;
    }
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

 void LinkedList<T>::print(ofstream &out) {
     for(Node<T>*newNode = head; newNode != 0; newNode = newNode -> next) {

         cout<<sortAlpha(); 
         cout<< newNode-> currentElem; 
     }
 }

template<typename T>
 void LinkedList<T>::sortAlpha() {
     Node<T> *i = head; 
     Node<T> *j; 
     const char * str1;
    const char * str2;
     if(!i) 
     return; 
     while (i) {
         j = i->next; 
         while(j) {
            str1 = i->currentElem.c_str();
            str2 = j->currentElem.c_str();
             if(strcmp(str1, str2) > 0) {
                 swap(i->currentElem,j->currentElem);
             }
             j = j->next; 
         }
         i = i->next;
     }
 }

 template<typename T> 
 void LinkedList<T>::sortLength() {
     Node<T> *i = head; 
     Node<T> *j; 

     if(!i) 
     return; 

     while (i) {
         j=i->next; 
         while (j) {
             if (i->currentElem.length() > j->currentElem.length()) {
                 swap(i->currentElem, j->currentElem); 

             }
             j = j->next; 
         }
         i = i->next; 
     }
 }

 
int main (int argc, char* argv[]) {

    ArgumentManager am (argc, argv);

    string input = am.get("input");   //whatever input file the ta runs for ex: input21.txt, the argument manager will catch it and save it to input 
    string output = am.get("output");
    string command1 = am.get("command");

    ifstream in ("input22.txt");
    ifstream com ("command22.txt");
    ofstream out ("answer.txt"); 
    LinkedList<string> *cl1 = new LinkedList<string>();

    string line;
    getline(in,line);
    if(line =="Beginning" ) {
         while(!in.eof()) {
        getline(in,line);
        cl1->addBeginning(line);
    }

    }
    else if(line =="End" ) {
         while(!in.eof()) {
        getline(in,line);
        cl1->addEnd(line);
         }
    }
    
    else if (line == "Length") {
        while(!in.eof()) {
        getline(in,line);
        cl1->addEnd(line);
         }
        cl1->sortLength();
    }
    else if (line == "Alphabetically") {
        while(!in.eof()) {
        getline(in,line);
        cl1->addEnd(line);
         }
        cl1->sortAlpha();
    }

    while (!com.eof()) {
        int index; 
        string sentence; 
        string sortType;

        getline(com,line); 
        istringstream iss(line);
        string token; 
        getline(iss,token,' ');
        const char* command = token.c_str (); 
        if (strcmp(command, "Add")==0) {
            //gets the index 
            getline(iss,token,' '); 
            int count = token.length() - 2;
            token = token.substr(1,count);
            stringstream temp (token);
            temp >> index; 
            // gets the sentence 
            getline (iss, token); 
            count = token.length() -2; 
            sentence = token.substr(1, count);
            cl1->add(index, sentence);
        }
        else if (strcmp(command, "Remove")==0) {
            getline (iss,token);
            int count = token.length() -2;  
            sentence =token.substr(1,count); 
            cl1->remove(sentence);
        }
        else if (strcmp(command, "Sort") == 0) {
            getline (iss, token);
            int count = token.length() -2;
            sentence = token.substr(1,count); 
            if (strcmp(sentence.c_str(), "alphabetically") == 0) {
                cl1->sortAlpha();
                
            }
            else if (strcmp(sentence.c_str(), "length")  == 0) {
                cl1->sortLength(); 
            }
        }
    }

    Node<string> * curr = cl1->head;
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