class CustomSet{
    constructor(){
        this.items=new Map();
    }
    add(element){
        if(this.items.has(element))
            return false
        this.items.set(element,element);
        return true;
    }
    has(element){
        return this.items.has(element);
    }
    remove(element){
        if(this.items.has(element))
        {
            return this.items.delete(element);
        }
    }
    size(){
        return this.items.size;
    }

    // 'values' function returns the set elements in an array
    values(){
        return [...this.items.keys()];
    }

    union(otherSet){
        const unionSet=new CustomSet();

        this.values().forEach(value =>unionSet.add(value));

        otherSet.values().forEach(value => unionSet.add(value));
        return unionSet;
    }
    intersectionObserver(otherSet){
        const intersectionSet=new CustomSet();

        const smallerSet=this.size() < otherSet.size() ? this:otherSet;
        const largerSet=this.size() < otherSet.size() ? otherSet:this;

        smallerSet.values().forEach(value => {
            if(largerSet.has(value)){
                intersectionSet.add(value);
            }
        });
        return intersectionSet;
    }
}