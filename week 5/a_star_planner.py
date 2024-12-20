# -*- coding: utf-8 -*-
"""cell_decomposition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WOdmycbwdj1LjkrbJ_HclwWDh5NvudvH
"""

def get_neighbors(node, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # atas, bawah, kiri, kanan
    for d in directions:
        neighbor = (node[0] + d[0], node[1] + d[1])
        if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
            neighbors.append(neighbor)
    return neighbors

def a_star(start, goal, grid):
    open_list = []  # daftar node yang perlu diperiksa
    closed_list = set()  # daftar node yang sudah diperiksa
    open_list.append(start)  # tambahkan node awal ke open_list

    g = {start: 0}  # menyimpan jarak dari start ke node saat ini
    f = {start: heuristic(start, goal)}  # menyimpan nilai f (cost + heuristic)

    came_from = {}  # melacak jalur

    while open_list:  # selama ada node di open list
        current = min(open_list, key=lambda x: f[x])  # ambil node dengan nilai f terendah

        if current == goal:  # jika mencapai tujuan
            path = []  # jalur kosong untuk menyimpan hasil
            while current in came_from:  # bangun jalur dari goal ke start
                path.append(current)
                current = came_from[current]  # kembali ke node sebelumnya
            path.append(start)  # tambahkan node awal
            return path[::-1]  # kembalikan jalur terbalik
        open_list.remove(current)  # hapus node saat ini dari open_list
        closed_list.add(current)  # tambahkan node ke closed_list

        for neighbor in get_neighbors(current, grid):  # periksa tetangga
            if neighbor in closed_list:  # lewati jika sudah diperiksa
                continue

            tentative_g = g[current] + 1  # hitung jarak sementara
            if neighbor not in open_list:  # jika tetangga belum ada di open_list
                open_list.append(neighbor)  # tambahkan ke open_list
            elif tentative_g >= g.get(neighbor, float('inf')):  # jika jarak lebih besar
                continue

            came_from[neighbor] = current  # melacak dari mana tetangga berasal
            g[neighbor] = tentative_g  # perbarui jarak
            f[neighbor] = g[neighbor] + heuristic(neighbor, goal)  # hitung nilai f
    return []  # kembalikan jalur kosong jika tidak ditemukan

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # menghitung jarak Manhattan

# contoh grid
grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

path = a_star((0, 0), (3, 3), grid)  # memanggil fungsi A* untuk mencari jalur
print("Path:", path)  # menampilkan jalur yang ditemukan
