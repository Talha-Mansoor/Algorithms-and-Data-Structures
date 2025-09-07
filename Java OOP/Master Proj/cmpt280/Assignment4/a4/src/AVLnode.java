//Talha Mansoor
//kgy284
//11346490
//Noah Orensa
//CMPT 280


import lib280.tree.BinaryNode280;

public class AVLnode <I extends Comparable<? super I>> extends BinaryNode280<I> {
    /**
     * Left and right subtree heights
     */
    protected int rightH;
    protected int leftH;
    /**
     * Construct a new node with item x.
     *
     * @param x the item placed in the new node
     * @timing Time = O(1)
     */
    public AVLnode(I x) {
        super (x);
        rightH=0;
        leftH=0;
    }
    /**
     * Returns a string representation of the item contained within the node.
     * @timing Time = O(1)
     */
    @Override
    public String toString() {
        return "AVLnode{" +
                "rightH=" + rightH +
                ", leftH=" + leftH +
                '}';
    }
    /**
     * Gives us typecasted left node
     * @timing Time = O(1)
     */
    @Override
    public AVLnode<I> leftNode() {
        return (AVLnode<I>) super.leftNode();
    }
    /**
     * Gives us typecasted right node
     * @timing Time = O(1)
     */
    @Override
    public AVLnode<I> rightNode() {
        return  (AVLnode<I>) super.rightNode();
    }

    //we will make getters and setters for heights of left and right subtree

    /**
     * Gives us height of right subtree
     * @timing Time = O(1)
     */
    public int getRightH() {
        return rightH;
    }

    /**
     * Gives us height of left subtree
     * @timing Time = O(1)
     */
    public int getLeftH() {
        return leftH;
    }
    /**
     * set the height of right subtree
     * @timing Time = O(1)
     */
    public void setRightH(int rightH) {
        this.rightH = rightH;
    }
    /**
     * set the height of left subtree
     * @timing Time = O(1)
     */
    public void setLeftH(int leftH) {
        this.leftH = leftH;
    }



}
