import heapq

class Node:
    def __init__(self, freq, symbol):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(chars, freq):
    pq = []
    for i in range(len(chars)):
        heapq.heappush(pq, Node(freq[i], chars[i]))

    while len(pq) > 1:
        node1 = heapq.heappop(pq)
        node2 = heapq.heappop(pq)
        merged_freq = node1.freq + node2.freq
        merged_node = Node(merged_freq, None)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(pq, merged_node)

    root = pq[0]
    codes = {}
    build_codes(root, "", codes)
    return codes

def build_codes(node, code, codes):
    if node.symbol:
    else:
        build_codes(node.left, code + "0", codes)
        build_codes(node.right, code + "1", codes)

chars = input("Enter characters separated by spaces: ").split()
freq = list(map(int, input("Enter corresponding frequencies separated by spaces: ").split()))

codes = huffman_codes(chars, freq)
print("Huffman Codes:")
for char, code in codes.items():
    print(f"{char}: {code}")