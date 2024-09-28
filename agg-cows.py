def canPlaceCows(stalls, n, cows, minDist):
    count = 1  # Place the first cow in the first stall
    lastPos = stalls[0]  # Position of the last placed cow

    for i in range(1, n):
        if stalls[i] - lastPos >= minDist:
            count += 1
            lastPos = stalls[i]
        if count == cows:
            return True
    return False

def aggressiveCows(stalls, n, cows):
    stalls.sort()  # Sort stall positions
    low, high = 1, stalls[-1] - stalls[0]  # The range of possible distances
    res = 0

    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(stalls, n, cows, mid):
            res = mid  # Update result if cows can be placed with at least 'mid' distance
            low = mid + 1  # Try for a larger minimum distance
        else:
            high = mid - 1  # Try for a smaller minimum distance
    return res