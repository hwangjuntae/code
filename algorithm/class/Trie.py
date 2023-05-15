class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word
    
    def delete(self, word):
        node = self.root
        node_to_delete = []
        for char in word:
            if char not in node.children:
                return False
            node_to_delete.append((node, char))
            node = node.children[char]
        if not node.end_of_word:
            return False
        node.end_of_word = False
        if node.children:
            return True
        for parent, char in reversed(node_to_delete):
            del parent.children[char]
            if parent.end_of_word or parent.children:
                return True
        return True

trie = Trie()

trie.insert("apple")
assert trie.root.children["a"].children["p"].children["p"].children["l"].children["e"].end_of_word == True

assert trie.search("apple") == True

assert trie.delete("apple") == True
assert trie.search("apple") == False
assert trie.search("a") == False

print("pass")

