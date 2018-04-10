def median_list(nums):
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        return nums[len(nums)//2]
    else:
        return int((nums[len(nums)//2 + 1] + nums[len(nums)//2 - 1])/2.0)

def activity_notification(arr , d):
    notification_count = 0
    for i in range(d, len(arr)):
        median = median_list(arr[i-d:i])
        if arr[i] >= 2* median:
            notification_count += 1
    return count
        
        
