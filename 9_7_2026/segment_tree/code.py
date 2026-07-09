#segment tree

arr = [5, -1, 3, 2, -4]


n = len(arr)
tree = [0] * (4 * n)

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2

    build(2 * node, start, mid)
    build(2 * node + 1, mid + 1, end)

    tree[node] = tree[2 * node] + tree[2 * node + 1]


def query(node, start, end, left, right):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    return query(2 * node, start, mid, left, right) + \
           query(2 * node + 1, mid + 1, end, left, right)


def update(node, start, end, idx, value):
    if start == end:
        arr[idx] = value
        tree[node] = value
        return

    mid = (start + end) // 2

    if idx <= mid:
        update(2 * node, start, mid, idx, value)
    else:
        update(2 * node + 1, mid + 1, end, idx, value)

    tree[node] = tree[2 * node] + tree[2 * node + 1]


build(1, 0, n - 1)

print("Original Array:", arr)
print("Segment Tree:", tree[:15])

print("Sum of index 1 to 4:", query(1, 0, n - 1, 1, 4))

update(1, 0, n - 1, 2, 6)

print("Updated Array:", arr)
print("Segment Tree after Update:", tree[:15])

print("New Sum of index 1 to 4:", query(1, 0, n - 1, 1, 4))