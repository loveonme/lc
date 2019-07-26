# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """cannot trans to integer"""
        """
        1,3,2
        2,1
         
        """
        a = []
        p = l1 
        while p is not None:
            a.append(p)
            p = p.next

        b = []
        q = l2
        while q is not None:
            b.append(q)
            q = q.next
        length = max(len(a),len(b))
        res = []
        index_a = len(a) -1
        index_b = len(b) - 1
        incre = 0
        for i in range(length):
            a_tmp = a[index_a].val if index_a >= 0 else 0
            b_tmp = b[index_b].val if index_b >= 0 else 0
            cur = (a_tmp + b_tmp + incre) % 10
            incre = 1 if (a_tmp + b_tmp + incre) >= 10 else 0
            res.append(cur)
            index_a -= 1
            index_b -= 1
        
        if incre > 0:
            res.append(incre)

        if len(res) == 0:
            return None
        
        for i in range(len(res)):
            p = ListNode(res[len(res) - i -1])
            if i == 0:
                out = p
                q = p
            if len(res) - i - 1 == 0:
                q.next = p
                p.next = None
            else:
                q.next = p
                q = p
            
        return out
        
    """
    第一步当然是逆序，可以是链表直接逆序，也可以是用一个list来保存顺序，前者更省内存
    第二个难点是生成新链表
    [1,2,3] for i in list;new 1, h = 1 p = h; q = new 2,p.next = q;p = q; q = new 3 ,p.next = q;p = q;
    """