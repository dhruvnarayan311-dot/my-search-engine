from flask import Flask, request, render_template, jsonify
import re

app = Flask(__name__)

# --- 1. DSA: Trie (For Autocomplete) ---
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, results)

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._dfs(node, prefix, results)
        return results


# --- 2. DSA: KMP Algorithm (For Exact Phrase Matching) ---
class KMP:
    def _compute_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, text, pattern):
        text = text.lower()
        pattern = pattern.lower()
        n = len(text)
        m = len(pattern)
        if m == 0: return True
        
        lps = self._compute_lps(pattern)
        i = 0  # index for text
        j = 0  # index for pattern
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == m:
                return True  # Match found
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False


# --- 3. DSA: Inverted Index & Search Coordinator ---
class SearchEngine:
    def __init__(self):
        self.documents = []
        self.index = {}
        self.trie = Trie()
        self.kmp = KMP()

    def add_document(self, doc_id, title, content):
        self.documents.append({"id": doc_id, "title": title, "content": content})
        words = re.findall(r'\b\w+\b', content.lower())
        for word in words:
            if word not in self.index:
                self.index[word] = {}
            self.index[word][doc_id] = self.index[word].get(doc_id, 0) + 1
            self.trie.insert(word)

    def smart_search(self, query):
        query = query.strip()
        # If the query contains spaces, treat it as an exact phrase match via KMP
        if " " in query:
            results = []
            for doc in self.documents:
                if self.kmp.search(doc["content"], query):
                    results.append({"title": doc["title"], "content": doc["content"], "score": "Exact Match"})
            return results
        
        # Otherwise, fall back to single Keyword Inverted Index lookup
        else:
            query = query.lower()
            if query not in self.index:
                return []
            doc_scores = sorted(self.index[query].items(), key=lambda x: x[1], reverse=True)
            results = []
            for doc_id, score in doc_scores:
                for doc in self.documents:
                    if doc["id"] == doc_id:
                        results.append({"title": doc["title"], "content": doc["content"], "score": f"Matches: {score}"})
            return results


# --- Initialize Engine ---
engine = SearchEngine()
engine.add_document(1, "Data Structures Intro", "A trie is a tree data structure used for tracking prefixes.")
engine.add_document(2, "Advanced Search Algorithms", "KMP matching is highly efficient for exact string algorithms.")
engine.add_document(3, "Binary Heaps and Priority Queues", "Heaps are used to build priority queues which rank items efficiently.")


# --- Web Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def perform_search():
    query = request.args.get("q", "")
    results = engine.smart_search(query)
    return jsonify(results)

@app.route("/autocomplete", methods=["GET"])
def perform_autocomplete():
    prefix = request.args.get("q", "").lower()
    suggestions = engine.trie.autocomplete(prefix)
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)