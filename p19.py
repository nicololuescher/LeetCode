import time


class ListNode:
    def __repr__(self):
        if self.next:
            return f"{self.val}, {self.next.__repr__()}"
        else:
            return str(self.val) 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: list[ListNode], n: int) -> list[ListNode]:
        history = []

        node = head
        while hasattr(node, "next"):
            history.append(node)
            node = node.next

        if n == 1:
            if len(history) == 1:
                return None
            else:
                history[-2].next = None
        elif n == len(history):
            if len(history) == 1:
                return None
            else:
                head = head.next
        else:
            history[-n-1].next = history[-n+1]
        
        return head
    def test(self):
        num = 5
        node = ListNode(num)
        for i in range(1, num):
            newNode = ListNode(num-i, node)
            node = newNode
        return self.removeNthFromEnd(node, 1)


def main():
    print(Solution().test())

if __name__ == "__main__":
    main()
