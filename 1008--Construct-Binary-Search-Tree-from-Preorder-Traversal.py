class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []


        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result
