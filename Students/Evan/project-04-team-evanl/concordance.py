from hash_quad import *
import string

FILENOTFOUND_MESSAGE = "File Not found"
class Concordance:

    def __init__(self):
        self.stop_table = HashTable(191)          # hash table for stop words
        self.concordance_table = HashTable(191)   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, "r", encoding="utf-8")
            print("hello")
        except FileNotFoundError:
            print(FILENOTFOUND_MESSAGE)
            raise

        for line in f:
            self.stop_table.insert(line[:-1])
        f.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, "r", encoding="utf-8")
        except FileNotFoundError:
            print(FILENOTFOUND_MESSAGE)
        line_number = 1
        for line in f:
            if line[-1] == "\n":
                line = line[:-1] # get rid of newline
            line = [i for i in line if i != "'"]
            for idx, char in enumerate(line):
                if char in string.punctuation:
                    line[idx] = " "
            line = "".join(line)
            line = line.lower().split(" ")
            line = list(filter(self.check_token, line))
            for token in line:
                if self.concordance_table.in_table(token):
                    line_numbers = self.concordance_table.get_value(token)
                    line_numbers.append(str(line_number))
                    self.concordance_table.insert(token, line_numbers)
                else:
                    self.concordance_table.insert(token, [str(line_number)])
            line_number += 1
        f.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        try:
            f = open(filename, "w+", encoding="utf-8")
        except FileNotFoundError:
            print(FILENOTFOUND_MESSAGE)
        hash_table = list(filter(lambda x: x != None,self.concordance_table.hash_table))
        hash_table.sort(key=lambda x: x[0])
        for index, (token, line_numbers) in enumerate(hash_table): # unpacking 
            line_numbers = " ".join(line_numbers)
            if index == len(hash_table) - 1:
                f.write(f"{token}: {line_numbers}")
            else:
                f.write(f"{token}: {line_numbers}\n")
        f.close()

    # helper functions
    def check_token(self, word):
        stop_words = self.stop_table.get_all_keys()
        if word.isalpha() and word not in stop_words:
            return True
        return False
