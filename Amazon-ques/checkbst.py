from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def is_bst_util(node, min_allowed, max_allowed):

    if node is None:
        return True
    if not (min_allowed < node.data < max_allowed):
        return False
    return (is_bst_util(node.left, min_allowed, node.data) and 
            is_bst_util(node.right, node.data, max_allowed))

def is_bst(root):

    return 1 if is_bst_util(root, float('-inf'), float('inf')) else 0

def build_tree_from_input():

    user_string = input("Enter node values in level-order (use 'N' for null, e.g., '2 1 3'): ")
    tokens = user_string.strip().split()
    
    if not tokens or tokens[0] == 'N':
        return None
        
    root = Node(int(tokens[0]))
    queue = deque([root])
    i = 1
    
    while queue and i < len(tokens):
        current_node = queue.popleft()
        

        if i < len(tokens):
            if tokens[i] != 'N':
                current_node.left = Node(int(tokens[i]))
                queue.append(current_node.left)
            i += 1
            

        if i < len(tokens):
            if tokens[i] != 'N':
                current_node.right = Node(int(tokens[i]))
                queue.append(current_node.right)
            i += 1
            
    return root

if __name__ == "__main__":
    print("--- Binary Search Tree (BST) Validator ---")
    print("Instructions: Enter values separated by spaces. Use 'N' for empty branches.")
    print("Example 1 Tree (2 with children 1 and 3)  -> Enter: 2 1 3")
    print("Example 2 Tree (Skewed tree from prompt)  -> Enter: 2 N 7 N 6 N 5 N 9 N 2 N 6\n")
    

    tree_root = build_tree_from_input()
    
    output_result = is_bst(tree_root)
    print(f"Output: {output_result}")
