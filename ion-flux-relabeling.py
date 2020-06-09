def main(h,idx):
    maxIndex = 2 ** h - 1
    if maxIndex <= idx:
        return -1
    subTreeSize = maxIndex
    contFlag = True
    nodeOffset = 0
    ans = 0
    while contFlag:
        if subTreeSize == 0:
            contFlag = False
        subTreeSize = (subTreeSize - 1) // 2
        leftNode = nodeOffset + subTreeSize
        rightNode = leftNode + subTreeSize
        rootNode = rightNode + 1

        if (idx == leftNode) or (idx == rightNode):
            ans = rootNode
            contFlag = False
        if idx > leftNode:
            nodeOffset = leftNode
    return ans

def solution(h, q):
    res = [main(h,item) for item in q]
    return res


ans = solution(5,[19,14,28])
print(ans)
