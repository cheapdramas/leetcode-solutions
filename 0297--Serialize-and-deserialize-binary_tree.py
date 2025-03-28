# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = '|'
    NULL = 'N'

    def serialize_preorder(self,root:TreeNode) -> list[str]:
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node == None:
                res.append(self.NULL)
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return res
    

    

    def serialize(self, root) -> str:
        """
            Encode:
                TreeNode -> str
        """
        return self.SEP.join(self.serialize_preorder(root))
        
        
    def deserialize_preorder(self,nodes: list[str]) -> TreeNode:
        val = nodes.pop()
        if val == self.NULL:
            return None
        node = TreeNode(int(val))
        node.left = self.deserialize_preorder(nodes)
        node.right = self.deserialize_preorder(nodes)
        return node




    def deserialize(self, data: str) -> TreeNode:
        """
            Decode:
                str -> TreeNode
        """
        nodes = data.split(self.SEP)
        nodes.reverse()
        return self.deserialize_preorder(nodes)
        
        
        

            





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



