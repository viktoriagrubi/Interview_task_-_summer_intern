class TrieNode:
    def __init__(self):
        # Node initialization - contains a child map
        # and a flag indicating whether a given node is the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Trie tree initialization with root
        self.root = TrieNode()

    def insert(self, word):
        # Inserting a word into the tree
        node = self.root
        # Iterate through each character of the word
        for char in word:
            # If the character does not exist in the children of the current node, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            # Go to the next node
            node = node.children[char]
        # Mark the last node as the final node of the word
        node.is_end_of_word = True

    def find_candidates(self, query):
        # Find potential autocomplete candidates for your query
        node = self.root
        # Iterate through each question mark
        for char in query:
            # If the character does not exist in the children of the current node, stop searching
            if char not in node.children:
                return []
            node = node.children[char]
        # Return all words starting with the query
        return self._get_all_words_from_node(node, query)

    def _get_all_words_from_node(self, node, prefix):
        # Recursively collect all words starting with a given node
        words = []
        if node.is_end_of_word:
            # If the node is the end of a word, add it to the word list
            words.append(prefix)
        for char, child in node.children.items():
            # Recursively collect words from a node's children
            words.extend(self._get_all_words_from_node(child, prefix + char))
        return words

def build_dictionary(words):
    # Function that builds a Trie tree from a list of words
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

# Implementation testing
def test():
    # Creating a dictionary
    dictionary = build_dictionary(["car", "carpet", "java", "javascript", "internet"])

    # Testing different queries
    print(dictionary.find_candidates("c"))  # ['car', 'carpet']
    print(dictionary.find_candidates("car"))  # ['car', 'carpet']
    print(dictionary.find_candidates("carp"))  # ['carpet']
    print(dictionary.find_candidates("jav"))  # ['java', 'javascript']
    print(dictionary.find_candidates("intern"))  # ['internet']
    print(dictionary.find_candidates("foo"))  # []

test()
