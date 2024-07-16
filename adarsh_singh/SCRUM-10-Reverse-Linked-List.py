class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Save the next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev to current
        curr = next_node       # Move to the next node
    return prev

# Example usage
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create a linked list [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the linked list
reversed_head = reverseList(head)
print_list(reversed_head)
