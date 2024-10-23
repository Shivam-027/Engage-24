import random
import logging
import os
import sys
from langchain_huggingface import HuggingFaceEndpoint

# Example question bank with hardcoded questions for simplicity
class QuestionBank:
    def __init__(self):
        self.questions = {
            'dsa': {
                'easy': {
                    'questions': [
                        "Define a stack and explain its operations.",
                        "What is a binary search tree?",
                        "Explain the difference between an array and a linked list.",
                        "What is the purpose of a queue in data structures?",
                        "Describe the concept of a hash table.",
                        "What are the basic operations of a linked list?",
                        "What is the difference between a stack and a queue?",
                        "Define a binary tree and its properties.",
                        "What is the purpose of a heap in data structures?",
                        "Explain the concept of a graph and its types.",
                    ],
                    'answers': [
                        "A stack is a linear data structure that follows the LIFO (Last In, First Out) principle. Operations include push, pop, and peek.",
                        "A binary search tree is a binary tree where each node has a value greater than any in its left subtree and less than any in its right subtree.",
                        "An array is a collection of elements stored in contiguous memory locations, while a linked list is a collection of elements, called nodes, where each node points to the next node in the sequence.",
                        "A queue is a linear data structure that follows the FIFO (First In, First Out) principle. It's used in various applications like task scheduling and handling requests in real-time systems.",
                        "A hash table is a data structure that maps keys to values using a hash function. It is used for fast data retrieval.",
                        "The basic operations of a linked list include insertion, deletion, and traversal of elements.",
                        "A stack follows LIFO, where the last element added is the first to be removed. A queue follows FIFO, where the first element added is the first to be removed.",
                        "A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.",
                        "A heap is a special tree-based data structure that satisfies the heap property. In a max heap, for any given node 'i', the value of 'i' is greater than or equal to the values of its children.",
                        "A graph is a collection of nodes (or vertices) and edges that connect pairs of nodes. Graphs can be directed or undirected, and they can be weighted or unweighted.",
                    ]
                },
                'medium': {
                    'questions': [
                        "Explain the difference between a stack and a queue.",
                        "Describe the quicksort algorithm.",
                        "What is dynamic programming, and how is it used?",
                        "What is the difference between depth-first search (DFS) and breadth-first search (BFS)?",
                        "Describe the process of merging two sorted arrays.",
                        "What is the purpose of a priority queue, and how is it implemented?",
                        "Explain the concept of memoization in dynamic programming.",
                        "What is the difference between a singly linked list and a doubly linked list?",
                        "Describe the Dijkstra algorithm for finding the shortest path in a graph.",
                        "Explain the concept of binary heap and its applications.",
                    ],
                    'answers': [
                        "A stack follows LIFO, where the last element added is the first to be removed. A queue follows FIFO, where the first element added is the first to be removed.",
                        "Quicksort is a divide-and-conquer algorithm that selects a 'pivot' element and partitions the array into sub-arrays such that elements less than the pivot come before, and elements greater come after. It then recursively sorts the sub-arrays.",
                        "Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is used in optimization problems where the optimal solution can be constructed from optimal solutions of its subproblems.",
                        "DFS explores as far as possible along each branch before backtracking, while BFS explores all neighbors at the present depth before moving on to nodes at the next depth level.",
                        "Merging two sorted arrays involves comparing the elements of both arrays one by one and adding the smaller element to the result array until all elements are added.",
                        "A priority queue is a type of queue where each element has a priority associated with it. Elements with higher priority are dequeued before elements with lower priority. It can be implemented using a heap.",
                        "Memoization is a technique used in dynamic programming where the results of expensive function calls are stored and reused to avoid redundant computations.",
                        "A singly linked list contains nodes with a single pointer pointing to the next node, whereas a doubly linked list contains nodes with two pointers, one pointing to the next node and one pointing to the previous node.",
                        "Dijkstra's algorithm finds the shortest path between nodes in a graph by iteratively selecting the node with the smallest known distance and updating the distances to its neighbors.",
                        "A binary heap is a complete binary tree where each node is smaller (in a min-heap) or larger (in a max-heap) than its children. It's used in implementing priority queues and heap sort.",
                    ]
                },
                'hard': {
                    'questions': [
                        "What is a Red-Black Tree and why is it used?",
                        "Explain Dijkstra's Algorithm for finding the shortest path in a graph.",
                        "Describe the A* algorithm and its use in pathfinding.",
                        "What is the amortized time complexity of splay tree operations?",
                        "Explain the difference between a binary heap and a Fibonacci heap.",
                        "Describe the process of implementing a Trie data structure and its applications.",
                        "What is the time complexity of the Boyer-Moore string search algorithm?",
                        "Explain the concept of a Bloom filter and its applications.",
                        "What is the difference between Kruskal's and Prim's algorithms for finding the minimum spanning tree?",
                        "Describe the Rabin-Karp algorithm for pattern matching and its advantages.",
                    ],
                    'answers': [
                        "A Red-Black Tree is a balanced binary search tree where each node contains an extra bit for denoting the color of the node, either red or black. It's used in various applications because it guarantees a logarithmic height, ensuring efficient insertion, deletion, and lookup operations.",
                        "Dijkstra's Algorithm is a greedy algorithm used to find the shortest path between nodes in a graph. It works by starting at the source node, repeatedly selecting the node with the smallest known distance, updating the distances to its neighbors, and marking it as processed.",
                        "The A* algorithm is a graph traversal and pathfinding algorithm that is often used in games and maps. It uses a best-first search and finds the least-cost path from a given initial node to a goal node.",
                        "The amortized time complexity of splay tree operations is O(log n), but in the worst case, it can be O(n) for a single operation.",
                        "A binary heap is a complete binary tree where each node is smaller or larger than its children, whereas a Fibonacci heap is a more complex data structure that allows for more efficient decrease-key operations, making it useful in algorithms like Dijkstra's.",
                        "A Trie is a tree-like data structure used to store a dynamic set of strings, where the keys are usually strings. It is used in applications like auto-complete and spell checking.",
                        "The time complexity of the Boyer-Moore string search algorithm is O(n/m), where n is the length of the text and m is the length of the pattern. It is particularly efficient for large alphabets.",
                        "A Bloom filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It is used in applications where space is limited and some false positives are acceptable.",
                        "Kruskal's algorithm builds the minimum spanning tree by sorting all edges and adding them one by one to the tree, while Prim's algorithm starts with a single node and grows the tree by adding the cheapest edge from the tree to another vertex.",
                        "The Rabin-Karp algorithm is a string-searching algorithm that uses hashing to find any one of a set of pattern strings in a text. It is particularly effective when searching for multiple patterns simultaneously.",
                    ]
                }
            },
            'os': {
                'easy': {
                    'questions': [
                        "Define an operating system and its main functions.",
                        "What is a process in an operating system?",
                        "Explain the difference between a process and a thread.",
                        "What is a file system in an operating system?",
                        "Describe the boot process of a computer.",
                        "What is the difference between multitasking and multiprogramming?",
                        "What is an interrupt in an operating system?",
                        "What is the purpose of device drivers?",
                        "Explain the difference between primary and secondary memory.",
                        "What is virtual memory and how does it work?",
                        # Add up to 100 questions...
                    ],
                    'answers': [
                        "An operating system is system software that manages hardware and software resources and provides common services for computer programs.",
                        "A process is an instance of a program in execution, including its code, data, and system resources.",
                        "A process is a program in execution, while a thread is a smaller unit of a process that can be scheduled for execution.",
                        "A file system is a method used by operating systems to store, retrieve, and organize files on a storage device.",
                        "The boot process involves loading the operating system into memory when the computer is powered on.",
                        "Multitasking allows multiple processes to run concurrently, while multiprogramming allows multiple programs to be in memory at once, improving CPU utilization.",
                        "An interrupt is a signal to the processor indicating that an event needs immediate attention.",
                        "Device drivers are specialized programs that allow the operating system to communicate with hardware devices.",
                        "Primary memory (RAM) is the main memory used by the CPU to execute programs, while secondary memory (hard drives, SSDs) is used for long-term storage.",
                        "Virtual memory is a memory management technique that creates an illusion of a large memory space by using disk storage to extend RAM.",
                        # Add up to 100 answers...
                    ]
                },
                'medium': {
                    'questions': [
                        "Explain the concept of deadlock in operating systems.",
                        "What are the different types of operating systems?",
                        "Describe the process of context switching in operating systems.",
                        "What is the role of a file system in an operating system?",
                        "Explain the difference between paging and segmentation.",
                        "Describe the concept of process synchronization.",
                        "What are semaphores and how are they used?",
                        "Explain the difference between internal and external fragmentation.",
                        "What is a system call in an operating system?",
                        "Describe the different types of process scheduling algorithms.",
                        # Add up to 100 questions...
                    ],
                    'answers': [
                        "A deadlock occurs when two or more processes are unable to proceed because each is waiting for the other to release resources.",
                        "Types of operating systems include batch OS, time-sharing OS, distributed OS, real-time OS, and multi-user OS.",
                        "Context switching is the process of storing the state of a process so that it can be resumed from the same point later, allowing the CPU to switch between processes.",
                        "The file system manages how data is stored and retrieved on a storage device, providing a way to organize files and directories.",
                        "Paging divides memory into fixed-size pages, while segmentation divides memory into variable-size segments.",
                        "Process synchronization ensures that processes execute in a way that prevents race conditions and ensures data consistency.",
                        "Semaphores are synchronization tools used to manage concurrent processes by signaling whether resources are available.",
                        "Internal fragmentation occurs when memory is allocated but not fully used by a process, while external fragmentation occurs when free memory is scattered in small blocks.",
                        "A system call is a request from a process to the operating system to perform a service, such as file manipulation, process control, or communication.",
                        "Process scheduling algorithms include FCFS, SJF, Round Robin, Priority Scheduling, and Multilevel Queue Scheduling.",
                        # Add up to 100 answers...
                    ]
                },
                'hard': {
                    'questions': [
                        "What is the difference between monolithic and microkernel operating systems?",
                        "Describe the process of memory management in an operating system.",
                        "Explain the concept of process synchronization using monitors.",
                        "What are the advantages and disadvantages of using virtual memory?",
                        "Describe the role of the scheduler in real-time operating systems.",
                        "What is the difference between hard and soft real-time systems?",
                        "Explain the concept of inter-process communication (IPC) and the various methods used.",
                        "What are the different types of scheduling algorithms used in operating systems?",
                        "Explain the concept of deadlock prevention and avoidance.",
                        "What are the key challenges in designing a distributed operating system?",
                        # Add up to 100 questions...
                    ],
                    'answers': [
                        "Monolithic kernels include all the operating system services in a single large block of code running in a single address space, while microkernels have a minimalistic core with other services running in user space.",
                        "Memory management involves managing the allocation, deallocation, and swapping of memory to ensure efficient use of system resources.",
                        "Monitors are synchronization constructs that provide a mechanism for safe access to shared resources by multiple processes.",
                        "Virtual memory allows for the execution of processes that may not be fully in memory, but it can lead to increased overhead and slower performance due to paging.",
                        "In real-time operating systems, the scheduler ensures that tasks are completed within specified time constraints by prioritizing tasks based on urgency.",
                        "Hard real-time systems guarantee task completion within strict deadlines, while soft real-time systems have more flexible deadlines, allowing occasional deadline misses.",
                        "IPC methods include shared memory, message passing, semaphores, and pipes, each with its own advantages and use cases.",
                        "Scheduling algorithms in operating systems include preemptive and non-preemptive scheduling, with variations like FCFS, SJF, Round Robin, and Priority Scheduling.",
                        "Deadlock prevention strategies include avoiding circular wait conditions, while avoidance involves careful resource allocation to ensure a safe state.",
                        "Challenges in distributed operating systems include managing communication, synchronization, resource allocation, and fault tolerance across multiple nodes.",
                        # Add up to 100 answers...
                    ]
                }
            },
            'java':{
                'easy': {
                    'questions': [
                        "What is Java and what are its main features?",
                        "Explain the concept of object-oriented programming (OOP) in Java.",
                        "What is inheritance and how is it implemented in Java?",
                        "Describe the use of constructors in Java.",
                        "What is encapsulation and how is it achieved in Java?",
                        "Explain the concept of polymorphism in Java with an example.",
                        "What are Java's primitive data types?",
                        "What is the role of the `this` keyword in Java?",
                        "Describe the difference between `static` and `non-static` methods.",
                        "What is the difference between a class and an object in Java?",
                        # Add up to 100 questions...
                    ],
                    'answers': [
                        "Java is a high-level, object-oriented programming language with features like platform independence, automatic memory management, and rich libraries.",
                        "OOP in Java is based on concepts like classes, objects, inheritance, polymorphism, and encapsulation.",
                        "Inheritance allows one class to inherit fields and methods from another class using the `extends` keyword.",
                        "Constructors are special methods used to initialize objects when they are created.",
                        "Encapsulation is the practice of bundling data and methods that operate on that data within a single class and restricting access to some of the object's components.",
                        "Polymorphism allows objects to be treated as instances of their parent class rather than their actual class. For example, method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.",
                        "Java's primitive data types include `byte`, `short`, `int`, `long`, `float`, `double`, `char`, and `boolean`.",
                        "The `this` keyword refers to the current instance of the class and is used to access instance variables and methods.",
                        "Static methods belong to the class rather than instances of the class, and they can be called without creating an object. Non-static methods require an instance of the class to be called.",
                        "A class is a blueprint for creating objects, while an object is an instance of a class.",
                        # Add answers for all 100 questions...
                    ]
                },
                'medium': {
                    'questions': [
                        "Explain the concept of `Java exceptions` and how they are handled.",
                        "What are the different types of collections in Java? Give examples.",
                        "Describe the use of `interfaces` and `abstract classes` in Java.",
                        "How does Java support multi-threading?",
                        "What is the purpose of the `final` keyword in Java?",
                        "Explain the concept of `serialization` and its use cases.",
                        "How do `HashMap` and `TreeMap` differ in Java?",
                        "What is `JVM` and how does it work?",
                        "Describe the difference between `checked` and `unchecked exceptions` in Java.",
                        "How does the `try-with-resources` statement work in Java?",
                        # Add up to 100 questions...
                    ],
                    'answers': [
                        "Java exceptions are objects that describe an exceptional condition that has occurred in a method. They are handled using `try-catch` blocks or declared with `throws` keyword.",
                        "Java collections include lists (`ArrayList`, `LinkedList`), sets (`HashSet`, `TreeSet`), queues (`PriorityQueue`), and maps (`HashMap`, `TreeMap`).",
                        "Interfaces define a contract for classes to implement, while abstract classes provide a partial implementation and can include abstract methods.",
                        "Java supports multi-threading using the `Thread` class and the `Runnable` interface, allowing concurrent execution of multiple threads.",
                        "The `final` keyword can be used to declare constants, prevent method overriding, and prevent inheritance.",
                        "Serialization is the process of converting an object into a byte stream to save it to a file or transmit it over a network. It is used for persistence and communication.",
                        "`HashMap` provides constant-time performance for basic operations, while `TreeMap` provides log(n) time complexity and maintains order.",
                        "JVM (Java Virtual Machine) executes Java bytecode and provides a platform-independent execution environment by translating bytecode into native machine code.",
                        "Checked exceptions are exceptions that must be either caught or declared in the method signature, while unchecked exceptions (runtime exceptions) do not require explicit handling.",
                        "The `try-with-resources` statement automatically closes resources (such as files or streams) when the try block exits.",
                        # Add answers for all 100 questions...
                    ]
                },
                'hard': {
                    'questions': [
                        "What is the Java Memory Model (JMM) and why is it important?",
                        "Explain the concept of `Java Reflection` and provide an example.",
                        "How does the `Java Garbage Collector` work, and what are its types?",
                        "Describe the use of `generics` in Java and their benefits.",
                        "What are `design patterns` in Java? Give examples of some common ones.",
                        "Explain the `Java ClassLoader` and how it works.",
                        "What is `aspect-oriented programming` and how does it relate to Java?",
                        "How does `Java support functional programming` and what features are used?",
                        "What are `Java Streams` and how do they differ from traditional collections?",
                        "Describe the differences between `JVM`, `JRE`, and `JDK`.",
                        # Add up to 100 questions...
                    ],
                    'answers': [
                        "The Java Memory Model defines how threads interact through memory and what behaviors are allowed regarding visibility and ordering of variables.",
                        "Java Reflection allows inspection and modification of classes, methods, and fields at runtime, enabling dynamic behavior and runtime type information.",
                        "The Garbage Collector reclaims memory by removing objects that are no longer referenced. Types include Mark-and-Sweep, Generational Garbage Collection, and G1 (Garbage-First).",
                        "Generics enable type-safe operations and reduce the need for explicit type casting by allowing classes and methods to operate on parameterized types.",
                        "Design patterns are standard solutions to common problems in software design, such as Singleton, Observer, Factory, and Strategy patterns.",
                        "The Java ClassLoader loads classes into the JVM at runtime, enabling dynamic class loading and classpath management.",
                        "Aspect-Oriented Programming (AOP) allows separation of cross-cutting concerns (such as logging) from the main business logic, and can be implemented using frameworks like AspectJ.",
                        "Java supports functional programming through features like lambda expressions, method references, and functional interfaces introduced in Java 8.",
                        "Java Streams provide a high-level API for processing sequences of elements in a functional style, supporting operations like map, filter, and reduce.",
                        "JVM (Java Virtual Machine) executes Java bytecode, JRE (Java Runtime Environment) includes JVM and standard libraries, while JDK (Java Development Kit) includes JRE along with development tools like the compiler.",
                        # Add answers for all 100 questions...
                    ]
                }
            }
        }

    def get_questions_and_answers(self, subject, difficulty, num_questions):
        subject = subject.lower()  # Normalize subject input
        questions = self.questions.get(subject, {}).get(difficulty, {}).get('questions', [])
        answers = self.questions.get(subject, {}).get(difficulty, {}).get('answers', [])

        if len(questions) < num_questions:
            num_questions = len(questions)  # Adjust if not enough questions

        all_data = list(zip(questions, answers))
        selected_data = random.sample(all_data, num_questions)
        selected_questions, selected_answers = zip(*selected_data)

        return selected_questions, selected_answers

    def verify_answer(self, question, answer, user_answer):
        logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

        # Temporarily suppress stdout and stderr
        original_stdout, original_stderr = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = open(os.devnull, 'w')

        os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'API_TOKEN'
        try:
            prompt = f"""Question: {question}
            Answer: {answer}

            System: You are a backend bot that checks the user's answer with the real answer to a question and tells how similar and accurate the user's answer is. Keep the result short and simple, and refer to the real answer only if you don't know, no need to give false information. And do not provide additional information about the answer.

            User answer: {user_answer}
            """

            model = HuggingFaceEndpoint(
                repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
                task="text-generation",
                max_new_tokens=512,
                top_k=30,
                temperature=0.1,
                repetition_penalty=1.03
            )
            result = model.invoke(prompt)
            response = result.split("Answer:")[1].strip() if "Answer:" in result else result.strip()

        finally:
            # Restore stdout and stderr
            sys.stdout, sys.stderr = original_stdout, original_stderr
            del os.environ['HUGGINGFACEHUB_API_TOKEN']
        
        cleaned_response = response.replace("System: ", "")
        return cleaned_response