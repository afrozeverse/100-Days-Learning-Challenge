// Define a Stack class
class Stack {
    constructor() {
        // Initialize an empty array to store stack elements
        this.item = []
    }

    // Push: Add an element to the top of the stack
    push(element) {
        this.item.push(element);
    }

    // Pop: Remove and return the top element from the stack
    pop() {
        if (this.isEmpty())          // If stack is empty, return null
            return null
        return this.item.pop();      // Otherwise, remove and return the top element
    }

    // Peek: Return the top element without removing it
    peek() {
        if (this.isEmpty())          // If stack is empty, return null
            return null
        return this.item[this.item.length - 1];  // Return the last element
    }

    // getSize: Return total number of elements in stack
    getSize() {
        return this.item.length;
    }

    // isEmpty: Check if stack is empty
    isEmpty() {
        return this.item.length === 0;
    }
}

// Create a stack object
s = new Stack()

// Push elements into the stack
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)

// Display size and top element
console.log("Size = ", s.getSize())
console.log("Last element = ", s.peek())

// Remove two elements from the top
s.pop()
s.pop()

// Display top element after popping twice
console.log("Last element (After popping 2 times) = ", s.peek())
