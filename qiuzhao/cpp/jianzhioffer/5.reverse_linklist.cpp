/*************************************************************************
	> File Name: 5.reverse_linklist.cpp
	> Author: 
	> Mail: 
	> Created Time: 二  9/18 09:46:10 2018
 ************************************************************************/

#include<iostream>
#include <stack>
using namespace std;
struct ListNode{
    int m_nkey;
    ListNode* m_pNext;
};

void PrintListReverse(ListNode* pHead){
    stack<ListNode*> st;
    while(pHead != NULL){
        st.push(pHead);
        pHead = pHead->m_pNext;
    }

    while(!st.empty()){
        pHead = st.top();
        cout << pHead->m_nkey << endl;
        st.pop();
    }
}


int main(){
    ListNode* node1 = &ListNode();
    node1->m_nkey = 2;
    ListNode* node2 = &ListNode();
    node2->m_nkey = 3;
    node1->m_pNext = node2;
    node2->m_pNext = NULL;
    PrintListReverse(node1);
    return 0;
}
