from base64 import b64decode
from binascii import Error
from collections import deque

encoded = (
    "QS4gVGhpcyBuYW11cGxhdGUgaGVscHMgcGVvcGx1IHJ1cG9ydCBvciBjb2xsZWN0IG1pc3NpbmcgaXR1bXMuCkluIFRoaXMGbmFtZ"
    "XBsYXR1IGlzIGtub3duIGJ5IHRoZSBzaG9ydCBmb3JtIeI1VSU1SLgpDLiBUaG1zIHBvc3R1"
    "ciB0ZWFjaGVzIHRoZSBmb3VyLWx1dHR1ciBtZXRob2QgdXN"
    "1ZCB0byBvcGVyYXR1IGEgZmlyZSB1eHRpbmd1aXNoZXIu"
)

graph = {0: [1], 1: [2], 2: []}
indegree = [0, 1, 1]
queue = deque([0])

try:
    data = b64decode(encoded, validate=True).decode("utf-8").splitlines()
except (Error, UnicodeDecodeError) as error:
    print(f"Cannot decode the supplied text: {error}")
else:
    if len(data) < len(graph):
        print("The decoded text must contain at least three lines.")
    else:
        while queue:
            node = queue.popleft()
            print(data[node])

            for neighbour in graph[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)