package lib280.tree;
import lib280.exception.ContainerEmpty280Exception;
import lib280.exception.NoCurrentItem280Exception;
public class IterableArrayedHeap280<I extends Comparable<? super I>> extends ArrayedHeap280<I> {

	/**
	 * Create an iterable heap with a given capacity.
	 * @param cap The maximum number of elements that can be in the heap.
	 */
	public IterableArrayedHeap280(int cap) {
		super(cap);
	}

	// TODO
	// Add iterator() and deleteAtPosition() methods here.


	public void deleteAtPosition(ArrayedBinaryTreeIterator280<I> x){
		if(this.isEmpty())
			throw new ContainerEmpty280Exception("Cannot delete an item from an empty heap.");
		if( !(x.itemExists())){
			throw new NoCurrentItem280Exception();
		}



		// Delete the root by moving in the last item.
		// If there is more than one item, and we aren't deleting the last item,
		// copy the last item in the array to the current position.
		//if( this.count > 1 ) {
		//	this.currentNode = x;
		//	this.items[currentNode] = this.items[count];
		//}
		items[x.currentNode]=items[this.count];
		this.count--;

		// If we deleted the last remaining item, make the the current item invalid, and we're done.
		if( this.count == 0) {
			x.currentNode = 0;
			return;
		}

		// Propagate the new root down the lib280.tree.
		int n = x.currentNode;

		// While offset n has a left child...
		while( findLeftChild(n) <= count ) {
			// Select the left child.
			int child = findLeftChild(n);

			// If the right child exists and is larger, select it instead.
			if( child + 1 <= count && items[child].compareTo(items[child+1]) < 0 )
				child++;

			// If the parent is smaller than the root...
			if( items[n].compareTo(items[child]) < 0 ) {
				// Swap them.
				I temp = items[n];
				items[n] = items[child];
				items[child] = temp;
				n = child;
			}
			else return;

		}
	}
	public ArrayedBinaryTreeIterator280<I> iterator(){
		return new ArrayedBinaryTreeIterator280<> (this);
	}
}
