def solution(flowerbed, n):
    index_plot = 0
    while 0 < n and index_plot < len(flowerbed):
        if flowerbed[index_plot] != 1 and flowerbed[max(0, index_plot - 1)] != 1 and flowerbed[min(len(flowerbed) - 1, index_plot + 1)] != 1:
            flowerbed[index_plot] = 1
            n -= 1
        index_plot += 1
    if n == 0:
        return True
    return False


print(solution([1, 0, 0, 0, 1, 0, 0], 2))