//Talha Mansoor
//kgy284
//11346490
//CMPT280
package lib280.tree;
import lib280.base.NDPoint280;
import lib280.exception.InvalidState280Exception;
public class KDNode280 extends BinaryNode280<NDPoint280> {
    //2 constructors
    /**
     * Constructor that creates a new KDNode280 with a given array of Double values.
     * The array is used to create a new NDPoint280 object, which is set as the item of this node.
     *
     * @param x An array of Double values used to create the NDPoint280 object stored in this node.
     */
    public KDNode280(Double[] x) {
        super(new NDPoint280(x));
    }
    /**
     * Constructor that creates a new KDNode280 with a given integer value.
     * The integer is used to create a new NDPoint280 object with a single dimension, which is set as the item of this node.
     *
     * @param x The integer value used to create the NDPoint280 object stored in this node.
     */
    public KDNode280(int x) {
        super(new NDPoint280(x));
    }
    /**
     * Returns the item stored in this node.
     *
     * @return The NDPoint280 object stored in this node.
     */
    @Override
    public NDPoint280 item() {
        return super.item();
    }
    /**
     * Checks whether this node is empty.
     * A node is considered empty if its item is null.
     *
     * @return True if this node is empty, false otherwise.
     */
    protected boolean isEmpty() {
        boolean b=(null==item);
        return  b;
    }

    /**
     * Returns the left child of this node.
     *
     * @return The left child of this node, cast to a KDNode280.
     */
    @Override
    public KDNode280 leftNode() {
        return (KDNode280) super.leftNode();
    }
    /**
     * Returns the right child of this node.
     *
     * @return The right child of this node, cast to a KDNode280.
     */
    @Override
    public KDNode280 rightNode() {
        return (KDNode280) super.rightNode();
    }
    /**
     * Returns a string representation of the item stored in this node.
     *
     * @return A string representation of the NDPoint280 object stored in this node.
     */
    @Override
    public String toString() {
        return item().toString();
    }
    /**
     * Sets the left child of this node to a given node.
     *
     * @param n The node to set as the left child of this node.
     */
    //@Override
    public void setLeftNode(KDNode280 n) {
        super.setLeftNode(n);
    }
    /**
     * Sets the right child of this node to a given node.
     *
     * @param n The node to set as the right child of this node.
     */
    //@Override
    public void setRightNode(KDNode280 n) {
        super.setRightNode(n);
    }

}