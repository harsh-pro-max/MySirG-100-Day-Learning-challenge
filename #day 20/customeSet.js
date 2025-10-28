class CustomeSet{
    constructor(){
        this.items=new Map();
    }
    add(element){
        if(this.items.has(element)){
            return false;
        }
        this.items.set(element,element);
        return true;
    }
    has(element){
        return this.items.has(element);
    }
    remove(element){
        return this.items.delete(element);
    }
    size(){
        return this.items.size;
    }
    values(){
        return [...this.items.keys()];
    }
    union(othersSet){
        const unionSet=new CustomeSet();
        this.values().forEach(value=>unionSet.add(value));

        othersSet.values().forEach(value=> unionSet.add(value));
        return unionSet;
    }
    Intersection(otherSet){
        const intersectionSet = new CustomeSet();

        const smallerSet= this.size() < otherSet.size()?this:otherSet;
        const largerSet= this.size()<otherSet.size()?otherSet:this;

        smallerSet.values().forEach(value =>{
            if(largerSet.has(value)){
                intersectionSet.add(value);
            }
        });
        return intersectionSet;
    }
}
const setA = new CustomeSet();
setA.add(2);
setA.add(4);
setA.add(6);
setA.add(8);
setA.add(10);

const setB= new CustomeSet();
setB.add(1);
setB.add(4);
setB.add(7);
setB.add(8);

console.log(setA);
console.log(setB);
setC=setA.union(setB);
console.log(setC);
setD= setA.Intersection(setB);
console.log(setD);