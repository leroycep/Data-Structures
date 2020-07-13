Answer the following questions for each of the data structures you implemented
as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?

   - O(1), amortized
   - Individual operations can be O(n), though this usually doesn't matter
     unless you are building a real-time system or something

2. What is the runtime complexity of `push` using a linked list?

   - O(1), always

3. What is the runtime complexity of `pop` using a list?

   - O(1), always
   - This is only true because python lists don't move a list when the size is
     reduced, only when it's potential capacity needs to increase. If this
     wasn't the case, and it always moved the list to an exact size allocation,
     it would be O(n).

4. What is the runtime complexity of `pop` using a linked list?

   - O(1), always

5. What is the runtime complexity of `len` using a list?

   - O(1), always
   - Lists are a pointer + a length. If it was a terminated with a sentinal
     instead of storing length, it would be O(n)

6. What is the runtime complexity of `len` using a linked list?

   - O(n)
   - This could easily be O(1) if the length of the LinkedList was stored and
     maintained

## Queue

1. What is the runtime complexity of `enqueue` using a list?

   - I will assume that `enqueue` appends to the end of the list
   - The runtime complexity is O(n)
   - Amortized (on average) the runtime is O(1) though

2. What is the runtime complexity of `enqueue` using a linked list?

   - O(1)

3. What is the runtime complexity of `dequeue` using a list?

   - I will assume that `dequeue` removes from the beginning of the list
   - The runtime complexity is O(n)

4. What is the runtime complexity of `dequeue` using a linked list?

   - The runtime complexity is O(1)

5. What is the runtime complexity of `len` using a list?

   - The runtime complexity is O(1)

6. What is the runtime complexity of `len` using a linked list?

   - The runtime complexity is O(1)
   - This assumes that you are storing the length of the linked list somewhere.
       - I think this is reasonable because the list also keeps track of its length
   - If the size is not stored, the runtime complexity of `len` is O(n)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

   - The runtime complexity is O(1)

2. What is the runtime complexity of `ListNode.insert_before`?

   - The runtime complexity is O(1)

3. What is the runtime complexity of `ListNode.delete`?

   - The runtime complexity is O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

   - The runtime complexity is O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

   - The runtime complexity is O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

   - The runtime complexity is O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

   - The runtime complexity is O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

   - The runtime complexity is O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

   - The runtime complexity is O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

   - The runtime complexity is O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the
    worst-case runtime of the JS `Array.splice` method. Which method generally
    performs better?
    
        - The doubly linked list is O(1), compared to O(n), meaning that the
          performance of the doubly linked list will be better on large datasets.

## Binary Search Tree

1. What is the runtime complexity of `insert`?

   - The runtime complexity is O(h), where h is the height of the tree
   - If the tree is balanced, this means that `insert` is O(log n)
   - In the worst case, it becomes a linked list without a
     pointer to the end of the list, making it O(n)

2. What is the runtime complexity of `contains`?

   - The runtime complexity is O(h), where h is the height of the tree
   - If the tree is balanced, this means that `insert` is O(log n)
   - In the worst case, it becomes a linked list without a
     pointer to the end of the list, making it O(n)

3. What is the runtime complexity of `get_max`?

   - The runtime complexity is O(h), where h is the height of the tree
   - If the tree is balanced, this means that `insert` is O(log n)
   - In the worst case, it becomes a linked list without a
     pointer to the end of the list, making it O(n)

4. What is the runtime complexity of `for_each`?

   - The runtime complexity is O(n)

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
