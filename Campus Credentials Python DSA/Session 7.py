# =====================================================================
# SESSION 7: TREES & GRAPHS (DATA STRUCTURES & ALGORITHMS)
# =====================================================================
# Topics Covered:
# ---------------------------------------------------------------------
# PART 1: BINARY TREES
#   1. Concepts, Terminology & Tree Types
#   2. Binary Tree Node Representation
#   3. Tree Traversals:
#      - Depth-First: Inorder, Preorder, Postorder (Recursive & Iterative)
#      - Breadth-First: Level Order Traversal (BFS)
#   4. Classic Tree Operations & Interview Problems:
#      - Height / Maximum Depth
#      - Total Node Count & Leaf Node Count
#      - Sum, Minimum & Maximum Values
#      - Search an Element
#      - Invert / Mirror a Binary Tree (LeetCode 226)
#      - Check Identical Trees (LeetCode 100)
#      - Symmetric / Mirror Image Tree (LeetCode 101)
#
# PART 2: BINARY SEARCH TREES (BST)
#   1. Properties of BST
#   2. BST Implementation:
#      - Insertion (Recursive & Iterative)
#      - Search (Recursive & Iterative)
#      - Finding Minimum & Maximum
#      - Deletion (3 cases: 0 child, 1 child, 2 children)
#   3. Validate BST (LeetCode 98)
#   4. Lowest Common Ancestor (LCA) in BST (LeetCode 235)
#   5. Inorder Predecessor & Successor
#
# PART 3: GRAPHS
#   1. Graph Terminology & Classifications
#   2. Graph Representations:
#      - Adjacency Matrix
#      - Adjacency List
#   3. Graph Implementation (Adjacency List Class)
#   4. Graph Traversals:
#      - Breadth-First Search (BFS)
#      - Depth-First Search (DFS - Recursive & Iterative)
#      - Handling Disconnected Components
#   5. Essential Graph Problems & Algorithms:
#      - Shortest Path in Unweighted Graph (BFS)
#      - Detect Cycle in Undirected Graph (DFS / BFS)
#      - Detect Cycle in Directed Graph (DFS with RecStack)
#      - Topological Sort (Kahn's Algorithm / In-degree BFS)
#      - Dijkstra's Algorithm (Single Source Shortest Path using Priority Queue)
# =====================================================================

from collections import deque
import heapq


# =====================================================================
# PART 1: BINARY TREES
# =====================================================================
"""
WHAT IS A TREE?
- A Tree is a non-linear, hierarchical data structure consisting of nodes
  connected by edges.
- Unlike arrays, stacks, and queues (which are linear), trees organize data
  hierarchically (like a family tree or file system directory).

TREE TERMINOLOGY:
1. Root: The topmost node of the tree (has no parent).
2. Edge: The link/connection between two nodes.
3. Parent: A node that has an outgoing edge to a child node.
4. Child: A node that has an incoming edge from a parent node.
5. Leaf (External Node): A node with no children (left = None, right = None).
6. Internal Node: A node with at least one child.
7. Siblings: Nodes that share the same parent.
8. Ancestor / Descendant:
   - Ancestors of node X: nodes on the path from root to X.
   - Descendants of node X: all nodes reachable downwards from X.
9. Degree:
   - Degree of a node: Number of children the node has.
   - Degree of a tree: Maximum degree among all nodes.
10. Level: The root is at level 0 (or 1 depending on convention). Children of root are at level 1.
11. Height of a Node: Number of edges on the longest downward path to a leaf.
    - Height of a leaf node = 0.
    - Height of empty tree = -1 (or 0 in some conventions).
12. Depth of a Node: Number of edges from the root to that node.
    - Depth of root = 0.

TYPES OF BINARY TREES:
1. Full / Strict Binary Tree: Every node has either 0 or 2 children.
2. Complete Binary Tree: All levels are completely filled except possibly
   the last, which is filled from left to right (used in Heaps).
3. Perfect Binary Tree: All internal nodes have 2 children, and all leaves
   are at the same level. (Total nodes = 2^(h+1) - 1).
4. Balanced Binary Tree: For every node, |height(left) - height(right)| <= 1 (e.g., AVL tree).
5. Degenerate / Skewed Tree: Every internal node has only one child.
   Effectively behaves like a linked list (Height = N, O(N) operations).
"""

# ---------------------------------------------------------------------
# 1.1 Binary Tree Node Class
# ---------------------------------------------------------------------
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.data})"


# ---------------------------------------------------------------------
# 1.2 Tree Traversals (DFS: Inorder, Preorder, Postorder)
# ---------------------------------------------------------------------
# Inorder:   Left -> Root -> Right  (For BST, this yields SORTED order!)
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)

# Preorder:  Root -> Left -> Right  (Used to clone/serialize a tree)
def preorder_traversal(root):
    if root is None:
        return []
    return [root.data] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Postorder: Left -> Right -> Root  (Used to delete tree, bottom-up calculations)
def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.data]


# Iterative Inorder using explicit Stack (Crucial for interviews!)
def inorder_iterative(root):
    result = []
    stack = []
    curr = root
    while curr is not None or len(stack) > 0:
        # Reach the leftmost node of current node
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        # Current must be None at this point
        curr = stack.pop()
        result.append(curr.data)
        # We have visited the node and its left subtree; now right subtree
        curr = curr.right
    return result

# Iterative Preorder using Stack
def preorder_iterative(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.data)
        # Push right first so that left is popped and processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

# ---------------------------------------------------------------------
# 1.3 Level Order Traversal (BFS) using Queue
# ---------------------------------------------------------------------
def level_order_traversal(root):
    """
    Traverses the tree level by level, left to right.
    Uses a Queue (FIFO). Time: O(N), Space: O(W) where W is max width of tree.
    """
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result


# ---------------------------------------------------------------------
# 1.4 Classic Binary Tree Problems & Operations
# ---------------------------------------------------------------------

# Problem 1: Maximum Depth / Height of Binary Tree (LeetCode 104)
def max_depth(root):
    if root is None:
        return 0
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    return 1 + max(left_height, right_height)

# Problem 2: Count Total Nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Problem 3: Count Leaf Nodes
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Problem 4: Sum of all nodes
def sum_of_nodes(root):
    if root is None:
        return 0
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)

# Problem 5: Find Maximum Value in Binary Tree
def find_max(root):
    if root is None:
        return float('-inf')
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(root.data, left_max, right_max)

# Problem 6: Search a value in Binary Tree
def search_tree(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    return search_tree(root.left, key) or search_tree(root.right, key)

# Problem 7: Invert / Mirror a Binary Tree (LeetCode 226)
def invert_tree(root):
    if root is None:
        return None
    # Swap left and right subtrees
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

# Problem 8: Check if Two Binary Trees are Identical (LeetCode 100)
def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return (p.data == q.data and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))

# Problem 9: Check if Tree is Symmetric / Mirror of itself (LeetCode 101)
def is_symmetric(root):
    if root is None:
        return True
    def is_mirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.data == t2.data and 
                is_mirror(t1.left, t2.right) and 
                is_mirror(t1.right, t2.left))
    return is_mirror(root.left, root.right)


# --- Binary Tree Demo ---
print("=" * 60)
print("DEMO: PART 1 - BINARY TREE")
print("=" * 60)
# Constructing Sample Binary Tree:
#         10
#        /  \
#       20   30
#      /  \    \
#     40  50    60
tree_root = TreeNode(10)
tree_root.left = TreeNode(20)
tree_root.right = TreeNode(30)
tree_root.left.left = TreeNode(40)
tree_root.left.right = TreeNode(50)
tree_root.right.right = TreeNode(60)

print("Inorder (Recursive):", inorder_traversal(tree_root))
print("Inorder (Iterative):", inorder_iterative(tree_root))
print("Preorder (Recursive):", preorder_traversal(tree_root))
print("Preorder (Iterative):", preorder_iterative(tree_root))
print("Postorder:", postorder_traversal(tree_root))
print("Level Order:", level_order_traversal(tree_root))
print("Height / Max Depth:", max_depth(tree_root))
print("Total Nodes:", count_nodes(tree_root))
print("Leaf Nodes:", count_leaf_nodes(tree_root))
print("Sum of Nodes:", sum_of_nodes(tree_root))
print("Maximum Value:", find_max(tree_root))
print("Search 50:", search_tree(tree_root, 50))
print("Search 99:", search_tree(tree_root, 99))
print()


# =====================================================================
# PART 2: BINARY SEARCH TREES (BST)
# =====================================================================
"""
WHAT IS A BINARY SEARCH TREE (BST)?
A Binary Search Tree is a binary tree with the following ordering property:
1. The left subtree of a node contains only nodes with keys LESS than the node's key.
2. The right subtree of a node contains only nodes with keys GREATER than the node's key.
3. Both left and right subtrees must also be binary search trees.
4. No duplicate nodes (standard convention, or duplicates counted in frequency).

IMPORTANT PROPERTY:
- The INORDER traversal of any BST always produces nodes in ASCENDING SORTED ORDER!

COMPLEXITIES:
- Search:   Average = O(log N), Worst (Skewed tree) = O(N)
- Insert:   Average = O(log N), Worst = O(N)
- Delete:   Average = O(log N), Worst = O(N)
- Space:    O(H) recursion stack where H is tree height.
"""

class BST:
    def __init__(self):
        self.root = None

    # -----------------------------------------------------------------
    # 2.1 Insertion in BST
    # -----------------------------------------------------------------
    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        # Base case: if tree/subtree is empty, return new node
        if root is None:
            return TreeNode(key)
        if key < root.data:
            root.left = self._insert_rec(root.left, key)
        elif key > root.data:
            root.right = self._insert_rec(root.right, key)
        # If key == root.data, duplicates are typically ignored
        return root

    def insert_iterative(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return
        curr = self.root
        parent = None
        while curr:
            parent = curr
            if key < curr.data:
                curr = curr.left
            elif key > curr.data:
                curr = curr.right
            else:
                return  # Duplicate value, ignore
        if key < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    # -----------------------------------------------------------------
    # 2.2 Search in BST
    # -----------------------------------------------------------------
    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)

    def search_iterative(self, key):
        curr = self.root
        while curr:
            if curr.data == key:
                return curr
            elif key < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return None

    # -----------------------------------------------------------------
    # 2.3 Minimum & Maximum in BST
    # -----------------------------------------------------------------
    # The minimum element is always the leftmost node
    def find_min(self, node=None):
        curr = node if node else self.root
        if curr is None:
            return None
        while curr.left is not None:
            curr = curr.left
        return curr.data

    # The maximum element is always the rightmost node
    def find_max(self, node=None):
        curr = node if node else self.root
        if curr is None:
            return None
        while curr.right is not None:
            curr = curr.right
        return curr.data

    # -----------------------------------------------------------------
    # 2.4 Deletion in BST (Crucial Interview Topic!)
    # -----------------------------------------------------------------
    """
    Three cases when deleting node X:
    Case 1: Node X is a Leaf node (0 children) -> simply remove it (return None).
    Case 2: Node X has 1 child -> replace X with its child.
    Case 3: Node X has 2 children:
            - Find Inorder Successor (smallest node in right subtree)
              OR Inorder Predecessor (largest node in left subtree).
            - Copy that successor's value to node X.
            - Recursively delete the successor from the right subtree.
    """
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, root, key):
        if root is None:
            return root

        # Step 1: Navigate to the node to be deleted
        if key < root.data:
            root.left = self._delete_rec(root.left, key)
        elif key > root.data:
            root.right = self._delete_rec(root.right, key)
        else:
            # Step 2: Node found! Handle the 3 cases:

            # Case 1 & 2: No child or 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node has two children
            # Find inorder successor (minimum value in right subtree)
            successor_val = self._min_value_node(root.right).data
            root.data = successor_val
            # Delete the inorder successor from right subtree
            root.right = self._delete_rec(root.right, successor_val)

        return root

    def _min_value_node(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    # -----------------------------------------------------------------
    # 2.5 Inorder Traversal Helper (Returns sorted list)
    # -----------------------------------------------------------------
    def inorder(self):
        return inorder_traversal(self.root)


# ---------------------------------------------------------------------
# 2.6 Validate Binary Search Tree (LeetCode 98)
# ---------------------------------------------------------------------
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Every node in left subtree must be < root.data
    Every node in right subtree must be > root.data
    """
    if root is None:
        return True
    if not (min_val < root.data < max_val):
        return False
    return (is_valid_bst(root.left, min_val, root.data) and
            is_valid_bst(root.right, root.data, max_val))


# ---------------------------------------------------------------------
# 2.7 Lowest Common Ancestor (LCA) in BST (LeetCode 235)
# ---------------------------------------------------------------------
def lca_bst(root, p_val, q_val):
    """
    Lowest Common Ancestor in BST:
    - If both p and q are smaller than root, LCA is in left subtree.
    - If both p and q are greater than root, LCA is in right subtree.
    - If one is on the left and one on the right (or one equals root),
      root is the split point, hence the LCA!
    """
    curr = root
    while curr:
        if p_val < curr.data and q_val < curr.data:
            curr = curr.left
        elif p_val > curr.data and q_val > curr.data:
            curr = curr.right
        else:
            return curr
    return None


# --- BST Demo ---
print("=" * 60)
print("DEMO: PART 2 - BINARY SEARCH TREE (BST)")
print("=" * 60)
bst = BST()
elements = [50, 30, 70, 20, 40, 60, 80]
for el in elements:
    bst.insert(el)

print("BST Inorder (Should be strictly sorted):", bst.inorder())
print("Min in BST:", bst.find_min())
print("Max in BST:", bst.find_max())
print("Search 40:", bst.search(40) is not None)
print("Search 90:", bst.search(90) is not None)
print("Is Valid BST?:", is_valid_bst(bst.root))

lca = lca_bst(bst.root, 20, 40)
print("LCA of 20 and 40:", lca.data if lca else None)
lca2 = lca_bst(bst.root, 20, 80)
print("LCA of 20 and 80:", lca2.data if lca2 else None)

# Deletion testing
print("\nDeleting Leaf Node (20):")
bst.delete(20)
print("Inorder after deleting 20:", bst.inorder())

print("Deleting Node with 1 Child (30):")
bst.delete(30)
print("Inorder after deleting 30:", bst.inorder())

print("Deleting Root Node with 2 Children (50):")
bst.delete(50)
print("Inorder after deleting 50:", bst.inorder())
print()


# =====================================================================
# PART 3: GRAPHS
# =====================================================================
"""
WHAT IS A GRAPH?
A Graph is a non-linear data structure consisting of a finite set of
VERTICES (Nodes, denoted by V) and EDGES (connections between nodes, denoted by E).
G = (V, E)

GRAPH CLASSIFICATIONS:
1. Directed Graph (Digraph): Edges have directions (u -> v != v -> u).
   - E.g., Twitter followers, web page links.
2. Undirected Graph: Edges are bidirectional (u -- v means u <-> v).
   - E.g., Facebook friendship.
3. Weighted Graph: Edges have associated values/costs/weights (distances, travel times).
4. Unweighted Graph: All edges have equal cost (usually considered 1).
5. Cyclic Graph: Contains at least one cycle (path that starts and ends at the same vertex).
6. Acyclic Graph: Contains no cycles.
   - Directed Acyclic Graph (DAG): Crucial in task scheduling, compilers, Git commits.
7. Connected Graph: Path exists between every pair of vertices.
8. Degree of a Vertex:
   - In Undirected Graph: Number of edges incident on the vertex.
   - In Directed Graph:
     - In-degree: Number of incoming edges.
     - Out-degree: Number of outgoing edges.

GRAPH REPRESENTATIONS:
1. Adjacency Matrix:
   - 2D array of size V x V.
   - matrix[i][j] = 1 (or weight) if an edge exists from i to j, else 0.
   - Space Complexity: O(V^2) -> Good for Dense Graphs (many edges).
   - Checking if edge (u, v) exists: O(1).
   - Finding all neighbors of u: O(V).

2. Adjacency List:
   - Array or Dictionary where each vertex maps to a list/set of its neighbors.
   - Space Complexity: O(V + E) for directed, O(V + 2E) for undirected.
   - Preferred for Sparse Graphs (most real-world graphs!).
   - Finding all neighbors of u: O(degree(u)).
"""

# ---------------------------------------------------------------------
# 3.1 Graph Representation (Adjacency List Class)
# ---------------------------------------------------------------------
class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        if weight is None:
            self.adj[u].append(v)
            if not self.directed:
                self.adj[v].append(u)
        else:
            self.adj[u].append((v, weight))
            if not self.directed:
                self.adj[v].append((u, weight))

    def display(self):
        for vertex, neighbors in self.adj.items():
            print(f"  {vertex} -> {neighbors}")

    # -----------------------------------------------------------------
    # 3.2 Breadth-First Search (BFS)
    # -----------------------------------------------------------------
    """
    BFS explores neighbors level-by-level using a QUEUE (FIFO).
    Time Complexity:  O(V + E)
    Space Complexity: O(V) for visited set & queue.
    Key application: Shortest path in unweighted graphs!
    """
    def bfs(self, start_node):
        if start_node not in self.adj:
            return []
        
        visited = set([start_node])
        queue = deque([start_node])
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)
            for neighbor in self.adj[node]:
                # If graph has weights, neighbor is a tuple (v, weight)
                nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        return traversal

    # BFS that handles disconnected components
    def bfs_all_components(self):
        visited = set()
        full_traversal = []
        for vertex in self.adj:
            if vertex not in visited:
                queue = deque([vertex])
                visited.add(vertex)
                component = []
                while queue:
                    curr = queue.popleft()
                    component.append(curr)
                    for neighbor in self.adj[curr]:
                        nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append(nbr)
                full_traversal.append(component)
        return full_traversal

    # -----------------------------------------------------------------
    # 3.3 Depth-First Search (DFS)
    # -----------------------------------------------------------------
    """
    DFS explores as deep as possible along each branch before backtracking.
    Implemented using Recursion (Call Stack) or explicit STACK (LIFO).
    Time Complexity:  O(V + E)
    Space Complexity: O(V) recursion stack / visited set.
    """
    def dfs_recursive(self, start_node):
        visited = set()
        traversal = []

        def _dfs(node):
            visited.add(node)
            traversal.append(node)
            for neighbor in self.adj.get(node, []):
                nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
                if nbr not in visited:
                    _dfs(nbr)

        if start_node in self.adj:
            _dfs(start_node)
        return traversal

    # Iterative DFS using explicit Stack
    def dfs_iterative(self, start_node):
        if start_node not in self.adj:
            return []
        visited = set()
        stack = [start_node]
        traversal = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                # Push neighbors in reverse order to visit them in natural order
                for neighbor in reversed(self.adj[node]):
                    nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
                    if nbr not in visited:
                        stack.append(nbr)
        return traversal


# ---------------------------------------------------------------------
# 3.4 Shortest Path in Unweighted Graph using BFS
# ---------------------------------------------------------------------
def shortest_path_unweighted(graph, start, target):
    """
    Finds the shortest path and minimum edge count between start and target.
    BFS guarantees the shortest path in an unweighted graph!
    """
    if start not in graph.adj or target not in graph.adj:
        return None, -1
    
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path, len(path) - 1

        for neighbor in graph.adj[node]:
            nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, path + [nbr]))

    return None, -1  # Target unreachable


# ---------------------------------------------------------------------
# 3.5 Cycle Detection in Undirected Graph (using DFS)
# ---------------------------------------------------------------------
def has_cycle_undirected(graph):
    """
    In an undirected graph, a cycle exists if we encounter a visited neighbor
    that is NOT the immediate parent of the current node.
    """
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.adj[node]:
            nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
            if nbr not in visited:
                if dfs(nbr, node):
                    return True
            elif nbr != parent:
                # Visited neighbor is NOT the parent -> Cycle detected!
                return True
        return False

    for vertex in graph.adj:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False


# ---------------------------------------------------------------------
# 3.6 Cycle Detection in Directed Graph (using DFS + Recursion Stack)
# ---------------------------------------------------------------------
def has_cycle_directed(graph):
    """
    In a directed graph, a cycle exists if there is a BACK-EDGE to an
    ancestor currently present in the recursion call stack (in_stack).
    """
    visited = set()
    in_stack = set()

    def dfs(node):
        visited.add(node)
        in_stack.add(node)

        for neighbor in graph.adj.get(node, []):
            nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
            if nbr not in visited:
                if dfs(nbr):
                    return True
            elif nbr in in_stack:
                return True  # Back-edge found! Cycle exists.

        in_stack.remove(node)  # Backtrack
        return False

    for vertex in graph.adj:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False


# ---------------------------------------------------------------------
# 3.7 Topological Sort (Kahn's Algorithm using In-Degrees / BFS)
# ---------------------------------------------------------------------
def topological_sort(graph):
    """
    Topological Sort applies ONLY to Directed Acyclic Graphs (DAGs).
    A linear ordering of vertices such that for every directed edge u -> v,
    vertex u comes before v in the ordering.
    Applications: Build systems (Makefiles), Course prerequisites, Task scheduling.

    Kahn's Algorithm (BFS-based):
    1. Calculate in-degree of all vertices.
    2. Enqueue all vertices with in-degree == 0.
    3. Pop vertex, add to result, decrease in-degree of its neighbors by 1.
    4. If neighbor's in-degree becomes 0, enqueue it.
    5. If result length != total vertices, the graph has a cycle!
    """
    in_degree = {v: 0 for v in graph.adj}
    for u in graph.adj:
        for neighbor in graph.adj[u]:
            nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
            in_degree[nbr] = in_degree.get(nbr, 0) + 1

    queue = deque([v for v, deg in in_degree.items() if deg == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph.adj.get(node, []):
            nbr = neighbor[0] if isinstance(neighbor, tuple) else neighbor
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)

    if len(topo_order) != len(graph.adj):
        return None  # Cycle detected; topological sort impossible!
    return topo_order


# ---------------------------------------------------------------------
# 3.8 Dijkstra's Algorithm (Single Source Shortest Path for Weighted Graphs)
# ---------------------------------------------------------------------
def dijkstra(graph, start):
    """
    Finds shortest distances from start vertex to all other vertices.
    Works for graphs with NON-NEGATIVE edge weights.
    Uses Min-Heap (heapq / Priority Queue) for efficiency.
    Time Complexity:  O((V + E) log V)
    Space Complexity: O(V)
    """
    distances = {v: float('inf') for v in graph.adj}
    distances[start] = 0
    # Min-Heap stores tuples of (distance_from_start, vertex)
    min_heap = [(0, start)]

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        # If current distance is already greater than recorded, skip
        if current_dist > distances[u]:
            continue

        for neighbor_tuple in graph.adj.get(u, []):
            v, weight = neighbor_tuple
            distance = current_dist + weight
            # If shorter path to v is found:
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))

    return distances


# --- Graph Demos ---
print("=" * 60)
print("DEMO: PART 3 - GRAPHS")
print("=" * 60)

# Undirected Graph Demo:
#      0 ----- 1
#      |       | \
#      |       |  2
#      |       | /
#      4 ----- 3
g_undirected = Graph(directed=False)
g_undirected.add_edge(0, 1)
g_undirected.add_edge(1, 2)
g_undirected.add_edge(2, 3)
g_undirected.add_edge(3, 4)
g_undirected.add_edge(4, 0)
g_undirected.add_edge(1, 3)

print("Undirected Graph Adjacency List:")
g_undirected.display()
print("BFS Traversal from 0:", g_undirected.bfs(0))
print("DFS Recursive from 0:", g_undirected.dfs_recursive(0))
print("DFS Iterative from 0:", g_undirected.dfs_iterative(0))

path, dist = shortest_path_unweighted(g_undirected, 0, 2)
print(f"Shortest path from 0 to 2 (BFS): {path} (Distance: {dist} edges)")

print("Has cycle in undirected graph?:", has_cycle_undirected(g_undirected))

# Directed Acyclic Graph (DAG) for Topological Sort:
#   5 -> 0 <- 4
#   |         |
#   v         v
#   2 -> 3 -> 1
dag = Graph(directed=True)
dag.add_edge(5, 2)
dag.add_edge(5, 0)
dag.add_edge(4, 0)
dag.add_edge(4, 1)
dag.add_edge(2, 3)
dag.add_edge(3, 1)

print("\nDAG Adjacency List:")
dag.display()
print("Has cycle in DAG?:", has_cycle_directed(dag))
print("Topological Sort Order:", topological_sort(dag))

# Directed Graph with Cycle:
#   1 -> 2 -> 3 -> 1
g_cycle = Graph(directed=True)
g_cycle.add_edge(1, 2)
g_cycle.add_edge(2, 3)
g_cycle.add_edge(3, 1)
print("\nDirected Graph with Cycle:")
print("Has cycle in directed graph?:", has_cycle_directed(g_cycle))
print("Topological Sort (Should be None):", topological_sort(g_cycle))

# Weighted Graph for Dijkstra's:
#         (4)
#     A -------> B
#     |        / |
#  (2)|    (1)/  | (5)
#     v   <--    v
#     C -------> D
#         (8)
g_weighted = Graph(directed=True)
g_weighted.add_edge('A', 'B', 4)
g_weighted.add_edge('A', 'C', 2)
g_weighted.add_edge('B', 'C', 1)
g_weighted.add_edge('B', 'D', 5)
g_weighted.add_edge('C', 'D', 8)

print("\nWeighted Graph Adjacency List:")
g_weighted.display()
shortest_distances = dijkstra(g_weighted, 'A')
print("Dijkstra Shortest Distances from 'A':", shortest_distances)
print("=" * 60)
