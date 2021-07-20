# codecs
import numpy as np

class Codec():
    
    def __init__(self):
        self.name = 'binary'
        self.delimiter = '00100011' # a hash symbol '#' 

    # convert text or numbers into binary form    
    def encode(self, text):
        if type(text) == str:
            # my own code
            result = ''.join([format(ord(i), "08b") for i in text])
            result += self.delimiter
            return result
        else:
            print('Format error')

    # convert binary data into text
    def decode(self, data):
        binary = []    
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.delimiter:
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            # int(byte,2) converts binary/byte representation to ASCII code.
            # chr() takes the ASCII code and find its corresponding value/character.
            text += chr(int(byte,2))       
        return text 

class CaesarCypher(Codec):

    def __init__(self, shift=3):
        self.name = 'caesar'
        self.delimiter = '00100011'  # you may need to set up it to a corresponding binary code
        self.shift = shift    
        self.chars = 256      # total number of characters

    # convert text into binary form
    # your code should be similar to the corresponding code used for Codec
    def encode(self, text):
        data = ''
        if type(text) == str:
            # my own code
            data = ''.join([format((ord(i)+self.shift)%255, "08b") for i in text])
            data += self.delimiter
            return data
        else:
            print('Format error')
    
    # convert binary data into text
    # your code should be similar to the corresponding code used for Codec
    def decode(self, data):
        binary = []        
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.delimiter:
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte,2)-self.shift)       
        return text 

# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''
        
class HuffmanCodes(Codec):
    
    def __init__(self):
        self.nodes = None
        self.name = 'huffman'

    # make a Huffman Tree    
    def make_tree(self, data):
        # make nodes
        nodes = []
        for char, freq in data.items():
            nodes.append(Node(freq, char))
            
        # assemble the nodes into a tree
        while len(nodes) > 1:
            # sort the current nodes by frequency
            nodes = sorted(nodes, key=lambda x: x.freq)
            print(nodes)

            # pick two nodes with the lowest frequencies
            left = nodes[0]
            right = nodes[1]

            # assign codes
            left.code = '0'
            right.code = '1'

            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)

            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        return nodes

    # traverse a Huffman tree
    def traverse_tree(self, node, val):
        next_val = val + node.code
        if(node.left):
            self.traverse_tree(node.left, next_val)
        if(node.right):
            self.traverse_tree(node.right, next_val)
        if(not node.left and not node.right):
            print(f"{node.symbol}->{next_val}") # this is for debugging
            # you need to update this part of the code
            # or rearrange it so it suits your need
            return val

    def assign_codes(self, node, keys, codes, code=''):
        for symbol in keys:
            if node.left and symbol in node.left.symbol:
                code += node.left.code
                self.assign_codes(node.left, [symbol], codes, code)
            elif node.right and symbol in node.right.symbol:
                code += node.right.code
                self.assign_codes(node.right, [symbol], codes, code)
            elif not node.left and not node.right:
                codes[symbol] = code 
                code = ''
        return codes
    # convert text into binary form
    def encode(self, text):
        data = ''
        data_dict = {}
        # your code goes here
        # you need to make a tree
        # and traverse it
        for c in text:
            if c in data_dict:
                data_dict[c] += 1
            else:
                data_dict[c] = 1
        tree = self.make_tree(data_dict)[0]
        code_dict = {}
        code_dict = self.assign_codes(tree, data_dict.keys(),code_dict)
        # print(code_dict)
        for c in text:
            data += code_dict[c]
        return data

    # convert binary data into text
    def decode(self, data):
        text = ''
        # your code goes here
        # you need to traverse the tree
        return text

# driver program for codec classes
if __name__ == '__main__':
    text = 'hello'
    print('Original:', text)

    c = Codec()
    binary = c.encode(text)
    print('Binary:',binary)
    data = c.decode(binary)
    print('Text:',data)

    cc = CaesarCypher()
    binary = cc.encode(text)
    print('Binary:',binary)
    data = cc.decode(binary)
    print('Text:',data)

    h = HuffmanCodes()
    binary = h.encode(text)
    print('Binary:',binary)
    data = h.decode(binary)
    print('Text:',data)  
