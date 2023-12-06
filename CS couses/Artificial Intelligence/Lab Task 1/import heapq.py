import heapq

# Function to read the input data from the text file and create a graph
def read_input(file_name):
    graph = {}
    heuristics = {}
    with open(file_name, 'r') as file:
        for line in file:
            data = line.split()
            city = data[0]
            heuristic = int(data[1])
            neighbors = {}
            for i in range(2, len(data), 2):
                neighbor = data[i]
                distance = int(data[i + 1])
                neighbors[neighbor] = distance
            graph[city] = neighbors
            heuristics[city] = heuristic
    return graph, heuristics

# A* search algorithm to find the optimal path
def astar_search(graph, heuristics, start, goal):
    open_list = [(0, start, [])]
    closed_set = set()

    while open_list:
        f, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, f

        if current in closed_set:
            continue

        closed_set.add(current)

        for neighbor, distance in graph[current].items():
            g = len(path) + distance
            h = heuristics[neighbor]
            f = g + h
            new_path = path + [current]

            heapq.heappush(open_list, (f, neighbor, new_path))

    return None, 0

# Main function to read input, take user input, and print the result
def main():
    file_name = "E:/Dev/Master/CS couses/Artificial Intelligence/Lab Task 1/input.txt"  # Update this to your input file
    graph, heuristics = read_input(file_name)

    start_city = input("Start node: ")
    destination_city = input("Destination: ")

    if start_city not in graph or destination_city not in graph:
        print("Start or destination city not found in the graph.")
        return

    path, total_distance = astar_search(graph, heuristics, start_city, destination_city)

    if path:
        print("Path:", " -> ".join(path + [destination_city]))
        print("Total distance:", total_distance, "km")
    else:
        print("NO PATH FOUND")

if __name__ == "__main__":
    main()
