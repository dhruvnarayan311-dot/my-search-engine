# Full-Stack DSA Search Engine

An interactive, web-based search engine built from scratch to demonstrate advanced Data Structures and Algorithms. It processes text, predicts queries, and ranks documents in real-time.

**Created By:** Dhruv Kumar

**Live Demo:** [Click here to try the Search Engine](https://your-render-url-goes-here.onrender.com)
*(Note: Replace the link above with your actual Render URL!)*

---

## Core Algorithms & Data Structures

This engine abandons slow, linear document scanning in favor of highly optimized computer science techniques:

* **Prefix Autocomplete (Trie):** Indexes unique text tokens into a tree structure, enabling instant query prediction strings and fast prefix autocompletes as the user types.
* **Instant Document Lookup (Inverted Index):** Maps internal keywords directly to document IDs and matching frequencies, bypassing the need to perform slow, full-document linear scans.
* **Result Ranking Matrix (Max-Heap Simulation):** Sorts matching search document vectors instantly by relevance frequency, ensuring top matching entries load first.
* **Exact Sequence Matcher (KMP Algorithm):** Searches text documents linearly for specific multi-word phrases without backtracking using precomputed failure function arrays.

## Tech Stack

* **Backend Logic:** Python 3
* **Web Framework:** Flask
* **Frontend UI:** HTML, CSS, Vanilla JavaScript (Async Fetch)
* **Production Server:** Gunicorn
* **Deployment:** Render

## How to Run Locally

If you want to run this search engine on your own machine, follow these steps:

1. Clone the repository and navigate into the project folder.
2. Install the required web framework:
   ```text
   pip3 install -r requirements.txt
