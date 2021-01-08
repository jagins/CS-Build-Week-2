def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
         #break each list into an array
        a1 = []
        a2 = []
        current = l1
        
        while current is not None:
            a1.append(current.val)
            current = current.next
        
        current = l2
        while current is not None:
            a2.append(current.val)
            current = current.next
        
        #join each array
        int1 = [str(i) for i in a1]
        int1.reverse()
        int2 = [str(j) for j in a2]
        int2.reverse()
        int1 = ''.join(int1)
        int2 = ''.join(int2)
        
        #add the numbers together
        sum = int(int1) + int(int2)

        #convert the sum back into an array of strings to reverse
        answer = [i for i in str(sum)]

        #convert back into ints to put into the linked list to be returned
        answer = [int(i) for i in answer]
        answer.reverse()
        #make into a linked list
        current = ll = ListNode(answer[0])
        i = 1
        while i < len(answer):
            current.next = ListNode(answer[i])
            current = current.next
            i += 1

        return ll
        