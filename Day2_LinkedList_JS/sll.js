class Node {
    constructor(data) {
        this.data=data;
        this.next=null;
    }
}

class SinglyLinkedList{
    constructor(){
        this.head=null;
        this.size=0;
    }
    append(data){
        let newNode= new Node(data);
        if(!this.head)
        {
            this.head=newNode;
        }
        else{
            let t=this.head;
            while(t.next) {
                t=t.next;
            } 
            t.next=newNode;
        }
        this.size++;
    }

    prepend(data){
        let newNode=new Node(data);
        newNode.next=this.head;
        this.head=newNode;
        this.size++;
    }

    insertAt(data,index){
        if(index<0 || index>this.size){
            console.error("Invalid index");
            return false;
        }
        if(index==0){
            this.prepend(data);
            return true;
        }
        const newNode=new Node(data);
        let current= this.head;
        let previous=null;
        let count=0;

        while(count<index){
            previous=current;
            current=current.next;
            count++;
        }
        newNode.next=current;
        previous.next=newNode;
        this.size++;
    }
    
    removeAt(index){
        if(index<0 || index>this.size)
            {
                console.error("Invalid index.")
                return null;
            }
            let removeData;
            if(index==0){
                removeData=this.head.data;
                this.head=this.head.next;
            }
            else{
            let current= this.head;
            let previous=null;
            let count=0;
        
            while(count<index){
                previous=current;
                current=current.next;
                count++;
            }
            removeData=current.data;
            previous.next=current.next;
        }
        this.size--;
        return removeData;
    }

    isEmpty(){
        return this.size==0;
    }
    getSize(){
        return this.size;
    }
    printList(){
        if(this.isEmpty())
        {
            console.error("List is empty!")
        }
        else{
            let output='';
            let t=this.head;
            while(t)
            {
                output += t.data + " -> ";
                t=t.next;
            }
            console.log(output + "null");
        }
    }
}

// Driver code
const list = new SinglyLinkedList();
list.prepend(10);
list.insertAt(30,0);
list.append(20);
list.append(40);
list.append(60);
list.append(100);
list.printList();