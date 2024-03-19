class Queue():    
    def __init__(self):
        self.size = 0
        self.list = []

    def enqueue(self, data):
        self.list.append(data)
        self.size += 1

    def dequeue(self):
        try:
            self.size -= 1
            return self.list.pop(0)
        except Exception as error:
            print(f'{error} is not possible')     

    def xprint(self, index):
        print(self.list[index])




def breadth_first(graph, root):

    queue = Queue()
    visited_nodes = list()
    queue.enqueue(root)
    visited_nodes.append(root)
    current_node = root
    
    while queue.size > 0:
        current_node = queue.dequeue()
        adj_nodes = graph[current_node]
        remaining_elements = sorted(set(adj_nodes) - set(visited_nodes))

        if len(remaining_elements) > 0:
            for element in remaining_elements:
                visited_nodes.append(element)
                queue.enqueue(element)
    
    return visited_nodes



if __name__ == '__main__':
    
    graph = dict()

    graph['1'] = ['2', '7', '4']
    graph['2'] = ['1', '6', '5']
    graph['3'] = ['6', '8']
    graph['4'] = ['6', '1']
    graph['5'] = ['2', '7']
    graph['6'] = ['2', '4', '3']
    graph['7'] = ['1', '5']
    graph['8'] = ['3']

    print(breadth_first(graph, '8'))
print("Anakha R Menon")
print("ROLL.NO-CH.EN.U4CSE20103\n")
