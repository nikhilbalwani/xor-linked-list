from xor_linked_list import Node

# Creating three different nodes
node1 = Node(data=1)
node2 = Node(data=2)
node3 = Node(data=3)

# Precede node1 by None and succeed by node2 
node1.set_neighbors(prev_node=None, next_node=node2)
# Precede node2 by node1 and succeed by node3
node2.set_neighbors(prev_node=node1, next_node=node3)
# Precede node3 by node2 and succeed by None
node3.set_neighbors(prev_node=node2, next_node=None)

curr_node = node1
prev_node = None

print('Traversing forwards:')

print(str(None), '<->', end=' ')

while curr_node != None:
    print(curr_node.data, '<->', end=' '),

    prev_node_temp = curr_node
    curr_node = curr_node.get_next(prev_node=prev_node, global_vars=globals())
    prev_node = prev_node_temp

print(str(None))

curr_node = node3
prev_node = None

print('Traversing backwards:')

print(str(None), '<->', end=' ')

while curr_node != None:
    print(curr_node.data, '<->', end=' '),

    prev_node_temp = curr_node
    curr_node = curr_node.get_next(prev_node=prev_node, global_vars=globals())
    prev_node = prev_node_temp

print(str(None))
