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

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the
    worst-case runtime of the JS `Array.splice` method. Which method generally
    performs better?

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

4. What is the runtime complexity of `for_each`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
