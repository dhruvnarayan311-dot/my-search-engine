# Custom DSA Search Engine

An optimized, from-scratch text indexing and searching engine built in C++ utilizing core Data Structures and Algorithms. 

**Created By:** Dhruv Kumar

---

## Key Features & Code Modules

* **Prefix Autocomplete Engine (Trie):** Indexes unique text tokens dynamically, enabling instant query prediction strings and fast prefix autocompletes.
* **Instant Document Lookup (Inverted Index):** Maps internal keywords directly to document IDs and matching frequencies, bypassing the need to perform slow, full-document linear scans.
* **Result Ranking Matrix (Max-Heap):** Sorts matching search document vectors instantly by relevance frequency, ensuring top matching entries load first.
* **Exact Sequence Matcher (KMP Algorithm):** Searches text documents linearly for specific phrases without backtracking using precomputed failure function arrays.

## How to Compile and Run Locally

1. Open your terminal or Command Prompt.
2. Navigate to your project directory:
   ```bash
   cd Desktop/project