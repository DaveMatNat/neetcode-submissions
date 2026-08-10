# Similar Idea to LinkedList method. This solution uses BST instead for each bucket, so query, add, and remove is way better long term.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# implementing BST from scratch
class BST:
    def __init__(self):
        self.root = None

    def add(self,val):
        self.root = self.insert(self.root, val)

    def remove(self, val):
        self.root = self.delete(self.root, val)

    def contains(self, target):
        return self.search(self.root, target)

    #### USE FOR ADD #####
    def insert(self, root, val):
        # Found an empty spot
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root

    #### USE FOR REMOVE #### (Come back to understand this code again in full details)
    def delete(self, root, val):
        if not root:
            return None
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root
        

    #### USE FOR CONTAINS ####
    def search(self, root, target):
        # base case, val doesn't exist
        if not root:
            return False

        # recursive case
        if root.val == target:
            return True
        elif target > root.val:
            return self.search(root.right, target)
        else:
            return self.search(root.left, target)

class MyHashSet:
    # BST, instead of using LinkedList, since it improves adding, removing, and searching to log(n/k) in average case instead of O(n/k). 
    # worst case still O(n/k) tho
    def __init__(self):
        self.size = 10**4
        self.buckets = [BST() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        # if val doesn't exist in BST of a hash bucket
        if not self.contains(key):
            self.buckets[index].add(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return self.buckets[index].contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)