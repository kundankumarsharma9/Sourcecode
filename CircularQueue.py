class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None
        self.front = self.rear = -1  # Both front and rear are set to -1 initially

    def is_full(self):
        # Condition for a full queue: if next position of rear is the front
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        # Condition for an empty queue: front and rear both are -1
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!")
        else:
            # If inserting the first element
            if self.front == -1:
                self.front = 0
            # Circular increment of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(f"Enqueued {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        else:
            data = self.queue[self.front]
            # If only one element was in the queue
            if self.front == self.rear:
                self.front = self.rear = -1  # Reset queue to empty
            else:
                # Circular increment of front
                self.front = (self.front + 1) % self.size
            print(f"Dequeued {data}")
            return data

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements are:", end=" ")
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")
            else:
                for i in range(self.front, self.size):
                    print(self.queue[i], end=" ")
                for i in range(0, self.rear + 1):
                    print(self.queue[i], end=" ")
            print()

# Example usage:
cq = CircularQueue(5)  # Queue size 5
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.display()

cq.dequeue()
cq.display()

cq.enqueue(60)
cq.display()


# Explanation:
# Initialization: When you create a circular queue, it starts with a fixed size, and both front and rear are set to -1. This means the queue is empty and ready to store data.

# is_full: This function checks if the queue is full. A queue is considered full if moving the rear to the next position would make it overlap with the front (because of the circular structure).

# is_empty: This function checks if the queue is empty. It does that by seeing if both front and rear are still at -1, which means no data has been added yet.

# enqueue: This is how you add an item to the queue. If it's the first time you're adding something, front is set to 0, and the item is placed at the position of rear. Then, rear moves to the next spot, using circular movement to wrap around if needed.

# dequeue: This removes an item from the queue. The item at the front is taken out, and the front is moved forward. If the queue becomes empty after removing the item, both front and rear reset to -1.

# display: This function shows the elements currently in the queue. Since it's a circular queue, it carefully displays the elements in the correct order, even if rear has looped around.
