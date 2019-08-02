# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=''):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, word, handler=''):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if word == None:
            return
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if path == None:
            return None
        node = self.root
        for char in path:
            if node == None:
                return None
            if char in node.children:
                node = node.children[char]
            else:
                node = None

        if node == None:
            return None
        elif node.handler == '':
            return None
        else:
            return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=''):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, char, handler=''):
        # Insert the node as before
        if char == None:
            return
        if char not in self.children:
            self.children[char] = RouteTrieNode(handler)

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, rootHandler='', notFoundHandler = ''):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(rootHandler)
        self.notFoundHandler = notFoundHandler

    def add_handler(self, path, handler=''):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == None:
            return []
        paths =self.split_path(path)

        prev = ''
        for item in paths:
            if item == '':
                continue
            if(self.router.find(prev+item) == None):
                self.router.insert(prev+item)
            prev = item

        self.router.insert(item,handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == None:
            return self.notFoundHandler

        if path == '' or path == "/":
            return self.router.root.handler

        pathItems = self.split_path(path)
        for item in pathItems:
            if item == '':
                continue
            handler = self.router.find(item)

        if handler == '' or handler == None:
            return self.notFoundHandler

        return handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == None:
            return []

        return path.split("/")


# Here are some test cases and expected outputs you can use to test your implementation
"""
TEST DATA
"""
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home", "home handler")  # add a route
router.add_handler("/home/about/me", "about me handler")  # add a route
router.add_handler("/home/about/me", "about me second handler")  # add a route

# some lookups with the expected output
"""
TEST CASE 1
"""
print(router.lookup("/")) # should print 'root handler'
"""
RESULT:
root handler
"""

"""
TEST CASE 2
"""
print(router.lookup("/home")) # should print 'home handler' or None if you did not implement one
"""
RESULT:
home handler
"""

"""
TEST CASE 3
"""
print(router.lookup("/home/")) # should print 'home handler' or None if you did not implement one
"""
RESULT:
home handler
"""

"""
TEST CASE 4
"""
print(router.lookup("/home/about")) # should print 'about handler'
"""
RESULT:
about handler
"""

"""
TEST CASE 5
"""
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
"""
RESULT:
about handler
"""

"""
TEST CASE 6
"""
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
"""
RESULT:
about me second handler
"""

"""
TEST CASE 7
"""
print(router.lookup("/home/about/nohandler")) # should print 'not found handler' or None if you did not implement one
"""
RESULT:
not found handler
"""
