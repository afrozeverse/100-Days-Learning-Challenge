class Queue {
    constructor() {
        this.items = []
    }
    enqueue(element) {
        if (element) {
            return this.items.push(element)
        }
        return null;
    }
    dequeue(element) {
        if (this.isEmpty) {
            return null;
        }
        return this.items.shift();
    }
    grtFront() {
        if (this.isEmpty()) {
            return null;
        }
        return this.items[0];
    }

    getRear() {
        if (this.isEmpty()) {
            return null;
        }
        return this.items[(this.items.length - 1)];
    }
    isEmpty() {
        return this.items.length === 0
    }
    getSize() {
        return this.items.length
    }
}