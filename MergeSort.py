# Given 2 sorted arrays of integer, merge them into one array.

def merge(nums1, nums2):
    answer = [None] * (len(nums1)+len(nums2))
    l1 = len(nums1)-1
    l2 = len(nums2)-1
    i = len(nums1) + len(nums2) - 1
    while(l1>=0 and l2>=0):
        if(nums1[l1] < nums2[l2]):
            answer[i] = nums2[l2]
            l2 -= 1
            i-=1
        else:
            answer[i] = nums1[l1]
            l1 -= 1
            i-=1

    while(l1>=0):
        answer[i] = nums1[l1]
        l1-=1
        i-=1
    while(l2>=0):
        answer[i] = nums1[l2]
        l2-=1
        i-=1
    return answer


nums1 = [1,3,5]
nums2 = [2,4,7]
print(merge(nums1, nums2))
