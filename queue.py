class Queue:
    def __init__(self, head):
        self.storage = [head]

    def enqueue(self, new_element):
        pass

    def peek(self):
        pass 

    def dequeue(self):
        pass
    
# Setup
# q = Queue(1)
# q.enqueue(2)
# q.enqueue(3)
queue = []

queue.append('1')
queue.append('2')
queue.append('3')
  
print("Initial queue")
print(queue)
  
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)
# Test peek
# Should be 1
# print (queue.peek())

# # Test dequeue
# # Should be 1
# print (queue.dequeue())

# # Test enqueue
# q.enqueue(4)
# # Should be 2
# print (queue.dequeue())
# # Should be 3
# print (queue.dequeue())
# # Should be 4
# print (queue.dequeue())
# q.enqueue(5)
# # Should be 5
# print (queue.peek())