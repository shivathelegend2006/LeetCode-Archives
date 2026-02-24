/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *curr = head;
    while(curr!=NULL){
        if(curr->val == 100001)
            return true;
        curr->val = 100001;
        curr = curr->next;
    }
    return false;
}