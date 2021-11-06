def find_parent(_node, _arr):
    if _arr[_node] != _node:
        _arr[_node] = find_parent(_arr[_node], _arr)
        return _arr[_node]
    return _node

def union(_node1, _node2, _arr):
    _root1 = find_parent(_node1, _arr)
    _root2 = find_parent(_node2, _arr)
    _arr[_root1] = _root2