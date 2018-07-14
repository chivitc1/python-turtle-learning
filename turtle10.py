list1 = ["apple", "bike", "car", "driver", "exit"]


def search1(targetItem, targetList):
    return targetItem in targetList


def search2(targetItem, targetList):
    for item in targetList:
        if item == targetItem:
            return True
    return False


def search3(targetItem, targetList):
    return not (targetList.index(targetItem) == -1)

def search4(targetItem, sortedList):
    def binarySearch(left, right):
        if left <= right:
            midpoint = (left + right) // 2
            if sortedList[midpoint] == targetItem:
                return True
            elif targetItem < sortedList[sortedList]:
                return binarySearch(left, midpoint -1)
            else:
                return binarySearch(midpoint + 1, right)
        else:
            return False
    return binarySearch(0, len(sortedList) - 1)


def main():
    item = "car"
    print("Search item", item, "in list", list1, "result is: ")
    #print(search1(item, list1))
    # print(search2(item, list1))
    # print(search3(item, list1))
    print(search4(item, list1))


if __name__ == '__main__':
    main()