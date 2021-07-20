# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        # print(image) # for debugging
        
        # calculate available bytes
        # 0 is for height or pixels rows,  1 is for width or pixels columns
        # print(image.shape[0], image.shape[1])
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message + self.delimiter
            self.binary = binary
            # your code goes here
            # you may create an additional method that modifies the image array
            row = 0
            col = 0
            bit = 0
            while bit != len(self.binary):
                if col != image.shape[1]-1:
                    for pixel in range(0,3):
                        binary_form = format(image[row][col][pixel], "08b")
                        if binary_form[-1] != self.binary[bit]:
                            binary_form = binary_form[:-1] + self.binary[bit]
                            image[row][col][pixel] = int(binary_form,2)
                        bit+=1
                        if bit == len(self.binary): break
                    col+=1
                else:
                    col=0
                    row+=1
            cv2.imwrite(fileout, image)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        # print(image) # for debugging      
        flag = True
        # convert into text
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # your code goes here
            # you may create an additional method that extract bits from the image array
            # convert each integer in image array into binary and extract the last bit
            binary_data = []
            for row in image:
                for pixel in row:
                    # pixel = [0,0,255]
                    # extracted_bits = [0,1,0]
                    # map takes two arguments: First is the function, second is the array.
                    extracted_bits = list(map(lambda x: format(x, "08b")[-1], pixel))
                    binary_data += extracted_bits
            # print(binary_data)
            # update the data attributes:
            self.binary = "".join(binary_data)
            self.text = self.codec.decode(self.binary)      
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

