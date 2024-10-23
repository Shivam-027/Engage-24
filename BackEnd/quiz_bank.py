import random

class QuizBank:
    def __init__(self):
        self.database = {
            'dsa': {
                'MCQs': {
                    'easy': {
                        'questions': [
                            "Which data structure uses LIFO (Last In, First Out)?",
                            "What is the time complexity of binary search?",
                            "What is the basic operation of a stack?",
                            "Which of the following is a non-linear data structure?",
                            "In which case is a linked list preferred over an array?",
                            "Which data structure is used for breadth-first traversal of a graph?",
                            "What is the time complexity of accessing an element in an array?",
                            "Which of the following is a self-balancing binary search tree?",
                            "What is the worst-case time complexity of insertion sort?",
                            "Which of the following is a divide-and-conquer algorithm?",
                            "Which operation in a stack is used to add an element?",
                            "What is the main advantage of a doubly linked list over a singly linked list?",
                            "What does BFS stand for in graph theory?",
                            "Which sorting algorithm has the best average case time complexity?",
                            "What is the main disadvantage of the bubble sort algorithm?",
                            "In a queue, where is the new element inserted?",
                            "Which data structure is best suited for implementing a priority queue?",
                            "What is the primary purpose of hashing?",
                            "Which of the following data structures is used to implement recursion?",
                            "What is the time complexity of finding the maximum element in an unsorted array?",
                            # Add up to 100 questions...
                        ],
                        'options': [
                            ["Queue", "Stack", "Heap", "Array"],
                            ["O(n)", "O(n^2)", "O(log n)", "O(1)"],
                            ["Push", "Pop", "Peek", "Insert"],
                            ["Array", "Linked List", "Graph", "Stack"],
                            ["When frequent insertions and deletions are required", "When random access is required", 
                            "When memory is limited", "When data size is fixed"],
                            ["Stack", "Queue", "Tree", "Graph"],
                            ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
                            ["Binary Tree", "AVL Tree", "Heap", "Queue"],
                            ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
                            ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"],
                            ["Pop", "Push", "Peek", "Enqueue"],
                            ["Easier deletion of the last node", "Easier deletion of the first node", 
                            "Easier traversal in both directions", "Less memory consumption"],
                            ["Breadth-First Search", "Binary-First Search", "Branch-First Search", "Best-First Search"],
                            ["Merge Sort", "Quick Sort", "Bubble Sort", "Heap Sort"],
                            ["High time complexity", "Not stable", "Uses extra space", "Requires recursion"],
                            ["Front", "Rear", "Middle", "Anywhere"],
                            ["Array", "Stack", "Heap", "Queue"],
                            ["To map keys to values", "To store data sequentially", "To sort data", "To reverse data"],
                            ["Queue", "Stack", "Linked List", "Tree"],
                            ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
                            # Add options for all 100 questions...
                        ],
                        'answers': [
                            1, 2, 0, 2, 0, 1, 0, 1, 2, 2, 1, 2, 0, 1, 0, 1, 2, 0, 1, 1, 
                            # Add answers for all 100 questions...
                        ]
                    },
                    'medium': {
                        'questions': [
                            "What is the time complexity of merge sort?",
                            "Which of the following data structures is used to implement recursion?",
                            "In a binary search tree, what is the time complexity of searching for a value?",
                            "Which of the following is an application of a priority queue?",
                            "What is the height of a balanced binary search tree with 'n' nodes?",
                            "Which graph traversal algorithm can be used to find the shortest path in an unweighted graph?",
                            "What is the main disadvantage of the quicksort algorithm?",
                            "Which data structure is used to convert infix to postfix expression?",
                            "What is the purpose of a hash function?",
                            "In which data structure is a double-ended queue implemented?",
                            # Add up to 100 questions...
                        ],
                        'options': [
                            ["O(n log n)", "O(n^2)", "O(log n)", "O(n)"],
                            ["Stack", "Queue", "Linked List", "Tree"],
                            ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
                            ["Task scheduling", "Memory allocation", "Disk scheduling", "All of the above"],
                            ["O(log n)", "O(n)", "O(n^2)", "O(n log n)"],
                            ["DFS", "BFS", "Dijkstra's Algorithm", "A* Algorithm"],
                            ["High time complexity", "Requires extra space", "Not stable", "Worst-case time complexity is O(n^2)"],
                            ["Queue", "Stack", "Array", "Graph"],
                            ["To map keys to values", "To sort data", "To reverse data", "To search data"],
                            ["Queue", "Deque", "Stack", "Priority Queue"],
                            # Add options for all 100 questions...
                        ],
                        'answers': [
                            0, 0, 0, 3, 0, 1, 3, 1, 0, 1, 
                            # Add answers for all 100 questions...
                        ]
                    },
                    'hard': {
                        'questions': [
                            "What is the amortized time complexity of splay tree operations?",
                            "Which graph traversal algorithm can be used to find the shortest path in an unweighted graph?",
                            "What is the time complexity of Dijkstra's algorithm using a priority queue?",
                            "What is the space complexity of merge sort?",
                            "Which of the following is a self-balancing binary search tree?",
                            "Which of the following is true about B-trees?",
                            "In dynamic programming, which of the following problems exhibits optimal substructure?",
                            "Which of the following algorithms is used to detect cycles in a graph?",
                            "What is the purpose of the Knuth-Morris-Pratt algorithm?",
                            "Which of the following is an NP-complete problem?",
                            # Add up to 100 questions...
                        ],
                        'options': [
                            ["O(log n)", "O(1)", "O(n)", "O(n log n)"],
                            ["DFS", "BFS", "Dijkstra's Algorithm", "A* Algorithm"],
                            ["O(V + E)", "O(V^2)", "O(E log V)", "O(V log V)"],
                            ["O(n)", "O(log n)", "O(n log n)", "O(n^2)"],
                            ["AVL Tree", "B-Tree", "Red-Black Tree", "All of the above"],
                            ["B-trees are always full", "B-trees are a type of binary tree", "B-trees are used in databases", "B-trees are used in graphs"],
                            ["Sorting", "Fibonacci Sequence", "Matrix Multiplication", "All of the above"],
                            ["DFS", "BFS", "Kruskal's Algorithm", "Dijkstra's Algorithm"],
                            ["String matching", "Searching in trees", "Sorting", "Dynamic programming"],
                            ["Traveling Salesman Problem", "Sorting", "Finding shortest paths", "Binary Search"],
                            # Add options for all 100 questions...
                        ],
                        'answers': [
                            2, 1, 2, 2, 3, 2, 1, 0, 0, 0,
                            # Add answers for all 100 questions...
                        ]
                    }
                }
            },
            'OS': {
                'MCQs': {
                    'easy': {
                        'questions': [
                            "Which of the following is a type of operating system?",
                            "What is the primary purpose of an operating system?",
                            "Which of the following is not a function of an operating system?",
                            "What is a kernel in an operating system?",
                            "Which of the following is a real-time operating system?",
                            "Which command is used to list files in a directory in UNIX?",
                            "What is the full form of GUI?",
                            "Which of the following is not a system software?",
                            "What is the main function of the command interpreter?",
                            "Which scheduling algorithm assigns the CPU to the process that arrives first?",
                            "What is virtual memory?",
                            "Which of the following is an example of an open-source operating system?",
                            "Which type of operating system is used in mobile phones?",
                            "What is the full form of CPU?",
                            "What does BIOS stand for?",
                            "Which of the following is a multi-user operating system?",
                            "What is the full form of RAM?",
                            "Which of the following is not an operating system?",
                            "What is the function of a file system in an operating system?",
                            "Which of the following is a function of device management?",
                            # Add up to 100 questions...
                        ],
                        'options': [
                            ["Batch OS", "Time-sharing OS", "Distributed OS", "All of the above"],
                            ["To manage hardware and software resources", "To create applications", "To provide an internet connection", "To perform calculations"],
                            ["Memory management", "Process management", "Network management", "Application development"],
                            ["The core of the operating system", "A type of application software", "A hardware component", "A utility program"],
                            ["Windows 10", "Linux", "VxWorks", "MS-DOS"],
                            ["ls", "dir", "cp", "mv"],
                            ["Graphical User Interface", "General User Interface", "Graphics Used Interface", "Group User Interface"],
                            ["Operating system", "Compiler", "Text editor", "Device driver"],
                            ["To execute commands", "To manage memory", "To manage processes", "To perform calculations"],
                            ["First-Come, First-Served (FCFS)", "Shortest Job Next (SJN)", "Round Robin (RR)", "Multilevel Queue"],
                            ["A technique that allows the execution of processes that may not be completely in memory", "A type of physical memory", "A process management technique", "None of the above"],
                            ["Windows", "Linux", "MacOS", "MS-DOS"],
                            ["Embedded OS", "Time-sharing OS", "Real-time OS", "Distributed OS"],
                            ["Central Processing Unit", "Central Programming Unit", "Control Processing Unit", "Control Programming Unit"],
                            ["Basic Input Output System", "Binary Input Output System", "Basic Integrated Operating System", "Binary Integrated Operating System"],
                            ["Windows 10", "UNIX", "Linux", "All of the above"],
                            ["Random Access Memory", "Read Access Memory", "Read And Modify", "Randomized Access Memory"],
                            ["Windows", "Linux", "Oracle", "MacOS"],
                            ["To manage data storage and retrieval", "To provide an internet connection", "To perform calculations", "To execute commands"],
                            ["Managing the hardware resources of the computer", "Managing user applications", "Developing software", "Providing internet access"],
                            # Add options for all 100 questions...
                        ],
                        'answers': [
                            3, 0, 3, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2, 0, 0, 
                            # Add answers for all 100 questions...
                        ]
                    },
                    'medium': {
                        'questions': [
                            "What is the main advantage of a multiprocessor system?",
                            "What is the role of the process scheduler?",
                            "Which of the following is not a process state?",
                            "What is a semaphore in the context of operating systems?",
                            "Which algorithm is used in deadlock avoidance?",
                            "What is the main function of paging in memory management?",
                            "What is the Banker’s algorithm used for?",
                            "What is the primary purpose of a shell in an operating system?",
                            "Which of the following is not a type of memory allocation?",
                            "What is the main function of an interrupt in an operating system?",
                            # Add up to 100 questions...
                        ],
                        'options': [
                            ["Increased throughput", "Increased reliability", "Increased cost", "Both A and B"],
                            ["To manage CPU time allocation to processes", "To manage memory allocation", "To manage file systems", "To manage input/output devices"],
                            ["Ready", "Blocked", "Running", "Swapped"],
                            ["A synchronization tool", "A type of process", "A memory management technique", "A scheduling algorithm"],
                            ["First-Come, First-Served", "Round Robin", "Shortest Job Next", "Banker’s algorithm"],
                            ["To translate logical addresses into physical addresses", "To allocate memory to processes", "To manage files on disk", "To allocate CPU time to processes"],
                            ["To manage memory", "To avoid deadlocks", "To allocate CPU time", "To manage file systems"],
                            ["To manage the execution of commands", "To allocate memory", "To manage processes", "To handle file systems"],
                            ["Contiguous allocation", "Non-contiguous allocation", "Dynamic allocation", "Manual allocation"],
                            ["To handle exceptions", "To allocate memory", "To manage file systems", "To allocate CPU time"],
                            # Add options for all 100 questions...
                        ],
                        'answers': [
                            3, 0, 3, 0, 3, 0, 1, 0, 3, 0, 
                            # Add answers for all 100 questions...
                        ]
                    },
                    'hard': {
                        'questions': [
                            "What is the difference between preemptive and non-preemptive scheduling?",
                            "Explain the working of the Linux kernel.",
                            "What is the role of the dispatcher in process scheduling?",
                            "Describe the working of a monitor in process synchronization.",
                            "What is the difference between paging and segmentation in memory management?",
                            "What are the various methods of inter-process communication (IPC)?",
                            "Explain the working of a virtual memory system.",
                            "What is the difference between a microkernel and a monolithic kernel?",
                            "Explain the concept of context switching in process management.",
                            "What is the difference between a hard real-time system and a soft real-time system?",
                            # Add up to 100 questions...
                        ],
                        'options': [
                            ["Preemptive allows the process to be interrupted, while non-preemptive does not", "Non-preemptive allows the process to be interrupted, while preemptive does not", "Both allow the process to be interrupted", "Neither allows the process to be interrupted"],
                            ["Manages system resources", "Manages memory", "Handles hardware communication", "All of the above"],
                            ["To swap processes in and out of memory", "To handle process transitions", "To allocate CPU time to processes", "To allocate memory to processes"],
                            ["A synchronization construct", "A memory management technique", "A process management technique", "A scheduling algorithm"],
                            ["Paging divides memory into fixed-sized pages, while segmentation divides memory into variable-sized segments", "Segmentation divides memory into fixed-sized pages, while paging divides memory into variable-sized segments", "Both divide memory into fixed-sized pages", "Both divide memory into variable-sized segments"],
                            ["Message passing", "Shared memory", "Pipes", "All of the above"],
                            ["Manages process memory", "Allocates CPU time", "Allows execution of processes that may not be entirely in memory", "Manages file systems"],
                            ["Microkernel handles only essential functions, while monolithic kernel handles everything", "Monolithic kernel handles only essential functions, while microkernel handles everything", "Both handle only essential functions", "Neither handles essential functions"],
                            ["Switching the CPU from one process to another", "Allocating memory to processes", "Handling process creation", "Managing file systems"],
                            ["Hard real-time systems guarantee a response within a fixed time, while soft real-time systems do not", "Soft real-time systems guarantee a response within a fixed time, while hard real-time systems do not", "Both guarantee a response within a fixed time", "Neither guarantees a response within a fixed time"],
                            # Add options for all 100 questions...
                        ],
                        'answers': [
                            0, 3, 1, 0, 0, 3, 2, 0, 0, 0, 
                            # Add answers for all 100 questions...
                        ]
                    }
                }
            }
        }

    def get_quiz_data(self, subject, difficulty, number):
        number = int(number)
        # Fetch questions, options, and answers from the database
        questions = self.database.get(subject, {}).get('MCQs', {}).get(difficulty, {}).get('questions', [])
        options = self.database.get(subject, {}).get('MCQs', {}).get(difficulty, {}).get('options', [])
        answers = self.database.get(subject, {}).get('MCQs', {}).get(difficulty, {}).get('answers', [])
        
        # Zip the questions, options, and answers together
        all_data = list(zip(questions, options, answers))
        
        # Make sure not to exceed the available number of questions
        num_questions = min(number, len(all_data))
        
        # Randomly select the desired number of questions
        selected_data = random.sample(all_data, num_questions)
        
        # Unzip the selected data
        selected_questions, selected_options, selected_answers = zip(*selected_data)
        
        # Prepare the quiz data structure
        quiz_data = [
            {"question": selected_questions[i], "options": selected_options[i], "answer": selected_answers[i]}
            for i in range(num_questions)
        ]
        
        return quiz_data
