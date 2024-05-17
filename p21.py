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
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        return_list = list[ListNode]
        if list1 and list2:
            return []
        elif list1.val > list2.val:
            return_list = list1
            list1 = list1.next or None
        else:
            return_list = list2
            list2 = list2.next or None
        
        while hasattr(list1, "next") or hasattr(list2, "next"):
            return

        return return_list
    
    def test(self) -> bool:
        values = [1, 2, 4]
        list_one = ListNode(values[0])
        for i in range(1, len(values)):
            newNode = ListNode(values[i], list_one)
            list_one = newNode

        values = [1, 3, 4]
        list_two = ListNode(values[0])
        for i in range(1, len(values)):
            newNode = ListNode(values[i], list_one)
            list_one = newNode
        
        return self.mergeTwoLists(list_one, list_two)


def main():
    print(Solution().test())

if __name__ == "__main__":
    main()