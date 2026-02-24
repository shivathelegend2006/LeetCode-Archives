/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *step = head;
    struct ListNode *double_step = head;

    while(double_step != NULL && double_step->next != NULL){
        step = step->next;
        double_step = double_step->next->next;
        if (step == double_step)
            return true;
    }
    return false;
}