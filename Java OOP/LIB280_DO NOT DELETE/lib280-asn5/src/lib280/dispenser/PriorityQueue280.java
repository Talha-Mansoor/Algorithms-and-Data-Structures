package lib280.dispenser;

import lib280.exception.ContainerEmpty280Exception;
import lib280.exception.ContainerFull280Exception;
import lib280.tree.ArrayedBinaryTree280;
import lib280.tree.ArrayedBinaryTreeIterator280;
import lib280.tree.IterableArrayedHeap280;

public class PriorityQueue280<I extends Comparable<? super I>> {

	// This is the heap that we are restricting.
	// Items in the priority queue get stored in the heap.
	protected IterableArrayedHeap280<I> items;
	ArrayedBinaryTreeIterator280<I> iterator;

	public PriorityQueue280(int cap) {
		items = new IterableArrayedHeap280<I>(cap);
		 iterator = items.iterator();
	}

	/**
	 * Returns a string representation of the priority queue.
	 * @return a string representation of the priority queue.
	 */
	public String toString() {
		return items.toString();
	}

	/**
	 * Insert an item into the priority queue.
	 * @param x The item to be inserted.
	 * @throws ContainerFull280Exception if the priority queue is full and there is no space to add an item.
	 */
	public void insert(I x){
		items.insert(x);
	}
	/**
	 * Determines if the priority queue is full.
	 * @return True if the priority queue is full, false otherwise.
	 */

	public boolean isFull(){
		return items.isFull();
	}


	/**
	 * Determines if the priority queue is empty.
	 * @return True if the priority queue is empty, false otherwise.
	 */
	public boolean isEmpty(){
		return items.isEmpty();
	}

	/**
	 * Returns the number of items currently in the priority queue.
	 * @return The number of items in the priority queue.
	 */
	public int count(){
		return items.count();
	}
	/**
	 * Returns the maximum item of the priority queue.
	 * @return The maximum item of the priority queue.
	 * @throws ContainerEmpty280Exception if the priority queue is empty.
	 */
	public I maxItem(){
		if(isEmpty()){
			throw new ContainerEmpty280Exception();
		}
		ArrayedBinaryTreeIterator280<I> x=items.iterator();
		x.goFirst();
		I y=items.item();
		return y;
	}
	/**
	 * Returns the minimum item of the priority queue.
	 * @return The minimum item of the priority queue.
	 * @throws ContainerEmpty280Exception if the priority queue is empty.
	 */
	public I minItem() {
		iterator.goFirst();
		//empty case and single element case
		if(isEmpty()){
			throw new ContainerEmpty280Exception();
		} else if (this.count()==1) {

			return iterator.item();
		}else{//Real min item in normal heap

			I x=iterator.item(); //original value stored here in x
			while(iterator.itemExists()){
				if(x.compareTo(iterator.item())>0){
					x=iterator.item(); //if xis greater than iterator item then make x the small one at the end we will be left with smallest one
				}iterator.goForth();
			}
			return x;
		}}


	/**

	 This method deletes the maximum item in the binary search tree.
	 */
	public void deleteMax() {
		items.deleteItem();
	}

	/**

	 This method deletes the minimum item in the binary search tree.

	 @throws ContainerEmpty280Exception if the tree is empty
	 */

	public void deleteMin(){
		if(isEmpty()){
			throw new ContainerEmpty280Exception();
		}
		ArrayedBinaryTreeIterator280<I> internal_iterator = items.iterator();
		internal_iterator.goFirst();
		I x=minItem();
		while(internal_iterator.itemExists() && (0 > (x.compareTo(internal_iterator.item()))) || 0<(x.compareTo(internal_iterator.item()))){

			internal_iterator.goForth();

		}
		items.deleteAtPosition(internal_iterator);


	}

	/**

	 This method deletes all the maximum items in the binary search tree.

	 @throws ContainerEmpty280Exception if the tree is empty
	 */
	public void deleteAllMax(){

		//Empty case
		if(isEmpty()){
			throw new ContainerEmpty280Exception();
		}
		//go to first
		//x is maximum item.
		// we will keep deleting them until we stop finding nodes equal to the max. It will reheapify automatically.
		iterator.goFirst();
		I x=maxItem();
		while (!(isEmpty()) && 0==x.compareTo(iterator.item())){
			deleteMax();
		}

	}

	public static void main(String args[]) {
		class PriorityItem<I> implements Comparable<PriorityItem<I>> {
			I item;
			Double priority;
			public PriorityItem(I item, Double priority) {
				super();
				this.item = item;
				this.priority = priority;
			}

			public int compareTo(PriorityItem<I> o) {
				return this.priority.compareTo(o.priority);
			}
			
			public String toString() {
				return this.item + ":" + this.priority;
			}
		}
		
		PriorityQueue280<PriorityItem<String>> Q = new PriorityQueue280<PriorityItem<String>>(5);
		
		// Test isEmpty()
		if( !Q.isEmpty()) 
			System.out.println("Error: Queue is empty, but isEmpty() says it isn't.");
		
		// Test insert() and maxItem()
		Q.insert(new PriorityItem<String>("Sing", 5.0));
		if( Q.maxItem().item.compareTo("Sing") != 0) {
			System.out.println("??Error: Front of queue should be 'Sing' but it's not. It is: " + Q.maxItem().item);
		}
		
		// Test isEmpty() when queue not empty
		if( Q.isEmpty()) 
			System.out.println("Error: Queue is not empty, but isEmpty() says it is.");
		
		// test count()
		if( Q.count() != 1 ) {
			System.out.println("Error: Count should be 1 but it's not.");			
		}

		// test minItem() with one element
		if( Q.minItem().item.compareTo("Sing")!=0) {
			System.out.println("Error: min priority item should be 'Sing' but it's not.");
		}	
		
		// insert more items
		Q.insert(new PriorityItem<String>("Fly", 5.0));
		if( Q.maxItem().item.compareTo("Sing")!=0) System.out.println("Front of queue should be 'Sing' but it's not.");
		Q.insert(new PriorityItem<String>("Dance", 3.0));
		if( Q.maxItem().item.compareTo("Sing")!=0) System.out.println("Front of queue should be 'Sing' but it's not.");
		Q.insert(new PriorityItem<String>("Jump", 7.0));
		if( Q.maxItem().item.compareTo("Jump")!=0) System.out.println("Front of queue should be 'Jump' but it's not.");
		
		if(Q.minItem().item.compareTo("Dance") != 0) System.out.println("minItem() should be 'Dance' but it's not.");
		
		if( Q.count() != 4 ) {
			System.out.println("Error: Count should be 4 but it's not.");			
		}
		
		// Test isFull() when not full
		if( Q.isFull()) 
			System.out.println("Error: Queue is not full, but isFull() says it is.");
		
		Q.insert(new PriorityItem<String>("Eat", 10.0));
		if( Q.maxItem().item.compareTo("Eat")!=0) System.out.println("Front of queue should be 'Eat' but it's not.");

		if( !Q.isFull()) 
			System.out.println("Error: Queue is full, but isFull() says it isn't.");

		// Test insertion on full queue
		try {
			Q.insert(new PriorityItem<String>("Sleep", 15.0));
			System.out.println("Expected ContainerFull280Exception inserting to full queue but got none.");
		}
		catch(ContainerFull280Exception e) {
			// Expected exception
		}
		catch(Exception e) {
			System.out.println("Expected ContainerFull280Exception inserting to full queue but got a different exception.");
			e.printStackTrace();
		}
		
		// test deleteMin
		Q.deleteMin();
		if(Q.minItem().item.compareTo("Sing") != 0) System.out.println("Min item should be 'Sing', but it isn't.");
		
		Q.insert(new PriorityItem<String>("Dig", 1.0));
		if(Q.minItem().item.compareTo("Dig") != 0) System.out.println("minItem() should be 'Dig' but it's not.");

		// Test deleteMax
		Q.deleteMax();
		if( Q.maxItem().item.compareTo("Jump")!=0) System.out.println("Front of queue should be 'Jump' but it's not.");

		Q.deleteMax();
		if( Q.maxItem().item.compareTo("Fly")!=0) System.out.println("Front of queue should be 'Fly' but it's not.");

		if(Q.minItem().item.compareTo("Dig") != 0) System.out.println("minItem() should be 'Dig' but it's not.");

		Q.deleteMin();
		if( Q.maxItem().item.compareTo("Fly")!=0) System.out.println("Front of queue should be 'Fly' but it's not.");

		Q.insert(new PriorityItem<String>("Scream", 2.0));
		Q.insert(new PriorityItem<String>("Run", 2.0));

		if( Q.maxItem().item.compareTo("Fly")!=0) System.out.println("Front of queue should be 'Fly' but it's not.");
		
		// test deleteAllMax()
		Q.deleteAllMax();
		if( Q.maxItem().item.compareTo("Scream")!=0) System.out.println("Front of queue should be 'Scream' but it's not.");
		if( Q.minItem().item.compareTo("Scream") != 0) System.out.println("minItem() should be 'Scream' but it's not.");
		Q.deleteAllMax();

		// Queue should now be empty again.
		if( !Q.isEmpty()) 
			System.out.println("Error: Queue is empty, but isEmpty() says it isn't.");

		System.out.println("Regression test complete.");
	}



}
