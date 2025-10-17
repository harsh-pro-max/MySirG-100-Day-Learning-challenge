class Stack{
    constructor(){
        this.items=[]
    }
    push(element){
        this.items.push(element);
    }
    peek(){
        if(this.isEmpty()){
            return null;
        }
        return this.items[this.items.length-1];
    }
    pop(){
        if(this.isEmpty()){
            return null;
        }
        const removedElement = this.items.pop();
        return removedElement;
    }
    isEmpty(){
        return this.items.length===0;
    }
    getSize(){
        return this.items.length;
    }
}
// Test code
const stack = new Stack();
stack.push(50);
stack.push(30);
stack.push(20);
stack.push(60);
stack.push(70);
console.log('Top Element = '+stack.peek());
const x=stack.pop();
console.log("Removed Element = "+x);