# Build a Task Manager with Python
Build a CLI task manager using linked lists, stacks, queues, and sorting algorithms.

michael jumah

Terminal square icon
DIFFICULTY
easy
TIME
50 min
REFRESHED
10th Jun '26
COST
Free
📣 Whoa! Welcome to our new beta feature!

This is a NextWork project generated with AI. It's a new feature and may have some bugs. If you spot anything, please let us know in our community. We're improving this everyday and really want to hear what you'd like to see us fix next. Happy learning.

30 Second Summary
Every app you use manages data behind the scenes. Whether it's your email inbox processing messages in order or your browser's back button remembering where you've been, data structures are the invisible engines making it all work.

In this project, you will build a command-line Task Manager in Python using data structures you implement from scratch. You'll create your own linked list, stack, and queue, then apply sorting and searching algorithms to manage tasks efficiently.

What You'll Build
A command-line Task Manager application that stores tasks in a custom linked list, tracks undo history with a stack, processes tasks in FIFO order with a queue, and supports sorting by priority and searching by name.

By the end of this project, you'll have:

A custom  that stores, deletes, and traverses tasks.

A  for undo history and a  for processing tasks in order.

 and  algorithms wired into a working CLI application.

Secret Mission: A -based category system that groups tasks and supports instant lookup.

Are there any prerequisites?

This project assumes basic familiarity with Python syntax. You should be comfortable with variables, functions, loops, and conditionals.

No external libraries are needed. The entire project uses only the Python standard library.

👀 Step #0
Before We Start

You are about to build a Task Manager application that runs in your terminal. Instead of relying on Python's built-in list for everything, you will implement your own data structures from scratch.

This step gets your environment ready. You will install , create a project folder, and confirm everything runs.

In this step, get ready to:
Install or verify Python 3.14.
Create your project folder and file.
Confirm Python can run your file.
✍️ What are we doing in this project?
I am building a... using custom data structures like... because...
1000

Tasks still to complete

Return to later
Check your Python version
Python is the programming language your Task Manager will run on. You need version 3.14 or higher installed.

Open your terminal by pressing Cmd+Space (macOS) or the Windows key (Windows), typing Terminal (macOS) or Command Prompt (Windows), and pressing Enter.

Check your Python version by running this command:

bash



python --version
✔️ I see version 3.14 or higher
ⓧ I see an older version
ⓧ Command not found
You should see output like Python 3.14.5. Python is ready to go.

Create your project folder and file
Every project needs a home. You will create a folder on your Desktop so it is easy to find.

Move to your Desktop by running this command:

bash



cd ~/Desktop
Create your project folder and move into it by running these commands:

bash



mkdir task-manager
cd task-manager
Confirm the folder exists by running:

bash



ls
The folder should be empty for now. Next, you will create the Python file and open it in your editor.

Open your code editor by pressing Cmd+Space (macOS) or the Windows key (Windows) to open your search bar.

Type Cursor (recommended) or Visual Studio Code and press Enter to open it.

In your editor, click File in the top menu bar.

Click Open Folder.

Navigate to your Desktop and select the task-manager folder, then click Open.

Create a new file by clicking File then New File.

Save it immediately with Cmd+S (macOS) or Ctrl+S (Windows) and name it task_manager.py.

Why task_manager.py?

Python file names use underscores instead of spaces or hyphens. This keeps imports clean and avoids errors when referencing the file in code.

🙋‍♀️ Don't see the task-manager folder on your Desktop?

Make sure you ran cd ~/Desktop before mkdir task-manager. If the folder ended up elsewhere, delete it and rerun both commands in order.



Verify Python runs your file
A quick test confirms that Python can see and execute your file. Since the file is empty, a successful run produces no output and no errors.

In your terminal, make sure you are inside the task-manager folder. Run your file with this command:

bash



python task_manager.py
If everything is set up correctly, the command finishes silently with no output. That means Python found and executed the empty file without errors.

Seeing a "No such file or directory" error?

This means your terminal is not inside the task-manager folder. Run cd ~/Desktop/task-manager and try the command again.



📸 Take a screenshot of your editor with task_manager.py open.
No file chosen
PNG or JPG (max. 10MB)




Tasks still to complete

Return to later
Your environment is ready. Next up, you will build a custom linked list from scratch to store tasks in your Task Manager.

🔧 Step #1
Set Up Python and Your Project

Before building any data structures, you need to confirm that your  environment can actually run code from a file.

A quick test script proves that Python is installed, on your PATH, and able to execute your project file. Once that works, you are ready to start building.

In this step, get ready to:
Write a test print statement in your project file.
Run the file from the terminal and confirm output appears.
✍️ What are we doing in this step?
In this step, I'm setting up... so that I can...
1000

Tasks still to complete

Return to later
Write and run a test script
The simplest way to verify your environment is to write a one-line script that prints a message. If you see that message in the terminal, everything is wired up correctly.

In your task_manager.py file (already open in your editor), add the following code:

task_manager.py
python



print("Task Manager setup complete!")
What does this code do?

The print() function outputs text to the terminal. If you see the message after running the script, it confirms Python can find and execute your file.

Save task_manager.py.

Run the script by entering this command in your terminal:

bash



python task_manager.py
You should see Task Manager setup complete! printed in the terminal.

Don't see the output?

Make sure you saved the file before running the command. Unsaved changes will not be picked up.

Confirm your terminal is inside the task-manager folder. Run cd task-manager if you are in the wrong directory.

If you see python: command not found, try python3 task_manager.py instead. Some systems use python3 as the default command.



✔️ Awesome, I've got everything!
ⓧ I'd like to double check the full code
Great. Double check you have saved your file before moving on.

📸 Take a screenshot of your terminal showing the output of python task_manager.py.
No file chosen
PNG or JPG (max. 10MB)


Tasks still to complete

Return to later
Your environment is ready. Next up, you will build a custom linked list from scratch to store and manage tasks.

🔍 Step #2
Build the Linked List

Your project folder and Python environment are ready. Now it's time to build the first core data structure for your Task Manager: a .

A linked list stores data in a chain of nodes. Each node holds a piece of data and a pointer to the next node. Unlike Python's built-in list (which uses a contiguous array), a linked list lets you insert and delete items without shifting everything around.

In this step, get ready to:
Build a custom Node class and LinkedList class from scratch.
Add methods to insert, delete, display, find, and convert tasks.
Verify your linked list works by testing with sample data.
✍️ What are we doing in this step?
In this step, I'm building... so that I can...
1000

Tasks still to complete

Return to later
Create the Node and LinkedList classes
The linked list needs two building blocks. A Node holds a task's data and a reference to the next node. The LinkedList manages the chain by tracking the head (first node).

Delete everything in task_manager.py (the test print statement from earlier).

Add the Node class and the beginning of the LinkedList class by copying this code:

task_manager.py
python



# --- Node and Linked List ---

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
What does this code do?

Node.__init__ stores the task data and sets self.next to None (no next node yet).

LinkedList.__init__ starts with self.head = None (empty list, no nodes).

append creates a new Node, then walks the chain to find the last node and attaches the new one there. If the list is empty, the new node becomes the head.

Save task_manager.py.

Run python task_manager.py in your terminal. You should see no output (the script loads without errors).

Seeing a SyntaxError?

Check that your indentation uses consistent spaces (4 spaces per level, no tabs mixed in).

Make sure class Node: and class LinkedList: are at the top level (no leading spaces).



Add the delete method inside the LinkedList class, below the append method:

task_manager.py
python



    def delete(self, task_name):
        if not self.head:
            return None
        if self.head.data["name"] == task_name:
            removed = self.head.data
            self.head = self.head.next
            return removed
        current = self.head
        while current.next:
            if current.next.data["name"] == task_name:
                removed = current.next.data
                current.next = current.next.next
                return removed
            current = current.next
        return None
What does delete do?

First checks if the list is empty. If so, returns None.

If the head node matches the target name, it removes the head by pointing self.head to the next node.

Otherwise, it walks the chain looking for a node whose next node matches the target. When found, it "skips over" that node by linking the current node directly to the one after it.

Returns the removed task's data, or None if the name wasn't found.

Save task_manager.py and run python task_manager.py. You should see no output and no errors.

Getting an IndentationError?

The delete method must be indented one level inside the LinkedList class (4 spaces before def).

Lines inside delete need 8 spaces of indentation (4 for the class, 4 for the method body).



Add the display and length methods below delete:

task_manager.py
python



    def display(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.data)
            current = current.next
        return tasks

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
What do these methods do?

display walks the entire chain, collecting each node's data into a Python list, then returns it. This gives you a snapshot of all tasks.

length walks the chain and counts how many nodes it visits. Both methods are O(n) because they must touch every node.

Save task_manager.py and run python task_manager.py. No output means no syntax errors.

Script throws a NameError?

Make sure display and length are indented inside the LinkedList class, at the same indentation level as append and delete.



Add the to_list method and test your linked list
Later steps need to convert the linked list into a standard Python list for sorting and searching. The to_list method handles this conversion.

Add the to_list method below length, then add temporary test code at the bottom of the file to verify everything works:

task_manager.py
python



    def to_list(self):
        return self.display()


# --- Test Code (temporary) ---
task_list = LinkedList()
task_list.append({"name": "Write report", "priority": 2, "status": "pending"})
task_list.append({"name": "Buy groceries", "priority": 1, "status": "pending"})
task_list.append({"name": "Call dentist", "priority": 3, "status": "pending"})
task_list.append({"name": "Fix bug", "priority": 1, "status": "pending"})

print("All tasks:")
for task in task_list.display():
    print(f"  {task['name']} (priority {task['priority']})")

print(f"\nTotal tasks: {task_list.length()}")

deleted = task_list.delete("Call dentist")
print(f"\nDeleted: {deleted['name']}")

print("\nRemaining tasks:")
for task in task_list.display():
    print(f"  {task['name']} (priority {task['priority']})")

print(f"\nAs Python list: {task_list.to_list()}")
What does this test code do?

Creates a LinkedList and appends 4 task dictionaries, each with name, priority, and status keys.

Calls display() to print all tasks, then deletes one by name, and displays the remaining tasks.

to_list() calls display() internally. It exists as a semantic alias because later steps will need a clear "convert to Python list" operation for sorting and searching.

Save task_manager.py and run python task_manager.py.

You should see all 4 tasks printed, then "Deleted: Call dentist", followed by only 3 remaining tasks.

Output shows 4 tasks after deletion?

Double-check that you typed "Call dentist" exactly (case-sensitive) in the delete call to match the name you used in append.

Make sure the second display() call appears AFTER the delete() call in your test code.



Add the find method
Sometimes you need to look up a specific task without deleting it. The find method searches by name and returns the task data if it exists.

In task_manager.py, scroll to the LinkedList class and find the end of the delete method (the line return None at the bottom of delete).

Add the find method directly below delete and above display:

task_manager.py
python



    def find(self, task_name):
        current = self.head
        while current:
            if current.data["name"] == task_name:
                return current.data
            current = current.next
        return None
What does find do?

find starts at the head and checks each node's name against the target.

If a match is found, it returns that node's data immediately.

If it reaches the end without a match, it returns None.

💡 Why is this O(n)?

In the worst case, find visits every single node before locating the target (or confirming it doesn't exist). That means performance scales linearly with the number of tasks.

Later in this project, you'll implement  as a faster O(log n) alternative. The tradeoff is that binary search requires sorted data, while find works on any unsorted linked list.

Now update the test code at the bottom of the file. Find the line that says print(f"\nAs Python list: {task_list.to_list()}") and add these lines above it:

task_manager.py
python



found = task_list.find("Buy groceries")
print(f"\nFound: {found}")

not_found = task_list.find("Call dentist")
print(f"Search for deleted task: {not_found}")
Save task_manager.py and run python task_manager.py.

You should see Found: {'name': 'Buy groceries', 'priority': 1, 'status': 'pending'} and Search for deleted task: None in the output.

find returns None for a task you know exists?

Check that the name string in find("Buy groceries") matches exactly what you used in append (case-sensitive).

Make sure the find method is indented inside the LinkedList class, not at the top level.



📸 Take a screenshot of your terminal showing the test output with tasks added, one deleted, and the find results.
No file chosen
PNG or JPG (max. 10MB)




Tasks still to complete

Return to later
Now remove the temporary test code. Delete everything below the to_list method (the entire # --- Test Code (temporary) --- section and all lines after it).

Save task_manager.py.

✔️ Awesome, I've got everything!
ⓧ I'd like to double check the full code
Great. Double-check you've saved the file with only the Node and LinkedList classes (no test code remaining at the bottom).

Your linked list is fully operational. Next up, you'll build a stack for undo history and a queue for task processing. These two structures will give your Task Manager the ability to reverse mistakes and handle tasks in order.

✨ Step #3
Build the Stack and Queue

Your linked list stores tasks perfectly. But a real task manager needs more than just storage. It needs to remember what you did (so you can undo it) and process tasks in the right order.

Two classic data structures solve these problems. A  tracks your action history for undo. A  manages your task inbox so tasks are processed in the order they arrived. You'll build both from scratch in this step.

In this step, get ready to:
Build a Stack class with LIFO (Last In, First Out) ordering.
Build a Queue class with FIFO (First In, First Out) ordering.
Test both to confirm they process items in the correct order.
✍️ What are we doing in this step?
In this step, I'm building... so that I can...
1000

Tasks still to complete

Return to later
Implement the Stack class
A stack follows the Last In, First Out (LIFO) principle. Think of it like a stack of plates. The last plate you place on top is the first one you take off.

This makes stacks perfect for undo functionality. When you undo, you always reverse the most recent action first.

In task_manager.py, add the Stack class below your LinkedList class by copying this code:

task_manager.py
python



# --- Stack (LIFO) ---

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # Add item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # Look at the top item without removing it
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # Check if stack has no items
        return len(self.items) == 0
What does this code do?

push adds an item to the end of the internal list (the "top" of the stack).

pop removes and returns the last item added. This is why it's Last In, First Out.

peek lets you see the top item without removing it.

is_empty prevents errors by checking whether there's anything to pop or peek at.

Save task_manager.py.

You won't see a change yet. The test code in the next substep confirms everything works.

Seeing a syntax error?

Make sure the Stack class starts after the to_list method of your LinkedList class, with a blank line separating them.

Check that all methods inside the class are indented by exactly 4 spaces.



Implement the Queue class
A queue follows the First In, First Out (FIFO) principle. Think of it like a line at a coffee shop. The first person who joins the line is the first one served.

This makes queues perfect for a task inbox. Tasks get processed in the order they arrive, not the order they were most recently added.

In task_manager.py, add the Queue class below your Stack class by copying this code:

task_manager.py
python



# --- Queue (FIFO) ---

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add item to the back of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front item
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        # Look at the front item without removing it
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Check if queue has no items
        return len(self.items) == 0
What does this code do?

enqueue adds an item to the back of the list (the "end" of the line).

dequeue removes and returns the first item in the list. This is why it's First In, First Out.

peek lets you see the front item without removing it.

items.pop(0) removes from index 0 (the front). This is simple and clear for learning purposes.

Save task_manager.py.

You won't see a change yet. The next substep tests both classes together.

Seeing an indentation error?

Make sure the Queue class starts after the is_empty method of your Stack class, with a blank line separating them.

Check that you didn't accidentally nest the Queue class inside the Stack class. Both should be at the same indentation level (no indent).



Test both data structures
Time to prove that your stack and queue actually work. You'll add temporary test code that pushes and pops items, then enqueues and dequeues items, printing the results so you can see the ordering.

Add this temporary test code at the very bottom of task_manager.py (below the Queue class):

task_manager.py
python



# --- Temporary Test Code (delete after verifying) ---

print("=== Stack Test (LIFO) ===")
stack = Stack()
stack.push("Action 1: Added 'Buy groceries'")
stack.push("Action 2: Added 'Walk the dog'")
stack.push("Action 3: Added 'Read a book'")

print("Popping from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\n=== Queue Test (FIFO) ===")
queue = Queue()
queue.enqueue("Task 1: Buy groceries")
queue.enqueue("Task 2: Walk the dog")
queue.enqueue("Task 3: Read a book")

print("Dequeuing from queue:")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
What should I see?

The stack pops in reverse order: Action 3 first, then Action 2, then Action 1. The last item pushed is the first one popped.

The queue dequeues in insertion order: Task 1 first, then Task 2, then Task 3. The first item enqueued is the first one dequeued.

Save task_manager.py.

Run the script by entering this command in your terminal:

bash



python task_manager.py
You should see the stack output in reverse order (Action 3, then 2, then 1) and the queue output in insertion order (Task 1, then 2, then 3).

Seeing a NameError?

A NameError: name 'Stack' is not defined means your test code can't find the Stack class. Make sure the test code is below both class definitions in the same file.

Check that you don't have any extra indentation on the test code. It should be at the top level (no indent), not inside a class.

If you see IndentationError, make sure the Queue class ended properly before the test code starts.



Once you've confirmed the output is correct, delete the temporary test code (everything below the # --- Temporary Test Code comment) from task_manager.py.

Save task_manager.py again.

Why LIFO for undo and FIFO for task processing?

When you undo actions, you always want to reverse the most recent one first. That's LIFO. If you added three tasks and want to undo, you undo the third add first, then the second, then the first.

When you process tasks from an inbox, you want to handle the oldest one first. That's FIFO. The task that's been waiting longest gets processed next.

✔️ Awesome, I've got everything!
ⓧ I'd like to double check the full code
Great. Double check you've saved your file with the test code removed.

📸 Take a screenshot of your terminal showing the stack and queue test output.
No file chosen
PNG or JPG (max. 10MB)




Tasks still to complete

Return to later
Your stack and queue are working perfectly. Next up, you'll implement merge sort and binary search to organize and find tasks at lightning speed.

📝 Step #4
Implement Sorting and Searching

Your  stores tasks, your stack tracks undo history, and your queue manages the inbox. But right now, there's no way to organize or quickly find tasks.

In this step, you'll implement two classic algorithms.  will organize tasks by priority.  will let you find a specific task by name almost instantly.

In this step, get ready to:
Implement merge sort to order tasks by priority.
Implement binary search to find tasks by name in O(log n) time.
Wire both algorithms into your linked list workflow and verify the output.
✍️ What are we doing in this step?
In this step, I'm implementing... so that I can...
1000

Tasks still to complete

Return to later
Implement the merge sort algorithm
Merge sort uses a divide-and-conquer strategy. It splits a list in half repeatedly until each piece has one item, then merges the pieces back together in sorted order.

This guarantees O(n log n) performance regardless of the input order. That means even in the worst case, merge sort stays efficient.

In task_manager.py, scroll to the bottom of the file (below the Queue class).

Add the merge sort functions by copying the following code:

task_manager.py
python



# --- Merge Sort ---

def merge_sort(tasks):
    # Base case: a list of 0 or 1 items is already sorted
    if len(tasks) <= 1:
        return tasks

    # Split the list in half
    mid = len(tasks) // 2
    left = merge_sort(tasks[:mid])
    right = merge_sort(tasks[mid:])

    # Merge the sorted halves back together
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements from both halves and add the smaller one
    while i < len(left) and j < len(right):
        if left[i]["priority"] <= right[j]["priority"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from either half
    result.extend(left[i:])
    result.extend(right[j:])
    return result
What does this code do?

merge_sort recursively splits the task list in half until each piece contains one item. Then it calls merge to reassemble the pieces in priority order.

The merge function walks through both halves simultaneously, always picking the task with the lower priority number (1 = highest priority). This "compare and pick" approach is what gives merge sort its guaranteed O(n log n) speed.

💡 Why merge sort over other sorting algorithms?

Merge sort has a guaranteed O(n log n) worst case. Other popular algorithms like quicksort can degrade to O(n²) with unlucky input. For a learning project, merge sort is easier to reason about because its performance is predictable.

Save task_manager.py.

You won't see a change yet. The next chunk adds binary search, and then you'll test both together.

Implement binary search
Binary search works by repeatedly cutting a sorted list in half. Instead of checking every single task (O(n) linear search), it eliminates half the remaining options with each comparison. This gives it O(log n) performance.

Why does binary search need a sorted list?

Binary search decides whether to look left or right based on alphabetical order. If the list isn't sorted, it has no way to know which half the target is in. This is also why you can't binary search a linked list directly. Linked lists have no random access, so you can't jump to the middle.

That's why the to_list method you built earlier is important. It converts your linked list into a Python list that can be sorted and searched.

Below your merge function, add the binary search function by copying this code:

task_manager.py
python



# --- Binary Search ---

def binary_search(sorted_tasks, target_name):
    low = 0
    high = len(sorted_tasks) - 1

    while low <= high:
        # Find the middle index
        mid = (low + high) // 2
        mid_name = sorted_tasks[mid]["name"].lower()

        # Check if we found the target
        if mid_name == target_name.lower():
            return sorted_tasks[mid]
        # If target comes after mid alphabetically, search right half
        elif mid_name < target_name.lower():
            low = mid + 1
        # If target comes before mid, search left half
        else:
            high = mid - 1

    # Target not found
    return None
What does this code do?

low and high track the boundaries of the search window. Each loop iteration compares the middle element to the target name (case-insensitive).

If the middle element matches, you've found the task. If the target comes alphabetically after the middle, move low up to search the right half. If it comes before, move high down to search the left half. The function returns None if the task doesn't exist.

Save task_manager.py.

You won't see a change yet. The next chunk wires both algorithms together and runs them.

Test sorting and searching together
Now you'll connect both algorithms to your linked list. The workflow is: convert the linked list to a Python list, sort it with merge sort, then search it with binary search.

At the very bottom of task_manager.py, add the following test code:

task_manager.py
python



# --- Test sorting and searching ---

task_list = LinkedList()
task_list.append({"name": "Write report", "priority": 3, "status": "pending"})
task_list.append({"name": "Fix bug", "priority": 1, "status": "pending"})
task_list.append({"name": "Team meeting", "priority": 2, "status": "pending"})
task_list.append({"name": "Code review", "priority": 5, "status": "pending"})

# Convert linked list to a regular list and sort by priority
tasks = task_list.to_list()
sorted_tasks = merge_sort(tasks)

print("Tasks sorted by priority:")
for t in sorted_tasks:
    print(f"  {t['name']} (priority {t['priority']})")

# Sort alphabetically by name for binary search
sorted_by_name = sorted(sorted_tasks, key=lambda t: t["name"].lower())

# Search for an existing task
result = binary_search(sorted_by_name, "Fix bug")
if result:
    print(f"\nSearch for 'Fix bug': Found! Priority {result['priority']}")

# Search for a non-existent task
result = binary_search(sorted_by_name, "Go shopping")
if result is None:
    print("Search for 'Go shopping': Not found.")
What does this test code do?

First, it creates a linked list with four tasks that have shuffled priorities. Then it converts to a list and runs merge_sort to sort by priority number.

For binary search, it sorts alphabetically by name (binary search requires sorted input). It then searches for a task that exists ("Fix bug") and one that doesn't ("Go shopping") to confirm both paths work.

Save task_manager.py.

Run the script by entering this command in your terminal:

bash



python task_manager.py
You should see the tasks printed in priority order (Fix bug first, Code review last). The search for "Fix bug" should return a result, and the search for "Go shopping" should print "Not found."

Seeing a NameError or unexpected output?

If you see NameError: name 'merge' is not defined, make sure the merge function is defined below merge_sort but above the test code.

If tasks aren't sorting correctly, check that the merge function compares left[i]["priority"] and right[j]["priority"] with the correct dictionary key.

If binary search never finds anything, confirm you're sorting by name (alphabetically) before searching, not by priority.



Once you've confirmed the output is correct, delete all the test code you just added (everything below the # --- Test sorting and searching --- comment).

Save task_manager.py.

Why remove the test code?

In the next step, you'll build a proper CLI menu that uses these algorithms. The test code was just to verify everything works before wiring it into the real application.

✔️ Awesome, I've got everything!
ⓧ I'd like to double check the full code
Great. Make sure you've saved your file with the test code removed.

📸 Take a screenshot of your terminal showing the sorted tasks and search results.
No file chosen
PNG or JPG (max. 10MB)




Tasks still to complete

Return to later
Your algorithms are working. You can now sort tasks by priority and find them by name in logarithmic time. Next up, you'll tie everything together into a real command-line interface that makes all of these data structures usable.

🚀 Step #5
Build the CLI Menu

You have all the building blocks ready. Your LinkedList stores tasks, your Stack tracks history, your Queue manages processing order, and your algorithms sort and search efficiently.

Now you need a way for users to actually interact with all of this. In this step, you will build a command-line menu that ties every data structure together into a usable application.

In this step, get ready to:
Create a main function with a looping menu.
Wire each menu option to the appropriate data structure.
Add input validation and handle edge cases.
✍️ What are we doing in this step?
In this step, I'm building... so that I can...
1000

Tasks still to complete

Return to later
Create the main function and menu loop
Every CLI application needs a loop that keeps running until the user decides to exit. Your main() function will create instances of each data structure and then repeatedly display a menu of choices.

In task_manager.py, scroll to the very bottom of the file (below the binary_search function).

Add the main function skeleton by copying this code:

task_manager.py
python



# --- Main Application ---

def main():
    # Create instances of each data structure
    task_list = LinkedList()
    undo_stack = Stack()
    task_queue = Queue()

    # Welcome banner
    print("=" * 40)
    print("  TASK MANAGER - Data Structures Demo")
    print("=" * 40)

    # Main menu loop - runs until user chooses Exit
    while True:
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Undo Last Action")
        print("5. Process Next Task (Queue)")
        print("6. Sort Tasks by Priority")
        print("7. Search Task by Name")
        print("8. Exit")

        choice = input("\nChoose an option (1-8): ").strip()
What does this code do?

This skeleton sets up the application's core loop.

task_list, undo_stack, and task_queue are live instances of the classes you built in previous steps.

while True: keeps the menu visible until the user explicitly picks Exit.

.strip() removes accidental whitespace from the user's input.

Save task_manager.py.

You will not run this yet because the menu options are not wired up. The next chunk adds the actual functionality.

Wire each menu option to your data structures
Each menu option maps directly to a data structure method you already built. Adding a task touches all three structures: it appends to the linked list, enqueues to the task queue, and pushes a record to the undo stack.

Directly below the choice = input(...) line, add the following code for options 1 through 4:

task_manager.py
python



        if choice == "1":
            name = input("Task name: ").strip()
            if not name:
                print("Task name cannot be empty.")
                continue
            try:
                priority = int(input("Priority (1=highest, 5=lowest): ").strip())
            except ValueError:
                print("Priority must be a number.")
                continue
            # Store task as a dictionary with name, priority, and status
            task = {"name": name, "priority": priority, "status": "pending"}
            task_list.append(task)
            task_queue.enqueue(task)
            undo_stack.push({"action": "add", "task": task})
            print(f"Added: '{name}' with priority {priority}")

        elif choice == "2":
            tasks = task_list.display()
            if not tasks:
                print("No tasks found.")
            else:
                # Formatted table output
                print(f"\n{'Name':<20} {'Priority':<10} {'Status':<10}")
                print("-" * 40)
                for t in tasks:
                    print(f"{t['name']:<20} {t['priority']:<10} {t['status']:<10}")

        elif choice == "3":
            name = input("Task name to delete: ").strip()
            removed = task_list.delete(name)
            if removed:
                # Track deletion for undo
                undo_stack.push({"action": "delete", "task": removed})
                print(f"Deleted: '{name}'")
            else:
                print(f"Task '{name}' not found.")

        elif choice == "4":
            last_action = undo_stack.pop()
            if not last_action:
                print("Nothing to undo.")
            elif last_action["action"] == "add":
                # Reverse an add by deleting the task
                task_list.delete(last_action["task"]["name"])
                print(f"Undid add: removed '{last_action['task']['name']}'")
            elif last_action["action"] == "delete":
                # Reverse a delete by re-adding the task
                task_list.append(last_action["task"])
                print(f"Undid delete: restored '{last_action['task']['name']}'")
What does this code do?

Option 1 (Add Task) validates the input, creates a task dictionary, then stores it in all three data structures. The undo stack records the action type so it knows how to reverse it later.

Option 2 (View Tasks) calls display() to traverse the linked list and prints a formatted table.

Option 3 (Delete Task) removes the task from the linked list and pushes a "delete" record to the stack so it can be undone.

Option 4 (Undo) pops the most recent action from the stack and reverses it. If the last action was "add", it deletes. If it was "delete", it re-appends.

Save task_manager.py.

Now add options 5 through 8, plus a catch-all for invalid input. These use your queue, merge sort, and binary search.

Directly below the elif choice == "4" block you just added, paste the following code:

task_manager.py
python



        elif choice == "5":
            task = task_queue.dequeue()
            if task:
                print(f"Processing: '{task['name']}' (priority {task['priority']})")
            else:
                print("Task queue is empty.")

        elif choice == "6":
            tasks = task_list.to_list()
            if not tasks:
                print("No tasks to sort.")
            else:
                # Use merge sort to order by priority
                sorted_tasks = merge_sort(tasks)
                print(f"\n{'Name':<20} {'Priority':<10} {'Status':<10}")
                print("-" * 40)
                for t in sorted_tasks:
                    print(f"{t['name']:<20} {t['priority']:<10} {t['status']:<10}")

        elif choice == "7":
            tasks = task_list.to_list()
            if not tasks:
                print("No tasks to search.")
            else:
                # Sort alphabetically first (binary search requires sorted input)
                sorted_by_name = sorted(tasks, key=lambda t: t["name"].lower())
                target = input("Search task name: ").strip()
                result = binary_search(sorted_by_name, target)
                if result:
                    print(f"Found: '{result['name']}' | Priority: {result['priority']} | Status: {result['status']}")
                else:
                    print(f"Task '{target}' not found.")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-8.")


if __name__ == "__main__":
    main()
What does this code do?

Option 5 (Process Queue) calls dequeue() to pull the oldest task from the front of the queue. This demonstrates FIFO ordering.

Option 6 (Sort) converts the linked list to a Python list, then runs your merge sort to display tasks ordered by priority.

Option 7 (Search) first sorts tasks alphabetically (binary search requires sorted input), then searches for the target name in O(log n) time.

if __name__ == "__main__": ensures main() only runs when you execute the file directly, not when importing it.

Save task_manager.py.

Why does binary search need a separate sorted list?

Your linked list stores tasks in insertion order, not alphabetical order. Binary search only works on sorted data because it relies on eliminating half the remaining items at each step.

The code converts the linked list to a Python list, sorts it alphabetically, then passes that sorted list to binary_search(). This is a common pattern: choose the right data structure for each operation.

🙋‍♀️ Seeing an indentation error?

All the if/elif blocks must be indented 8 spaces (two levels) because they sit inside while True: which is itself inside def main():.

Make sure you did not mix tabs and spaces. Python requires consistent indentation throughout a file.

Check that the if __name__ == "__main__": line is at the leftmost column (zero indentation). It lives outside any function.



✔️ Awesome, I've got everything!
ⓧ I'd like to double check the full code
Great. Double check you have saved your file before moving on.

Test the complete application
Every menu option includes edge case handling. If the stack is empty when the user tries to undo, the app prints a clear message instead of crashing. The same applies to an empty queue or searching with no tasks.

Run your Task Manager by executing this command in your terminal:

bash



python task_manager.py
You should see the welcome banner and menu appear. Now test each data structure by following this sequence.

Choose option 1 and add a task named Write report with priority 3.

Add a second task named Fix bug with priority 1.

Add a third task named Read docs with priority 2.

Choose option 6 to sort tasks by priority. You should see Fix bug (priority 1) at the top.

Choose option 7 and search for Fix bug. You should see its details printed.

Choose option 4 to undo. The last task you added (Read docs) should be removed.

Choose option 5 to process the next task from the queue. The first task you added (Write report) should be processed because it was enqueued first.

Choose option 8 to exit.

Why does the queue process a different task than expected?

The queue uses FIFO (first in, first out) ordering. It processes tasks in the order they were added, regardless of priority. The stack uses LIFO (last in, first out), so undo removes the most recently added task.

This is the key difference between the two structures. The queue preserves insertion order. The stack reverses it.

🙋‍♀️ Program crashes or shows unexpected behavior?

If you see NameError: name 'merge_sort' is not defined, make sure the main() function is defined below all your class and function definitions in the file.

If nothing happens when you run the file, confirm that if __name__ == "__main__": main() is at the very bottom of the file with no indentation.

If searching returns "Not found" for a task you just added, check that you typed the name exactly as you entered it. The search is case-insensitive but spelling must match.



📸 Take a screenshot of your terminal showing the Task Manager menu and at least one successful operation (like adding or sorting tasks).
No file chosen
PNG or JPG (max. 10MB)




Tasks still to complete

Return to later
💎 SECRET MISSION
Add a Category Hash Map

Your Task Manager stores, sorts, and searches tasks. But what if you want to instantly see all your "work" tasks or all your "personal" tasks? Right now, you would have to scan every single task. In this secret mission, you will build a hash map-based category system that gives you O(1) lookup by category.

keyhole
🤫 Secret Mission
Ready for a challenge? Secret Missions are for students looking to showcase more advanced skills.


Jump in!
🗑 Before you go
Clean Up Your Resources

Decide whether to keep your resources running, pause them to come back later, or delete them entirely. This project runs entirely locally with no external dependencies, so there are no ongoing costs.

Resources you used:

The task-manager folder on your Desktop containing task_manager.py.
✔️ Keep everything running
✋ Pause - I'll come back to this later
ⓧ Delete - I don't want to use this again
No action needed. Choose this if you're still actively building or want to revisit the project later.

Your task-manager folder stays on your Desktop.

You can run the script anytime with python task_manager.py.

Python remains installed on your machine for future projects.

✍️ What were the key tools and concepts you learnt in this project?
The key tools I used include... Key concepts I learnt include...
1000



Tasks still to complete

Return to later
🎉 Mission Accomplished
Nice Work!

Nice work! You just built a fully functional Task Manager CLI in Python, powered entirely by data structures you implemented from scratch.

You've learned how to:

Build a custom linked list from scratch with insert, delete, traverse, and find operations, and wire it into a real application.

Implement a stack (LIFO) for undo history and a queue (FIFO) for task processing, demonstrating how each structure's access pattern solves a different problem.

Apply merge sort (O(n log n)) to sort tasks by priority and binary search (O(log n)) to find tasks by name, combining them into a working CLI application.

Secret Mission: Added a hash map-based category system with O(1) lookup for instant task grouping.

Ready to quiz yourself?

Python Task Manager Concepts
5 questions
2.5 minutes
Test your understanding of linked lists, stacks, queues, and classic search/sort algorithms implemented from scratch.


















