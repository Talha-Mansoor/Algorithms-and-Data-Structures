import lib280.base.Cursor280;
import lib280.base.CursorPosition280;
import lib280.base.Dispenser280;
import lib280.exception.ContainerFull280Exception;
import lib280.exception.DuplicateItems280Exception;
import lib280.exception.NoCurrentItem280Exception;
import lib280.tree.ArrayedBinaryTree280;
import lib280.tree.ArrayedBinaryTreePosition280;
//Talha Mansoor
//kgy284
//11346490
//Noah Orensa
//CMPT 280

public class ArrayedHeap280<I extends Comparable<I>> extends ArrayedBinaryTree280<I> implements Dispenser280<I>{
   // private Comparable [] items;
    public ArrayedHeap280(int cap) {
        super(cap);

        items = (I[]) new Comparable[cap+1];

    }

    @Override
    public void insert(I e) throws ContainerFull280Exception, DuplicateItems280Exception {
        if( this.isFull() ) throw new ContainerFull280Exception("Cannot add item to a tree that is full.");
        else {
            currentNode=1;     //points to the root node, always points to the root node.
            count ++;          //count refers to number of items in the array, we are adding a new item, so it goes up.
            items[count] = e;    //placing the node of interest into the last position on the heap.

            //int top=count;

            int eindex=count;     //get index integer value of the last item on the heap.

            while((eindex>1) &&  (0<items[eindex].compareTo(items[findParent(eindex)]))) {       //run loop if node of interest is not at root AND less than parent  NO ISSUE
                int parenti = findParent(eindex);                                                //integer variable to represent the index of the parent of node of interest

                I tempParent = items[findParent(eindex)];          // storing the parent to be replaced in a temporary variable.

                items[findParent(eindex)] = items[eindex];        //storing the node of interest in the parent index location.
                items[eindex] = tempParent;                    //storing the parent, in the old location of the node of interest
                eindex = parenti;                     //eindex represents the index of node of interest, since we changed locations, need to up it
            }}}
//        //Insert e into H normally , as in ArrayedBinaryTreeWithCursors280 <I >
//        // ( put it in the left - most open position at the bottom level of the tree )
//        //while e is larger than its parent and is not at the root :
//        //swap e with its parent


    @Override
    public void deleteItem(){

        int k=1;                            //index root
        items[k]=items[count];              //swap root with smallest child
        items[count]=null;
        count--;
        int l=findLeftChild(k);             //left child index
        if(count==0) {
            count = 0;
            currentNode = 0;
        }
        //System.out.println(items[1]);
        while(l<count){                     //while left is less than count than right may exist

            int max=l;                      //max child is left by default
            int r=findRightChild(k);        //get right child index
            //System.out.println(items[r]);
            //System.out.println(items[r].compareTo(items[l]));
            if(r<count()){                  //if right child is less than count then check if its bigger than left
                if(0<items[r].compareTo(items[l])){
                    max++;                  //if right is bigger than its index is put in max
                }}

            //System.out.println(items[k].compareTo(items[max]));

        if(0>items[k].compareTo(items[max])){    //if item at k (parent) is smaller than biggest child then
            I temp=items[max];                   //temporary child copy
            items[max]=items[k];                //child=parent
            items[k]=temp;                      //parent=child temp copy
            k=max;                              //index of k is now that of child
            l=findLeftChild(k);                 //l is now the child of new k
        }else{

            break;
        }}}

//                       Removes the largest element from the heap H .
//                    // Since the largest element in a heap is always at the root ...
//                    Remove the root from H normally , as in ArrayedBinaryTreeWithCursors280 <I >
//                // ( copy the right - most element in the bottom level , e, into the root ,
//                    // remove the original copy of e.)
//                    while e is smaller than its largest child
//                    swap e with its largest chil

    /**
         * Helper for the regression test.  Verifies the heap property for all nodes.
         */
        private boolean hasHeapProperty() {
            for(int i=1; i <= count; i++) {
                if( findRightChild(i) <= count ) {  // if i Has two children...
                    // ... and i is smaller than either of them, , then the heap property is violated.
                    if( items[i].compareTo(items[findRightChild(i)]) < 0 ) return false;
                    if( items[i].compareTo(items[findLeftChild(i)]) < 0 ) return false;
                }
                else if( findLeftChild(i) <= count ) {  // if n has one child...
                    // ... and i is smaller than it, then the heap property is violated.
                    if( items[i].compareTo(items[findLeftChild(i)]) < 0 ) return false;
                }
                else break;  // Neither child exists.  So we're done.
            }
            return true;
        }

        /**
         * Regression test
         */
        public static void main(String[] args) {

            ArrayedHeap280<Integer> H = new ArrayedHeap280<Integer>(10);

            // Empty heap should have the heap property.
            if(!H.hasHeapProperty()) System.out.println("Does not have heap property.");

            // Insert items 1 through 10, checking after each insertion that
            // the heap property is retained, and that the top of the heap is correctly i.
            for(int i = 1; i <= 10; i++) {
                H.insert(i);
                if(H.item() != i) System.out.println("Expected current item to be " + i + ", got " + H.item());
                if(!H.hasHeapProperty()) System.out.println("Does not have heap property.");
               //System.out.println(H.toString());
            }


            // Remove the elements 10 through 1 from the heap, chekcing
            // after each deletion that the heap property is retained and that
            // the correct item is at the top of the heap.
            for(int i = 10; i >= 1; i--) {
                //System.out.println(H.toString());
                // Remove the element i.
                H.deleteItem();
                // If we've removed item 1, the heap should be empty.
                if(i==1) {
                    if( !H.isEmpty() ) System.out.println("Expected the heap to be empty, but it wasn't.");
                }
                else {
                    // Otherwise, the item left at the top of the heap should be equal to i-1.
                    if(H.item() != i-1) System.out.println("Expected current item to bee " + i + ", got " + H.item());
                    if(!H.hasHeapProperty()) System.out.println("Does not have heap property.");
                }
            }

            System.out.println("Regression Test Complete.");
        }
    }

