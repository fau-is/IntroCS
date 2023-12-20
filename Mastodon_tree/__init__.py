import check50
import check50.py
#from binary_search_tree import BST

@check50.check()
def exists():
    """binary_search_tree.py exists"""
    check50.exists("binary_search_tree.py")

def import_bst():
    bst_module = check50.py.import_("binary_search_tree.py")
    if bst_module is None:
        raise check50.Failure("import failed")
    return bst_module.BST

@check50.check(exists)
def initialization():
    """BST node correctly initialized"""
    bst_module = import_bst()
    try:
        bst = bst_module("Lopinel")
        if bst.username != "Lopinel":
            raise check50.Mismatch("Lopinel", bst.username)
        if bst.left is not None:
            raise check50.Mismatch("None", str(bst.left))
        if bst.right is not None:
            raise check50.Mismatch("None", str(bst.right))
        if bst_module.root is not None:
            raise check50.Mismatch("None", str(bst_module.root))
    except:
        raise check50.Failure("Initialization failed.")

@check50.check(initialization)
def add_root():
    """Root node added to BST"""
    bst_module = import_bst()
    try:
        bst_module.add("Lopinel")
        if bst_module.root.username != "Lopinel":
            raise check50.Mismatch("Lopinel", bst_module.root.username)
    except:
        raise check50.Failure("Adding root failed.")

@check50.check(add_root)
def add_nodes():
    """Multiple nodes added to BST correctly"""
    bst_module = import_bst()
    usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                 'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']
    try:
        bst_module.add("Lopinel")
        for username in usernames:
            bst_module.add(username)
        if bst_module.root.username != 'Lopinel':
            raise check50.Mismatch('Lopinel', bst_module.root.username)
        if bst_module.root.right.username != 'THD_IT':
            raise check50.Mismatch('THD_IT', bst_module.root.right.username)
        if bst_module.root.right.right.username != 'mistur':
            raise check50.Mismatch('mistur', bst_module.root.right.right.username)
        if bst_module.root.right.left is not None:
            raise check50.Mismatch("None", str(bst_module.root.right.left))
    except:
        raise check50.Failure("Adding nodes failed.")

@check50.check(add_nodes)
def tree_structure():
    """BST structure is correct"""
    bst_module = import_bst()
    try:
        def is_bst(node):
            if not node:
                return True
            if node.left and node.left.username >= node.username:
                return False
            if node.right and node.right.username <= node.username:
                return False
            return is_bst(node.left) and is_bst(node.right)

        if not is_bst(bst_module.root):
            raise check50.Failure("The BST structure is incorrect. Ensure left child < parent and right child > parent.")
    except:
        raise check50.Failure("Tree structure validation failed.")



@check50.check(tree_structure)
def iterative_search():
    """iterative search works correctly"""
    bst_module = import_bst()
    usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                 'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']
    try:
        bst_module.add("Lopinel")
        for username in usernames:
            bst_module.add(username)
        if bst_module.iterative_search(bst_module.root, 'Lopinel').username != 'Lopinel':
            raise check50.Mismatch('Lopinel', bst_module.iterative_search(bst_module.root, 'Lopinel').username)
        if bst_module.iterative_search(bst_module.root, 'mistur').username != 'mistur':
            raise check50.Mismatch('mistur', bst_module.iterative_search(bst_module.root, 'mistur').username)
        if bst_module.iterative_search(bst_module.root, 'NonExistingUser'):
            raise check50.Mismatch('False', 'True')
        bst_module.root = None
        if bst_module.iterative_search(bst_module.root, 'Lopinel'):
            raise check50.Mismatch('False', 'True')
    except:
        raise check50.Failure("iterative search failed.")

@check50.check(tree_structure)
def recursive_search():
    """Recursive search works correctly"""
    bst_module = import_bst()
    usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                 'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']
    try:
        bst_module.add("Lopinel")
        for username in usernames:
            bst_module.add(username)
        if bst_module.recursive_search(bst_module.root, 'Lopinel').username != 'Lopinel':
            raise check50.Mismatch('Lopinel', bst_module.recursive_search(bst_module.root, 'Lopinel').username)
        if bst_module.recursive_search(bst_module.root, 'mistur').username != 'mistur':
            raise check50.Mismatch('mistur', bst_module.recursive_search(bst_module.root, 'mistur').username)
        if bst_module.recursive_search(bst_module.root, 'NonExistingUser'):
            raise check50.Mismatch('False', 'True')
        bst_module.root = None
        if bst_module.recursive_search(bst_module.root, 'Lopinel'):
            raise check50.Mismatch('False', 'True')
    except:
        raise check50.Failure("Recursive search failed.")

@check50.check(recursive_search)
def preorder():
    """Preorder traversal returns expected order of usernames"""
    bst_module = import_bst()
    usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                 'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']
    bst_module.add("Lopinel")
    for username in usernames:
        bst_module.add(username)
    expected_preorder = ["Lopinel", "Harmonia_Amanda", "Dju", "Bram_Finkel", "BrunoBellamy", "GeoffreyDorne", "HyP",
                         "THD_IT", "mistur", "Zestryon"]
    try:
        result = bst_module.preorder()
        if result != expected_preorder:
            raise check50.Mismatch(expected_preorder, result)
    except:
        raise check50.Failure("Could not run Preorder traversal.")

@check50.check(preorder)
def inorder():
    """Inorder traversal returns expected order of usernames"""
    bst_module = import_bst()
    usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                 'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']
    bst_module.add("Lopinel")
    for username in usernames:
        bst_module.add(username)
    expected_inorder = ["Bram_Finkel", "BrunoBellamy", "Dju", "GeoffreyDorne", "Harmonia_Amanda", "HyP", "Lopinel",
                        "THD_IT", "Zestryon", "mistur"]
    try:
        result = bst_module.inorder()
        if result != expected_inorder:
            raise check50.Mismatch(expected_inorder, result)
    except:
        raise check50.Failure("Could not run Inorder traversal.")

@check50.check(inorder)
def postorder():
    """Postorder traversal returns expected order of usernames"""
    bst_module = import_bst()
    usernames = ['THD_IT', 'Harmonia_Amanda', 'Dju', 'GeoffreyDorne', 'Bram_Finkel',
                 'HyP', 'mistur', 'Zestryon', 'BrunoBellamy']
    bst_module.add("Lopinel")
    for username in usernames:
        bst_module.add(username)
    expected_postorder = ["BrunoBellamy", "Bram_Finkel", "GeoffreyDorne", "Dju",  "HyP", "Harmonia_Amanda",
                          "Zestryon", "mistur", "THD_IT", "Lopinel"]
    try:
        result = bst_module.postorder()
        if result != expected_postorder:
            raise check50.Mismatch(expected_postorder, result)
    except:
        raise check50.Failure("Could not run Postorder traversal.")

if __name__ == "__main__":
    check50.run()
