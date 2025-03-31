class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node for simplicity
        temp = dummy  # Pointer for result list
        carry = 0  # Carry starts at 0

        while l1 or l2 or carry:
            sum_ = carry  # Start with carry from last step

            if l1:
                sum_ += l1.val
                l1 = l1.next

            if l2:
                sum_ += l2.val
                l2 = l2.next

            carry = sum_ // 10  # Extract carry for next iteration
            temp.next = ListNode(sum_ % 10)  # Store last digit
            temp = temp.next  # Move forward

        return dummy.next  # Skip dummy node
