def loop_size(node):
    explored_nodes = []
    current_node = node

    while current_node not in explored_nodes:
        explored_nodes.append(current_node)
        current_node = current_node.next

    idx = explored_nodes.index(current_node)

    return len(explored_nodes) - idx
