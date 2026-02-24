/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    int count = 1;
    struct ListNode *curr = head;
    while(curr != NULL){
        count++;
        curr = curr->next;
        if (count > 10001)
            return true;
    }
    return false;
}