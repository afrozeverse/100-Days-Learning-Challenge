class Deque{
    constructor(){
        this.items={};
        this.head=0;
        this.tail=0;
    }
    addHead(element){
            this.head--;
            this.items[this.head]=element;
    }
    addTail(element){
        this.items[this.tail]=element;
        this.tail++;
    }
    removeHead(){
        if(this.isEmpty()){
            return undefined;
        }
        const result=this.items[this.head];
        delete this.items[this.head];
        this.head++;
        if(this.isEmpty()){
            this.head=0;
            this.tail=0;
        }
        return result;
    }

    removeTail(){
        if(this.isEmpty()){
            return undefined;
        }
        this.tail--;
        const result=this.items[this.tail];
        delete this.items[this.tail];
        if(this.isEmpty()){
            this.head=0;
            this.tail=0;
        }
        return result;
    }
    peekHead(){
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.head];
    }
    peekTail(){
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.tail-1];
    }
    isEmpty(){
        return this.head===this.tail;
    }
    size(){
        return this.tail-this.head;
    }
}