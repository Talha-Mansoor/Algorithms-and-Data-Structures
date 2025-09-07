//Talha Mansoor
//kgy284
//11346490
//Noah Orensa
//CMPT 280


import lib280.base.Cursor280;
import lib280.base.Dispenser280;
import lib280.base.Searchable280;
import lib280.exception.ContainerEmpty280Exception;
import lib280.exception.ContainerFull280Exception;
import lib280.exception.DuplicateItems280Exception;
import lib280.exception.NoCurrentItem280Exception;
import lib280.tree.BinaryNode280;
import lib280.tree.LinkedSimpleTree280;

public class AVLTree280<I extends Comparable<I>>extends LinkedSimpleTree280<I>implements Dispenser280<I>, Searchable280<I>, Cursor280<I> {
    /**
     * THIS DOES NOT WORK. ITS JUST A SKELETON. DIDNT HAVE ENOUGH TIME TO WORK ON IT.
     *
     An implementation of an AVL Tree that extends the LinkedSimpleTree280 class and implements the Dispenser280,

     Searchable280, and Cursor280 interfaces.

     @param <I> The type of item that the AVL Tree will store. I must extend the Comparable interface.
     */
    protected BinaryNode280<I> currentNode; // The current node of the cursor.
    protected BinaryNode280<I> parentNode;// The parent of the current node.
    protected boolean boolCompare;// A boolean indicating if comparisons should be made based on object
    protected boolean look=false; // A boolean indicating if we want to search or not

    /**

     Constructor for an AVL Tree object. Sets the root node of the AVL Tree to null, and initializes
     boolCompare and look to false.
     */
    public AVLTree280() {
        this.setRootNode(null);
        this.boolCompare =false;
        this.look = false;
    }

    @Override
    public I item() throws NoCurrentItem280Exception {
        return null;
    }
    /**

     Returns a boolean indicating if the cursor has a current item.
     @return A boolean indicating if the cursor has a current item.
     */

    @Override
    public boolean itemExists() {
        return false;
    }

    /**
     Returns a boolean indicating if the AVL Tree is empty.
     @return A boolean indicating if the AVL Tree is empty.
     */
    @Override
    public boolean isEmpty() {
        return super.isEmpty();
    }
    /**

     Returns a boolean indicating if the AVL Tree is full.
     @return A boolean indicating if the AVL Tree is full.
     */
    @Override
    public boolean isFull() {
        return super.isFull();
    }
    /**

     Creates a new AVL node with the given item.
     @param item The item to create a new AVL node with.
     @return A new AVL node with the given item.
     */
    public AVLnode<I> newN(I item) {
        return new AVLnode<I>(item);
    }

    /**

     Returns a boolean indicating if the AVL Tree contains the given item.
     @param y The item to search for in the AVL Tree.
     @return A boolean indicating if the AVL Tree contains the given item.
     */
    @Override
    public boolean has(I y) {
        BinaryNode280<I> tempcurrent=currentNode;
        BinaryNode280<I> temppar=parentNode;
        search(y);
        Boolean check=itemExists();
        currentNode=tempcurrent;
        parentNode=temppar;
        return check;
    }


    /**
     * Checks if the membership of two items x and y in the AVL Tree is equal.
     *
     * @param x The first item.
     * @param y The second item.
     * @return True if the membership of x and y is equal, false otherwise.
     */
    @Override
    public boolean membershipEquals(I x, I y) {
        if (true==boolCompare){
            return x==y;
        } else if (y.equals(x)) {
            return true;
        } else if ((y instanceof Comparable<I>) && (x instanceof Comparable<I>) ) {
            //equals case 2
            return 0==x.compareTo(y);
        }else{
        return false;
    }}
    /**
     * Checks if the current node is above the root node in the AVL Tree.
     * @return True if the current node is above the root node, false otherwise.
     */
    public boolean before(){
        //is position above root
        boolean b = ((currentNode == null) && (parentNode == null));
        return b;}
    /**
     * Checks if the current node is below the leaf nodes in the AVL Tree.
     * @return True if the current node is below the leaf nodes, false otherwise.
     */
    public boolean after(){
        //is position below beneath tree?
        boolean b = (isEmpty() || null != parentNode) && (currentNode == null);
        return b;}

    /**

     This method searches for a specific item in tree

     @param x the item to search for
     */
    @Override
    public void search(I x) {
        boolean check=false; // a flag to indicate if the item is found or not
        if ((!after())){     // check if the iterator is not positioned after the last element
            currentNode=rootNode;     // set the current node to the root node and set the parent node to null
            parentNode=null;
        } else if ((before()) || (!look)) {    // if the iterator is positioned before the first element or the look flag is false
            parentNode=currentNode;             // set the parent node to the current node and move the current node to the right child
            currentNode=currentNode.rightNode();   //
        }
        while (itemExists() && !check){         // loop while there is an item and the item has not been found yet
            if (0 < (x.compareTo(item()))){// if the item to search for is greater than the current item
                parentNode=currentNode;        // set the parent node to the current node
                currentNode=parentNode.rightNode(); // move the current node to the right child
            } else if (0>(x.compareTo(item()))) {// if the item to search for is less than the current item
                parentNode=currentNode;//
                currentNode=parentNode.leftNode();
            }else{check=true;//if the item found then set the flag to indicate that the item is found
            }}}
    /**

     Overrides the restartSearches() method from Tree280 to set look to false.
     This method can be used to indicate that any search that was in progress should be stopped.
     */

    @Override
    public void restartSearches() {
        look=false;
    }
    /**

     Overrides the resumeSearches() method from Tree280 to set look to true.
     This method can be used to indicate that searches can be resumed after a call to restartSearches().
     */
    @Override
    public void resumeSearches() {
        look=true;
    }
    /**

     Overrides the rootLeftSubtree() method from Tree280 to cast the returned subtree to an AVLTree280.
     This method returns the left subtree of the root node as an AVLTree280.
     @throws ContainerEmpty280Exception if the AVLTree280 is empty.
     @return the left subtree of the root node as an AVLTree280.
     */
    @Override
    public AVLTree280<I> rootLeftSubtree() throws ContainerEmpty280Exception {
        return ((AVLTree280<I>) super.rootLeftSubtree());
    }
    /**

     Overrides the rootRightSubtree() method from Tree280 to cast the returned subtree to an AVLTree280.
     This method returns the right subtree of the root node as an AVLTree280.
     @throws ContainerEmpty280Exception if the AVLTree280 is empty.
     @return the right subtree of the root node as an AVLTree280.
     */
    @Override
    public AVLTree280<I> rootRightSubtree() throws ContainerEmpty280Exception {
        return ((AVLTree280<I>) super.rootRightSubtree());
    }
    /**

     Inserts a new item into the AVL tree.
     @param x the item to be inserted into the tree
     @throws ContainerFull280Exception if the AVL tree is full
     @throws DuplicateItems280Exception if an item with the same value as x already exists in the AVL tree
     */
    @Override
    public void insert(I x) throws ContainerFull280Exception, DuplicateItems280Exception {
        this.insert_internal(x, null);
    }

    /**

     Insert an item into the AVL Tree.
     @param x - The item to insert.
     @throws ContainerFull280Exception - If the AVL Tree is full.
     @throws DuplicateItems280Exception - If the item already exists in the AVL Tree.
     */
    protected void insert_internal(I x, AVLnode<I> parentNode) throws ContainerFull280Exception, DuplicateItems280Exception {
        //empty case
        if(this.isEmpty()){
            this.setRootNode(this.newN(x));
            return;
        }
        //check whether to ge left or right
        AVLnode<I> g=this.rootNode();
        if (0<item().compareTo(g.item())){ // check if item() is greater than g.item()
            //going right
            if (g.rightNode()==null){ // if right child of g is null
                g.setRightNode(new AVLnode<I>(x));// set x as the right child of g

            }else{
                this.rootRightSubtree().insert(x); // othrwise insert x into the right subtree of g
            }
            g.setRightH(Math.max(g.rightNode().getRightH(),g.rightNode().getRightH())+1);  // update the height of the right child of g
        }
        else{
            //SIMILARLY
        //going left
            if(null==g.leftNode()){
                g.setLeftNode(new AVLnode<I>(x));
            }else{
                this.rootLeftSubtree().insert_internal(x,this.rootNode());
            }
            g.setLeftH(Math.max(g.leftNode().getLeftH(),g.leftNode().getRightH())+1);

        this.reAVLify((AVLnode<I>) this.parentNode);
    }}

    /**

     Returns the root node of this AVL tree.
     @return the root node of this AVL tree.
     */
    public AVLnode<I> rootNode() {
        BinaryNode280<I> x=super.rootNode();
        return (AVLnode<I>) x;
    }

    /**

     Performs a left rotation on the current AVLTree280 object around the root node, with the given parent node of the current tree.
     This method updates the parent node's child node to point to the new tree, updates the heights of relevant nodes, and performs a left rotation.
     @param parentNode the parent node of the current tree, which is being updated with the new rotated subtree
     @throws NullPointerException if the current AVLTree280 object is not empty, but either the left or right subtree is empty
     */
    protected void leftR(AVLnode<I> parentNode)  {
        AVLTree280<I> tree = this;
        AVLTree280<I> tright = this.rootRightSubtree();
        AVLTree280<I> tleft = tright.rootLeftSubtree();

        // Set new parent node for tree
        if (parentNode != null) {
            if (this.rootNode() == parentNode.leftNode()) {
                parentNode.setLeftNode(tright.rootNode());
            } else {
                parentNode.setRightNode(tright.rootNode());
            }
        }
        // Update right height of tree root node
        if (tleft.isEmpty()) {
            tree.rootNode().setRightH(0);
        } else {
            tree.rootNode().setRightH(Math.max(tleft.rootNode().getLeftH(), tleft.rootNode().getRightH()) + 1);
        }

        // Update left height of tright root node
        if (tree.isEmpty()) {
            tright.rootNode().setLeftH(0);
        } else {
            tright.rootNode().setLeftH(Math.max(tree.rootNode().getLeftH(), tree.rootNode().getRightH()) + 1);
        }

        // Perform left rotation
        tree.rootNode().setRightNode(tleft.rootNode());
        tright.rootNode().setLeftNode(tree.rootNode());
        this.setRootNode(tright.rootNode());
    }

    /**

     Performs a right rotation on the AVL tree rooted at this node.
     <p>Rotates the tree to the right, such that the left child of the current root becomes the new root,
     and the current root becomes the right child of the new root. The right subtree of the new root becomes
     the left subtree of the old root.
     <p>If a parent node is provided, updates the appropriate child node of the parent to point to the new tree.
     <p>Updates the heights of relevant nodes in the tree after rotation.
     @param parentNode the parent node of the AVL tree rooted at this node, if applicable


     */

    public void rightR(AVLnode<I> parentNode) {
        AVLTree280<I> tree = this;
        AVLTree280<I> tleft = this.rootLeftSubtree();
        AVLTree280<I> tright = tleft.rootRightSubtree();

        // If a parent node is given, update the appropriate child node to point to the new tree
        if (parentNode != null) {
            //? means if else
            AVLnode<I> nodeToUpdate = (this.rootNode == parentNode.leftNode()) ? parentNode.leftNode() : parentNode.rightNode();
            nodeToUpdate.setLeftNode(tright.rootNode());
        }

        // Update heights of relevant nodes
        int newLeftHeight = (tright.isEmpty()) ? 0 : Math.max(tright.rootNode().getLeftH(), tright.rootNode().getRightH()) + 1;
        int newRightHeight = (tree.isEmpty()) ? 0 : Math.max(tleft.rootNode().getLeftH(), tleft.rootNode().getRightH()) + 1;
        tleft.rootNode().setRightH(newRightHeight);
        tree.rootNode().setLeftH(newLeftHeight);

        // Perform right rotation
        AVLnode<I> oldLeftNode = tree.rootNode().leftNode();
        tree.rootNode().setLeftNode(tright.rootNode().rightNode());
        tright.rootNode().setRightNode(tree.rootNode());
        tleft.rootNode().setRightNode(tright.rootNode().rightNode());
        tright.rootNode().setLeftNode(tleft.rootNode());
        tright.setRootNode(tree.rootNode());
        tree.setRootNode(oldLeftNode);
    }

    /**
     * Performs a double left rotation on the current tree, using the given parent node.
     * First performs a right rotation on the right subtree, then a left rotation on the current tree.
     *
     * @param parentNode the parent node of the current tree, used to update the appropriate child node after rotation
     */
    protected void left2xr(AVLnode<I> parentNode){
        this.rootRightSubtree().rightR(this.rootNode());
        this.leftR(parentNode);
    }


    /**
     * Performs a double right rotation on the current tree, using the given parent node.
     * First performs a left rotation on the left subtree, then a right rotation on the current tree.
     *
     * @param parentNode the parent node of the current tree, used to update the appropriate child node after rotation
     */
    protected void right2xr(AVLnode<I> parentNode){
        this.rootLeftSubtree().leftR(this.rootNode());
        this.rightR(parentNode);
    }

    /**
     * Calculates the imbalance factor of the given AVL node, defined as the difference between the heights of its left and right subtrees.
     * A positive value indicates that the left subtree is taller, while a negative value indicates that the right subtree is taller.
     *
     * @param x the AVL node to calculate the imbalance factor of
     * @return the imbalance factor of the given AVL node
     */
    protected int imbalance_checker(AVLnode<I> x){
        return x.getLeftH()-x.getRightH();
    }
    /**

     Should Rebalance the AVL tree by performing single or double rotations at the node where an imbalance was detected.
     @param parent the parent node of the subtree being rebalanced
     */
    protected void reAVLify(AVLnode<I> parent) {
        int balanceFactor = this.imbalance_checker(this.rootNode());

        // Check if the tree is balanced
        if (imbalance_checker((AVLnode<I>) this.rootNode)== 1 || imbalance_checker((AVLnode<I>) this.rootNode)== 0 || imbalance_checker((AVLnode<I>) this.rootNode)= -1) {
            return;}

        // If right-heavy
        if (balanceFactor == 2) {
            AVLnode<I> leftNode = this.rootNode().leftNode();
            int leftNodeBalanceFactor = this.imbalance_checker(leftNode);

            // Single rotation
            if (leftNodeBalanceFactor >= 0) {
                this.rightR((AVLnode<I>) parentNode);
            }
            // Double rotation
            else {
                this.right2xr((AVLnode<I>) parentNode);}
        }
        // If left-heavy
        else {
            AVLnode<I> rightNode = this.rootNode().rightNode();
            int rightNodeBalanceFactor = this.imbalance_checker(rightNode);

            // Single rotation
            if (rightNodeBalanceFactor <= 0) {
                this.leftR((AVLnode<I>) parentNode);
            }
            // Double rotation
            else {
                this.left2xr((AVLnode<I>) parentNode);
            }}}


    /**

     should be able to Delete the current item from the tree. but it doesnt

     @throws NoCurrentItem280Exception if there is no current item.
     */
    public void delete() throws NoCurrentItem280Exception {
        //user calls delet and this method calls deletehelper method. It finds and gives current item to be deleted.
        I to_be_deleted = currentNode.item();
        this.deleteHelper(to_be_deleted, null, this);
    }

    /**
   Internal use delete function :|
     */
    protected void deleteHelper(I toBeDeleted, AVLnode<I> parent, AVLTree280<I> mistree) {
            }

    /**
     * Form a string representation that includes level numbers.
     * Analysis: Time = O(n), where n = number of items in the (sub)lib280.tree
     *
     */
    @Override
    public String toString() {
        return "AVLTree280{" +
                "currentNode=" + currentNode +
                ", boolCompare=" + boolCompare +
                ", parentNode=" + parentNode +
                ", look=" + look +
                '}';
    }


    public static void main(String[] args) {
        AVLTree280<Integer> tree = new AVLTree280<Integer>();
        //NO TESTING OR CONSOLE TEXT FILE :(

    }
}
