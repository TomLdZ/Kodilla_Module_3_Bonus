def build_bridge(chunk,goal):
    elements = []
    length = 0
    while length < goal:
        elements.append(chunk)
        length += chunk
        elements.append(chunk/2)
        length += chunk/2
    elements.pop()
    if sum(elements) == goal:
        return True
    else:
        return False
    
print(build_bridge(2, 18))