from Queue import Queue


def DuckDuckGoose(arr, k):
    queue = Queue()

    for item in arr:
        queue.enqueue(item)

    while queue.get_size() > 1:
        for _ in range(k-1):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()

arr = ["A", "B", "C", "D", "E","F"]
print(DuckDuckGoose(arr, 3)) 

