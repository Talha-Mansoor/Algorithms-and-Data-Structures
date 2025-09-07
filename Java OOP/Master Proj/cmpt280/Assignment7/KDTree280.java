//Talha Mansoor
//kgy284
//11346490
//CMPT280


package lib280.tree;
import lib280.base.NDPoint280;
import lib280.exception.DuplicateItems280Exception;
import lib280.list.LinkedList280;
/**

 This class implements a k-d tree data structure to store and search for points in k-dimensional space.
 */
public class KDTree280{
    private int dimensions;
    private KDNode280 rutNode;
    /**

     Constructs a k-d tree from an array of k-dimensional points.
     @param pointArray An array of k-dimensional points to build the k-d tree from.
     */
    public KDTree280(KDNode280[]pointArray) {
        if (0==pointArray.length ) {return;}
        rutNode=(buildKDTree(pointArray, 0, pointArray.length - 1, 0));
    }

    /**

     Recursive method that builds a k-d tree from an array of k-dimensional points.

     @param pointArray An array of k-dimensional points to build the k-d tree from.

     @param left The left index of the subarray of points to build the k-d tree from.

     @param right The right index of the subarray of points to build the k-d tree from.

     @param depth The current depth of the k-d tree.

     @return The root node of the constructed k-d tree.
     */
    private KDNode280 buildKDTree(KDNode280[] pointArray, int left, int right, int depth) {
        this.dimensions = pointArray[0].item().dim();// dimensions is set to the dimensionality of the first point's data.
// If left is greater than right, there are no more points to add and null is returned.

        if (left > right) {
            return null;
        }
// depth is the depth of the current node in the tree, modulo the number of dimensions.
        int d = depth % dimensions;
        int mid = (left + right) / 2;
// mid is the index of the median element of the array slice.
// jSmallest is a helper function that sorts the array slice and finds the median element.
        jSmallest(pointArray, left, right, mid, d);

        KDNode280 newNode = new KDNode280(this.dimensions);
        newNode.setItem(pointArray[mid].item());
// The left and right subtrees of the new node are constructed recursively from the left and right halves of the array slice, respectively.
        newNode.setLeftNode(buildKDTree(pointArray, left, mid - 1, depth + 1));
        newNode.setRightNode(buildKDTree(pointArray, mid + 1, right, depth + 1));

        return newNode;// The newly constructed node is returned
    }


    /**

     Helper method that finds the jth smallest element in an array of points based on a specific dimension.

     @param kdList An array of points to find the jth smallest element from.

     @param left The left index of the subarray to search in.

     @param right The right index of the subarray to search in.

     @param j The index of the element to find.

     @param depth The current depth of the k-d tree.
     */
    private void jSmallest(KDNode280[] kdList, int left, int right, int j, int depth) {
        int d = depth % dimensions;

        while (right > left) {
            int pivot = partition(d, right, left, kdList);

            if (j > pivot) {
                left = pivot + 1;
            } else if (j < pivot) {
                right = pivot - 1;
            } else {
                break;
            }}}

    /**

     Helper method that partitions an array of points based on a specific dimension.
     @param t The dimension to partition the points by.
     @param r The right index of the subarray to partition.
     @param l The left index of the subarray to partition.
     @param kdList An array of points to partition.
     @return The index of the pivot element after partitioning.
     */
    private int partition(int t, int r, int l, KDNode280[] kdList) {
        // This code implements the partitioning step of the algorithm to sort a KD-tree based on its k-th dimension values.
        // It uses the last element of the list as a pivot, and swaps elements in the list such that all elements less than or
        // equal to the pivot come before it, and all elements greater than it come after it. If a duplicate element is found, a DuplicateItems280Exception is thrown.
        int swapOffset = l;
        KDNode280 pivot = kdList[r];
        int i = l;
        while (i < r) {
            if (kdList[i].item().compareTo(pivot.item()) == 0) {
                throw new DuplicateItems280Exception();
            }
            if (pivot.item().compareByDim(t, kdList[i].item()) >= 0) {
                KDNode280 holder = kdList[i];
                kdList[i] = kdList[swapOffset];
                kdList[swapOffset] = holder;
                swapOffset++;
            }
            i++;
        }
        KDNode280 holder = kdList[r];
        kdList[r] = kdList[swapOffset];
        kdList[swapOffset] = holder;
        return swapOffset;
    }


    /**

     Searches for nodes within a given range bounded by two KDNodes.

     The result is returned as a string containing all the found nodes.

     @param lower_bound the lower bound of the search range.

     @param upper_bound the upper bound of the search range.

     @return a string containing all the found nodes within the given range.
     */
    public String searcher(KDNode280 lower_bound, KDNode280 upper_bound) {
        LinkedList280<KDNode280> lList = new LinkedList280<>();
        searchHelper(lList, this.rutNode, 0, lower_bound, upper_bound);

        StringBuilder sbuilt = new StringBuilder();
        for (lList.goFirst(); lList.itemExists(); lList.goForth()) {
            sbuilt.append(lList.item()).append("\n");
        }
        return sbuilt.toString();
    }


    //private void search(KDNode280 root, K)
    /**

     Recursively searches for nodes within the given range bounded by two KDNodes.

     The search result is stored in a linked list.

     @param list the linked list used to store the search result.

     @param root the current node being searched.

     @param theDeep the current depth of the search in the KD Tree.

     @param lower_bound the lower bound of the search range.

     @param upper_bound the upper bound of the search range.
     */
    private void searchHelper(LinkedList280<KDNode280> list,KDNode280 root, int theDeep,KDNode280 lower_bound, KDNode280 upper_bound) {
        if (root == null) { //null case
            return;
        }
        int currDepth = theDeep % dimensions;// currDepth is the depth of the current node in the tree, modulo the number of dimensions.
        Double half_val = root.item().idx(currDepth);// half_val is the value of the current node along the k-th dimension.


        // If half_val is greater than or equal to the lower bound of the range, the left subtree is searched recursively.
        if ( (half_val) >= (lower_bound.item().idx(currDepth)) ) {
            searchHelper(list, root.leftNode(),theDeep + 1,lower_bound, upper_bound);

        }// If half_val is less than or equal to the upper bound of the range, the right subtree is searched recursively.
        if ((half_val) <= (upper_bound.item().idx(currDepth))) {
            searchHelper(list, root.rightNode(), theDeep + 1, lower_bound, upper_bound );
        }

        boolean inInterval = true;
        for (int i = 0; i < dimensions && inInterval; i++) {
            double loCoord = lower_bound.item().idx(i);
            double hiCoord = upper_bound.item().idx(i);
            double nodeCoord = root.item().idx(i);
            if (loCoord > nodeCoord || hiCoord < nodeCoord) {
                inInterval = false;
            }}
        if (inInterval) {
            list.insert(root);
        }}


    /**

     Returns a string representation of the KDTree starting from the root node.
     @return a string representation of the KDTree starting from the root node
     */
    @Override
    public String toString() {
        return toStringbyLvl(1,rutNode);
    }


    /**

     Returns a string representation of the KDTree starting from the specified node

     and indented based on the level of the node in the tree.

     @param rootn the root node of the subtree

     @return a string representation of the KDTree starting from the specified node
     */
    protected static String toStringbyLvl(int y,KDNode280 rootn) {
        StringBuffer tab_effect = new StringBuffer((y - 1) * 5);
        String visual = " ";

        for (int i = 0; i < y - 1; i++){
            tab_effect.append("          ");}
        if (null!=rootn){
            if(null!= rootn.rightNode()){
                visual += toStringbyLvl( y+1,rootn.rightNode());
            }}
        visual += "\n\n"+tab_effect+"=>"+y+":-  " ;


        if (rootn == null){
            visual += "EMPTY";
        }else {
            visual += rootn.toString();
            if (null !=rootn.leftNode()){
                visual += toStringbyLvl( y+1,rootn.leftNode());
        }}
        return visual;
    }


    public static void main(String[] args) {


        // Print separators and headers
        System.out.println("============================================================");
        System.out.println("+++++Testing KDTree Creation with 2D Points+++++");
        System.out.println("============================================================");

// Initialize 2D points and KD nodes
        KDNode280[] KD2dPoints = new KDNode280[12];
        Double[][] doublePairs = {{5.1, 2.1}, {9.1, 10.1}, {11.1, 1.1},{4.1, 3.1},
                {2.1, 12.1}, {3.1, 7.1}, {1.1, 5.1}, {42.1, 11.1},{6.1, 3.4},{7.1, 52.2} ,{2.2, 1.3} ,{8.2, 22.1} };
// Create KD nodes for 2D points
        for (int idx = 0; idx < KD2dPoints.length; idx++) {
            KD2dPoints[idx] = new KDNode280(doublePairs[idx]);
        }
// Print 2D input points
        System.out.println("========================");
        System.out.println("=== Input 2D Points ===");
        System.out.println("========================");
        for (int idx = 0; idx < 12; idx++) {
            System.out.println(idx + 1 + "-> " + KD2dPoints[idx]);
        }
// Build and print KD tree
        System.out.println("====================================================");
        System.out.println("=== The 2D KDTree Built from These Points is ===");
        System.out.println("====================================================");

        KDTree280 kdTree1 = new KDTree280(KD2dPoints);
        System.out.println(kdTree1);
        System.out.println("============================================================");

// Sample 2 KDTree with 2D points
        System.out.println("============================================================");
        System.out.println("+++++ Sample 2 KDTree using 2 dimensional points +++++");
        System.out.println("============================================================");

        KDNode280[] KD2dPoints2 = new KDNode280[7];
        Double[][] doublePairs2 = {{5.1, 2.1}, {9.1, 10.1}, {11.1, 1.1},{4.1, 3.1},
                {2.1, 12.1}, {3.1, 7.1}, {1.1, 5.1}};
// Create KD nodes for 2D points
        for (int idx = 0; idx < KD2dPoints2.length; idx++) {
            KD2dPoints2[idx] = new KDNode280(doublePairs2[idx]);
        }
// Print 2D input points
        System.out.println("========================");
        System.out.println("=== Input 2D Points ===");
        System.out.println("========================");
        for (int idx = 0; idx < 7; idx++) {
            System.out.println(idx + 1 + "-> " + KD2dPoints2[idx]);
        }
// Build and print KD tree
        System.out.println("====================================================");
        System.out.println("=== The 2D KDTree Built from These Points is ===");
        System.out.println("====================================================");

        KDTree280 kdTree2 = new KDTree280(KD2dPoints2);
        System.out.println(kdTree2);
        System.out.println("############# NEW TREE #############");

// Testing Creation of KDTree using 3D points
        System.out.println("============================================================");
        System.out.println("+++++ Testing Creation of KDTree using 3D Points +++++");
        System.out.println("============================================================");
        KDNode280[] KD3dPoints = new KDNode280[8];
        Double[][]triplePairs = {{1.1, 12.1, 1.1}, {18.1, 1.1, 2.1}, {2.1, 12.1, 16.1}, {7.1, 3.1, 3.1}, {3.1, 7.1, 5.1},
                {16.1, 4.1, 4.1}, {4.1, 6.1, 1.1}, {5.1, 5.1, 17.1}};
// Create KD nodes for 3D points
        for (int idx = 0; idx < KD3dPoints.length; idx++) {
            KD3dPoints[idx] = new KDNode280(triplePairs[idx]);
        }

// Print 3D input points
        System.out.println("========================");
        System.out.println("=== Input 3D Points ===");
        System.out.println("========================");
        for (int idx = 0; idx < 8; idx++) {
            System.out.println(idx + 1 + "-> " + KD3dPoints[idx]);
        }
// Build and print KD tree
        System.out.println("====================================================");
        System.out.println("=== The 3D KDTree Built from These Points is ===");
        System.out.println("====================================================");

        KDTree280 kdTree3D = new KDTree280(KD3dPoints);
        System.out.println(kdTree3D);

// Search for points within a range
        System.out.println("");
        System.out.println("*** Looking for points between (0.1, 1.1, 0.1) and (4.1, 6.1, 3.1) ***");
        System.out.println("");
        Double[] lowerBound = {0.1, 1.1, 0.1};
        Double[] upperBound = {4.1, 6.1, 3.1};
        KDNode280 lowerNode = new KDNode280(lowerBound);
        KDNode280 upperNode = new KDNode280(upperBound);
        System.out.println(kdTree3D.searcher(lowerNode, upperNode));

        System.out.println("");
        System.out.println("*** Looking for points between (0.1, 1.1, 0.1) and (8.1, 7.1, 4.1). ***");
        System.out.println("");
        Double[] upperBound2 = {8.1, 7.1, 4.1};
        KDNode280 newUpper2 = new KDNode280(upperBound2);
        System.out.println(kdTree3D.searcher(lowerNode, newUpper2));

        System.out.println("");
        System.out.println("*** Looking for points between (0.1, 1.1, 0.1) and (17.1, 9.1, 10.1). ***");
        System.out.println("");
        Double[] upperBound3 = {17.1, 9.1, 10.1};
        KDNode280 newUpper3 = new KDNode280(upperBound3);
        System.out.println(kdTree3D.searcher(lowerNode, newUpper3));

// Second KDTree using 3D points
        System.out.println("############# NEW TREE #############");
        System.out.println("");
        System.out.println("+++++ Testing Creation of 2nd KDTree using 3D Points +++++");
        System.out.println("");
        KDNode280[] KD3dPoints2 = new KDNode280[8];
        Double[][] triplePairs2 = {{1.1, 12.1, 0.1}, {18.1, 1.1, 2.1}, {2.1, 13.1, 16.1}, {7.1, 3.1, 3.1}, {3.1, 7.1, 5.1},
                {16.1, 4.1, 4.1}, {4.1, 6.1, 1.1}, {5.1, 5.1, 17.1}};
// Create KD nodes for 3D points
        for (int idx = 0; idx < KD3dPoints2.length; idx++) {
            KD3dPoints2[idx] = new KDNode280(triplePairs2[idx]);
        }

// Print 3D input points
        System.out.println("================================================");
        System.out.println("+++++ Input 3D Points +++++");
        System.out.println("================================================");
        for (int idx = 0; idx < 8; idx++) {
            System.out.println(idx + 1 + "-> " + KD3dPoints2[idx]);
        }
// Build and print KD tree
        System.out.println("====================================================");
        System.out.println("+++++ The 3D KDTree Built from These Points is +++++");
        System.out.println("====================================================");

        KDTree280 kdTree3D2 = new KDTree280(KD3dPoints2);
        System.out.println(kdTree3D2);

// Search for points within a range
        System.out.println("");
        System.out.println("*** Looking for points between (0.1, 1.1, 0.1) and (4.1, 6.1, 3.1) ***");
        System.out.println("");
        System.out.println(kdTree3D2.searcher(lowerNode, upperNode));

        System.out.println("");
        System.out.println("*** Looking for points between (0.1, 1.1, 0.1) and (8.1, 7.1, 4.1). ***");
        System.out.println("");
        System.out.println(kdTree3D2.searcher(lowerNode, newUpper2));

        System.out.println("");
        System.out.println("*** Looking for points between (0.1, 1.1, 0.1) and (17.1, 9.1, 10.1). ***");
        System.out.println("");
        System.out.println(kdTree3D2.searcher(lowerNode, newUpper3));
   }

}