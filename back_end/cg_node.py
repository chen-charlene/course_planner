class Node:
    def __init__(self, name) -> None:
        self.item = self
        self.name = name
        self.pre_req_needed: False
        self.pre_req = []
        self.level = None
        self.post = []
        self.setup_level()
    
    def setup_level(self) -> None:
        #setup class level
        code = int(self.name[-4:])
        if code < 1000:
            self.level = 1
        elif code < 2000:
            self.level = 2
        else: self.level = 3

    
    def add_prereq(self, child, index) -> None:
        if child not in self.pre_req[index]:
            self.pre_req[index].append(child)

        if len(self.pre_req) > 0:
            self.pre_req_needed: True

    def initialize_prereq(self, index) -> None:
        self.pre_req = [[] for _ in range(index)]

class headNode:
    def __init__(self) -> None:
        self.no_req = []
    
    def add_child(self, child) -> None:
        if child not in self.no_req:
            self.no_req.append(child)


class Tree:
    def __init__(self) -> None:
        self.start = headNode()
        self.added_courses_name = []
        self.added_courses_node = []
        self.testing_dict= {
            "CSCI0150" : [],
            "CSCI0200" : [["CSCI0120", "CSCI0150", "CSCI0170", "CSCI0190"]],
            "CSCI0170" : [], 
            "CSCI0110" : [], 
            "CSCI0120" : [["CSCI0110"]], 
            "CSCI1470" : [["CSCI0150", "CSCI0170", "CSCI0190", "CSCI0200"],
                          ["MATH0530", "MATH0520", "MATH0540"],
                          ["CSCI0220", "CSCI1450", "CSCI0450", "MATH1610", "APMA1650", "APMA1655"]],
            "MATH0520" : [],
            "APMA1650" : []
        }

    
    def make_node(self, name: str) -> Node:
        if (name in self.added_courses_name):
            return self.get_node(name)
        
        new_node = Node(name)
        self.added_courses_name.append(name)
        self.added_courses_node.append(new_node)
        return new_node
    
    def get_node(self, name: str) -> Node:
        for x in range(0, len(self.added_courses_node)):
            if self.added_courses_node[x].name == name:
                return self.added_courses_node[x]
            
    def populate_tree_helper(self, parent_node: Node, node_name: str, index) -> None:
        for req in self.testing_dict[node_name][index]:
                    req_node = self.make_node(req)
                    req_node.post.append(parent_node)
                    parent_node.add_prereq(req_node, index)

    def populate_tree(self) :
        #take out classes with no prereqs and connect them to self.start
        empty_nodes = [x for x in self.testing_dict.keys() if len(self.testing_dict[x])==0]
        for node in empty_nodes:
            new_node = self.make_node(node)
            self.start.add_child(new_node)
        
        pre_req_nodes = [x for x in self.testing_dict.keys() if len(self.testing_dict[x])!=0]
        for node_name in pre_req_nodes:
            parent_node = self.make_node(node_name)
            #iteration for normal lists
            if len(self.testing_dict[node_name])==1:
                parent_node.initialize_prereq(len(self.testing_dict[node_name]))
                self.populate_tree_helper(parent_node, node_name, 0)
            
            else: 
                parent_node.initialize_prereq(len(self.testing_dict[node_name]))
                for x in range(0, len(self.testing_dict[node_name])):
                    self.populate_tree_helper(parent_node, node_name, x)
        
        print("hi")
            


if __name__ == "__main__":
    tree = Tree()
    tree.populate_tree()
        