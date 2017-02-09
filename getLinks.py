# Tyler Moore
# Starter code to HW3 Q1.
# author: Shengwei Huang , Yiqing Yu

import urllib
from collections import deque


def getLinks(url, baseurl="http://secon.utulsa.edu/cs2123/webtraverse/"):
    """
    Input: url to visit, Boolean absolute indicates whether URLs should include absolute path (default) or not
    Output: list of pairs of URLs and associated text
    """
    # import the HTML parser package
    try:
        from BeautifulSoup import BeautifulSoup
    except:
        print 'You must first install the BeautifulSoup package for this code to work'
        raise
    # fetch the URL and load it into the HTML parser
    soup = BeautifulSoup(urllib.urlopen(url).read())
    # pull out the links from the HTML and return
    return [baseurl + a["href"].encode('ascii', 'ignore') for a in soup.findAll('a')]


def print_dfs(url):
    S,Q=set(),[]
    Q.append(url)
    while Q:
        u=Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(getLinks(u))
        print u


    """
    Print all links reachable from a starting **url**
    in depth-first order
    """
    #



def print_bfs(url):
    """
    Print all links reachable from a starting **url**
    in breadth-first order
    """
    #
    S,Q =set(),deque()
    Q.append(url)
    while Q:
        u=Q.popleft()
        if u in S: continue
        S.add(u)
        Q.extend(getLinks(u))
        print u



def find_shortest_path(url1,url2):
    """
    Find and return the shortest path
    from **url1** to **url2** if one exists.
    If no such path exists, say so.
    """
    P, Q = {url1: None}, deque([url1])
    while Q:
        u = Q.popleft()
        for v in getLinks(u):
            if v in P: continue
            P[v] = u
            Q.append(v)
    path = [url2]
    u = url2
    if url2 in P:
        while P[u] != url1:
            if P[u] is None:
                print "path not found"
                break
            path.append(P[u])
            u = P[u]
        path.append(P[u])
        path.reverse()
        print path
    else:
        print "path not found"

def find_max_depth(start_url):
    """
    Find and return the URL that is the greatest distance from start_url, along with the sequence of links that must be followed to reach the page.
    For this problem, distance is defined as the minimum number of links that must be followed from start_url to reach the page.
    """
    print "****** sequence of links that must be followed to reach the page *****"
    S, Q = set(), deque()
    Q.append(start_url)
    while Q:
        u = Q.popleft()
        if u in S: continue
        b = u
        S.add(u)
        Q.extend(getLinks(u))
    find_shortest_path(start_url,b)
    print "****** URL that is the greatest distance from start_url  *****"
    print b

if __name__ == "__main__":
    starturl = "http://secon.utulsa.edu/cs2123/webtraverse/index.html"
    print "*********** (a) Depth-first search   **********"
    print_dfs(starturl)
    print "*********** (b) Breadth-first search **********"
    print_bfs(starturl)
    print "*********** (c) Find shortest path between two URLs ********"
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/index.html",
                       "http://secon.utulsa.edu/cs2123/webtraverse/wainwright.html")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/turing.html",
                       "http://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html")
    print "*********** (d) Find the longest shortest path from a starting URL *****"
    find_max_depth(starturl)

