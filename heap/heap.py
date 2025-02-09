# changes added
#test for commit
heap = []


def insert(ele, heap):
    heap.append(ele)

    if len(heap) > 1:
        shift_up(len(heap)-1, heap)

    return True


def get_max(heap):
    if not heap:
        return False
    max_ele = heap[0]
    last_ele = heap.pop()

    if heap:
        heap[0] = last_ele
        shift_down(0, heap)
    return max_ele


def shift_up(index, heap):
    parent = get_parent(index)

    while parent is not None and heap[parent] < heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        parent = get_parent(index)


def shift_down(index, heap):
    while True:
        r_child = 2 * index + 1 if 2 * index + 1 < len(heap) else None
        l_child = 2 * index + 2 if 2 * index + 2 < len(heap) else None

        largest = index

        if l_child is not None and heap[l_child] > heap[largest]:
            largest = l_child
        if r_child is not None and heap[r_child] > heap[largest]:
            largest = r_child

        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            index = largest
        else:
            break


def get_parent(index):
    return (index-1)//2 if index != 0 else None


lst = [3, 4, 5, 5, 6, 7, 8, 9]
for i in lst:
    insert(i, heap)


for i in lst:
    print(heap)
    print(get_max(heap))

print(heap)
