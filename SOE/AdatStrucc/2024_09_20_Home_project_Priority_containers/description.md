# Overall task

Your task is to compare different possible implementation solutions for an abstract data structure, that has 3 basic operations:
 - creating an empty container
 - adding an integer to the container (`push`)
 - getting and removing the largest number from the container (`pop_max`)

It can be assumed, that each number is unique. 

# Mandatory implementations

The skeleton of the mandatory implementations can be found in [priority.py](priority.py). 
 - **LazyPriorityList**: uses `list` as internal structure without keeping them in order, so `push` is simple, but `pop_max` has to find the max value.
 - **PriorityList**: Also uses `list` as internal structure, but keeps it in increasing order when a new element is `push`ed, so `get_max` is quick.
 - **PriorityDequeue**: The same, but uses `deque` as internal structure
 - **PriorityQueue**: A wrapper for [`queue.PriorityQueue`](https://docs.python.org/3/library/queue.html#queue.PriorityQueue)
  
As a bonus, one can also add an own maxheap implementation and/or a [`heappq`](https://docs.python.org/3/library/heapq.html).

# GA tests

In [test_random_cases.py](test_random_cases.py) several test cases with various sizes are run for all of the implementations. 

The cases are stored in `Random_cases_MAXSIZE.json` files. Each element of a list is a test case in this format:

```json
  {
    "input": [ 3, null, 2, 0, 1, 4, null, 5 ],
    "output": [ 3, 4 ]
  },
```

In the `input`, numbers are `push` operations and `null`s are `pop_max` operations.

If any of theses tests fail, the corresponding implementation is faulty and the submission cannot be accepted. 

# Emprirical tests

Your task is to carry out "interesting" tests on test cases generated by you. For each test, you have to measure, plot the time required by different data structures, draw conclusions based on them, and provide a hypothesis based on learned asymptotic running times why those results occur, or indicate if/where theory and experimental results diverge.

Mandatory test cases:
1. Only push operations in increasing order
2. Only push operations in decreasing order
3. Only push operations in random order
4. `n` push operations in increasing order then `n` `pop_max` operations 
5. `n` push operations in decreasing order then `n` `pop_max` operations 
6. `n` push operations in random order then `n` `pop_max` operations 
7. `n` times `push`-`pop_max` operation pairs right after each other
8. Initialize the container with `n` elements in random order, then `n//100` push operations
9. Initialize the container with `n` elements in random order, then `n//100` push operations followed by `n//100` pop_operations.

In the last two tests, the initialization should **not** be included in the time measurement.

You should push `n` as high as reasonable. If some implementations seem drastically slower than others, you may continue to test on larger test cases for only a selection of implementations.

For each test use the same machine with `timeit`, preferably with no other processes running. 

The test results should be available in `csv` file format.

Diagrams should be communicating the results. One test case may need more diagrams to fully do that. Do **not** state that something "can be seen" on the diagram if it clearly can't. 
