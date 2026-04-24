import tkinter as tk
from graph import Graph
from bfs import bfs
from dfs import dfs

g = Graph()

def add_edge():
    u = entry1.get()
    v = entry2.get()
    if u and v:
        g.add_edge(u, v)
        output.insert(tk.END, f"✅ Edge added: {u} - {v}\n")

def run_bfs():
    s = start.get()
    g_node = goal.get()

    path, explored = bfs(g, s, g_node)

    if path:
        output.insert(tk.END, f"\n🔵 BFS Path: {' → '.join(path)}\n")
        output.insert(tk.END, f"Nodes Explored (BFS): {explored}\n")
    else:
        output.insert(tk.END, "\n❌ No path found using BFS\n")

def run_dfs():
    s = start.get()
    g_node = goal.get()

    path, explored = dfs(g, s, g_node)

    if path:
        output.insert(tk.END, f"\n🟢 DFS Path: {' → '.join(path)}\n")
        output.insert(tk.END, f"Nodes Explored (DFS): {explored}\n")
    else:
        output.insert(tk.END, "\n❌ No path found using DFS\n")

def compare():
    s = start.get()
    g_node = goal.get()

    bfs_path, bfs_nodes = bfs(g, s, g_node)
    dfs_path, dfs_nodes = dfs(g, s, g_node)

    output.insert(tk.END, "\n📊 --- Comparison ---\n")

    if bfs_path and dfs_path:
        output.insert(tk.END, f"BFS Path Length: {len(bfs_path)} (Optimal)\n")
        output.insert(tk.END, f"DFS Path Length: {len(dfs_path)} (Not guaranteed)\n")
        output.insert(tk.END, f"BFS Nodes Explored: {bfs_nodes}\n")
        output.insert(tk.END, f"DFS Nodes Explored: {dfs_nodes}\n")

root = tk.Tk()
root.title("Smart Navigation System")
root.geometry("400x500")

tk.Label(root, text="Enter Edge (Node1, Node2)").pack()

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add Edge", command=add_edge).pack(pady=5)

tk.Label(root, text="Start Node").pack()
start = tk.Entry(root)
start.pack()

tk.Label(root, text="Goal Node").pack()
goal = tk.Entry(root)
goal.pack()

tk.Button(root, text="Run BFS", command=run_bfs).pack(pady=5)
tk.Button(root, text="Run DFS", command=run_dfs).pack(pady=5)
tk.Button(root, text="Compare BFS vs DFS", command=compare).pack(pady=5)

output = tk.Text(root, height=15, width=45)
output.pack(pady=10)

root.mainloop()