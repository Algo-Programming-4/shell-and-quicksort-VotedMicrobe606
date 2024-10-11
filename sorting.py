def bubble(nums):
    length = len(nums)
    newArr = nums[:]
    for i in range(length):
        for j in range(length - 1):
            if newArr[j] > newArr[j + 1]:
                temp = newArr[j]
                newArr[j] = newArr[j + 1]
                newArr[j + 1] = temp
    return newArr

def selection(nums):
    length = len(nums)
    newArr = nums[:]
    for i in range(length):
        minIndex = i
        for j in range(i + 1, length):
            if newArr[j] < newArr[minIndex]:
                minIndex = j
        temp = newArr[i]
        newArr[i] = newArr[minIndex]
        newArr[minIndex] = temp
    return newArr

def insertion(nums):
    length = len(nums)
    newArr = nums[:]
    for i in range(1, length):
        key = newArr[i]
        j = i - 1
        while j >= 0 and newArr[j] > key:
            newArr[j + 1] = newArr[j]
            j -= 1
        newArr[j + 1] = key
    return newArr

def shell(nums):
    n=len(nums)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=nums[i]
            j=i
            while j>=gap and nums[j-gap]>temp:
                nums[j] = nums[j-gap]
                j-=gap
            nums[j]=temp
        gap//=2
    return nums




def quicksort(nums):
  if len(nums)<=1:
    return nums
  else:
    p=nums[len(nums)//2]
    left = [x for x in nums if x<p]
    mid = [x for x in nums if x==p]
    right = [x for x in nums if x>p]
    return quicksort(left) + mid + quicksort(right)
