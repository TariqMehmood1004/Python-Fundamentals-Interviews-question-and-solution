# 10-practical-implementation-using-networkx.py
import os
import re
import networkx as nx


def EXTRACT_LINKS(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return re.findall(r'href="([^"]+)"', content)


def BUILD_GRAPH(directory):
    G = nx.DiGraph()
    
    for file in os.listdir(directory):
        if file.endswith(".html"):
            file_path = os.path.join(directory, file)
            links = EXTRACT_LINKS(file_path)
            for link in links:
                G.add_edge(file, link)
    
    return G

def FIND_MOST_POPULAR(directory):
    graph = BUILD_GRAPH(directory)
    pagerank_scores = nx.pagerank(graph)
    return max(pagerank_scores, key=pagerank_scores.get)

if __name__ == "__main__":
    directory = "html_files"
    most_popular = FIND_MOST_POPULAR(directory)
    print("[FIND_MOST_POPULAR]:", most_popular)
    # [FIND_MOST_POPULAR]: ./Install — NetworkX 3.6.1 documentation_files/theme.css
