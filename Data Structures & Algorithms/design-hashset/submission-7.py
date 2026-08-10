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

    def add(self, val):
        self.root = self.insert(self.root, val)

    def remove(self, val):
        self.root = self.delete(self.root, val)

    def contains(self, target):
        return self.search(self.root, target)


    def insert(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)

        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root


    def delete(self, root, val):
        if not root:
            return None

        if val < root.val:
            root.left = self.delete(root.left, val)

        elif val > root.val:
            root.right = self.delete(root.right, val)

        else:
            # no left child
            if not root.left:
                return root.right

            # no right child
            if not root.right:
                return root.left

            # two children
            temp = self.minValueNode(root.right)

            root.val = temp.val

            root.right = self.delete(root.right, temp.val)

        return root


    def minValueNode(self, root):
        current = root

        while current.left:
            current = current.left

        return current


    def search(self, root, target):
        if not root:
            return False

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