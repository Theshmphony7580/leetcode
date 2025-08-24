/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* F = head;
    // F = NULL;
    //to print
    // struct ListNode* temp = F;
    while(F&&F->next){
        // F = F->next;
        if (F -> next -> val == F->val){
            F->next = F->next->next;
            continue;
        }
        F = F->next;
    }
    return head;
}
        


    
