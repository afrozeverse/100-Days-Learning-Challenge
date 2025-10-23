class MinHeap {
    constructor() {
        this.heap = [];
    }
    size() {
        return this.heap.length;
    }
    getParentIndex(index) {
        return Math.floor((index - 1) / 2)
    }
    getRightChildIndex(index) {
        return (2 * index) + 2
    }
    getLeftChildIndex(index) {
        return (2 * index) + 1
    }
    swap(index1, index2) {
        [this.heap[index1], this.heap[index2]] = [this.heap[index2], this.heap[index1]]
    }
    bubbleUp(index) {
        let currentIndex = this.index;
        while (currentIndex > 0) {
            const parentIndex = this.getParentIndex(currentIndex);
            if (this.heap[currentIndex].priority < this.heap[parentIndex].priority) {
                this.swap(currentIndex, parentIndex);
                currentIndex = parentIndex;
            }
            else {
                break;
            }
        }
    }
    sinkDown(index) {
        let currentIndex = index;
        const lastIndex = this.heap.length - 1;

        while (true) {

            let rightChildIndex = this.getRightChildIndex(currentIndex);
            let leftChildIndex = this.getLeftChildIndex(currentIndex);
            let swapIndex = null;
            if (leftChildIndex <= lastIndex) {
                if (this.heap[leftChildIndex].priority < this.heap[currentIndex].priority) {
                    this.swapIndex = leftChildIndex;
                }
            }
            if (rightChildIndex <= lastIndex) {
                const isRightHigherPriority=swapIndex===null || this.heap[rightChildIndex].priority<this.heap[swapIndex].priority;
                if (isRightHigherPriority) {
                    swapIndex = rightChildIndex;
                }
            }
            if (swapIndex === null) {
                break;
            }
            this.swap(currentIndex, swapIndex);
            currentIndex = swapIndex;

        }
    }

    insert(value) {
        this.heap.push(value);
        this.bubbleUp(this.heap.length - 1)
    }

    // deletion always done to the root node. hence we dont need the value as an argument.
    extractMin() {
        // if the heap is empty
        if (this.heap.length === 0) {
            return null;
        }

        // if the heap has single element
        if (this.heap.length === 1) {
            return this.heap.pop();
        }

        // if the element has more than 1 element

        // the root node is swapped with the last node, for ease of deletion
        this.swap(0, this.heap.length - 1);
        const minValue = this.heap.pop();
        // now the the new root node's value may not be appropriate, hence we have to sink it down
        this.sinkDown(0)
        return minValue;
    }

    peek() {
        return (this.heap.length === 0) ? null : this.heap[0];
    }
}

class PriorityQueue{
    constructor(){
        this.minHeap=new MinHeap();
    }
    isEmpty(){
        return this.minHeap.size()===0;
    }
    size(){
        return this.minHeap.size();
    }
    enqueue(data,priority){
        const newItem={data,priority};
        this.minHeap.insert(newItem);
    }
    dequeue(){
        return this.minHeap.extractMin();
    }
    peek(){
        return this.minHeap.peek();
    }
}