class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char == None:
            return
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        node = self
        def getList(node,word,suffixList):
            if node == None:
                return
            for child in node.children:
                if node.children[child].is_word == True:
                    suffixList.append(word+child)
                getList(node.children[child], word+child, suffixList)

        word = ''
        suffixList = []
        getList(node,word,suffixList)

        return suffixList


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        if word == None:
            return
        
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix == '' or prefix == None:
            return None
        node = self.root
        for char in prefix:
            if node == None:
                return node
            if char in node.children:
                node=node.children[char]
            else:
                node = None
        return node

    def __repr__(self):
        node = self.root
        if node == None:
            print("empty trie")
            return ''
        def printTrie(node, word):
            if node == None:
                return

            for child in node.children:
                if node.children[child].is_word == True:
                    print(word+child)
                printTrie(node.children[child], word+child)
        word = ''
        printTrie(node, word)
        return ''


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod",
    "my","sample", "test"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
        print('\n')
    else:
        print('')

"""
TEST CASE 1
"""
f('s')
"""
Result:
ample
"""

"""
TEST CASE 2
"""
f('a')
"""
Result:
nt
nthology
ntagonist
ntonym
"""

"""
TEST CASE 3
"""
f('d')
"""
Result:
d not found
"""

"""
TEST CASE 4
"""
f('fu')
"""
Result:
n
nction
"""

"""
TEST CASE 5
"""
f('ant')
"""
Result:
hology
agonist
onym
"""

"""
TEST CASE 6
"""
f('tr')
"""
Result:
ie
igger
igonometry
ipod
"""

"""
TEST CASE 7
"""
f('m')
"""
Result:
y
"""

"""
TEST CASE 8
"""
f('')
"""
Result:

"""

"""
TEST CASE 9
"""
f('ye')
"""
Result:
ye not found
"""
