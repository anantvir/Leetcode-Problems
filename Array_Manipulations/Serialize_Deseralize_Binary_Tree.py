
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :return type: str
        """
        def Serialize_Helper(root,string):
            if root == None:
                string += 'None,'
            else:
                string += root.val
                string = Serialize_Helper(root.left,string)
                string = Serialize_Helper(root.right,string)
            return string
        return Serialize_Helper(root,'')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        string_to_list = data.split(',')
        def Deserialize_Helper(string_to_list):
            if string_to_list[0] == 'None':
                string_to_list.pop(0)
                return None

            node = TreeNode(string_to_list[0])
            string_to_list.pop(0)
            node.left = Deserialize_Helper(string_to_list)
            node.right = Deserialize_Helper(string_to_list)
            return node
        return Deserialize_Helper(string_to_list)
        

codec = Codec()
codec.deserialize(codec.serialize(root))