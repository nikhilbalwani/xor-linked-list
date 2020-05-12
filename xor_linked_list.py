def get_by_address(address, global_vars):
    if address == 0:
        return None
    
    return [x for x in global_vars.values() if id(x) == address][0]

class Node(object):
    def __init__(self, data):
        self.data = data
        self.address_store = None
    
    def get_address(self):
        return id(self)
    
    def set_neighbors(self, prev_node=None, next_node=None):
        local_address = self.get_address()
        
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()
        
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()
    
        self.address_store = prev_address ^ next_address
        
    def get_next(self, prev_node, global_vars):
        if self.address_store == None:
            raise Exception('set_neighbors not called yet, no next node!')
            
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()
        
        next_address = self.address_store ^ prev_address
        
        return get_by_address(address=next_address, global_vars=global_vars)
    
    def get_prev(self, next_node, global_vars):
        if self.address_store == None:
            raise Exception('set_neighbors not called yet, no next node!')
        
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()
        
        prev_address = self.address_store ^ next_address
        
        return get_by_address(prev_address, global_vars=global_vars)
