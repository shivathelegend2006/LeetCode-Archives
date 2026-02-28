/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reorderList(struct ListNode* head) {
    struct ListNode *tort = head, *hare = head;
    while(hare != NULL && hare->next != NULL){
        tort = tort->next;
        hare = hare->next->next;
    }
    struct ListNode *prev = NULL, *curr = tort->next,*nextTemp;
    tort->next = NULL; 
    while(curr != NULL){
        nextTemp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextTemp;
    }
    struct ListNode *first = head, *second = prev;
    
    while(second != NULL){
        struct ListNode *temp1 = first->next, *temp2 = second->next;
        first->next = second;
        second->next = temp1;

        first = temp1;
        second = temp2;
    }
}