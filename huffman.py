
import heapq
from collections import Counter

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Build Huffman Tree
def build_tree(text):
    frequency = Counter(text)
    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    return heap[0]


# Generate Huffman Codes
def generate_codes(root, code="", codes=None):
    if codes is None:
        codes = {}

    if root.char is not None:
        codes[root.char] = code if code else "0"
        return codes

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)

    return codes


# Encode Text
def encode(text, codes):
    return "".join(codes[char] for char in text)


# Decode Text
def decode(encoded_text, root):
    result = ""
    current = root

    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            result += current.char
            current = root

    return result


# Main Program
text = input("Enter text: ")

root = None
codes = {}

while True:
    print("\n--- HUFFMAN ENCODING ---")
    print("1. Build Huffman Tree")
    print("2. Encode the Text")
    print("3. Decode the Text")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not text:
            print("Please enter some text.")
            continue

        root = build_tree(text)
        codes = generate_codes(root)

        print("\nHuffman Codes:")
        for char, code in codes.items():
            print(repr(char), ":", code)

        print("Huffman Tree built successfully!")

    elif choice == "2":
        if root is None:
            print("Please build the Huffman Tree first.")
        else:
            encoded = encode(text, codes)
            print("Encoded Text:", encoded)

    elif choice == "3":
        if root is None:
            print("Please build the Huffman Tree first.")
        else:
            encoded = encode(text, codes)
            decoded = decode(encoded, root)
            print("Decoded Text:", decoded)

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.")
