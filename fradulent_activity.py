#Hackerrnk problem link: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem


def activityNotifications(arr, d):
    # Complete this function
    if len(arr) <= d:
        return 0
    elif len(arr) == 1:
        return 0
    elif len(arr) == 2 and d == 1:
        return 1 if arr[1] >= 2 * arr[0] else 0
    notification_count = 0
    for i in range(d, len(arr)):
        median = median_list(arr[i-d:i])
        if arr[i] >= 2* median:
            notification_count += 1
    return notification_count

def median_list(nums):
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        return nums[len(nums)//2]
    else:
        return int((nums[len(nums)//2 + 1] + nums[len(nums)//2 - 1])/2.0)




if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)



################################################### METHOD 2 #######################################
n, d = map(int, input().split())
expenditure = list(map(int, input().split()))


spend_amt = [0]*201

notification = 0

for i in range(d):
    spend_amt[expenditure[i]] += 1

def median(spent_amt):
    temp = 0
    if d%2:
        for i in range(len(spent_amt)):
            temp += spent_amt[i]
            if temp > d//2:
                return i
    else:
        for i in range(len(hist)):
            temp += spent_amt[i]
            if d//2 - temp == 0:
                for j in range(i +1 , len(spent_amt)):
                    if spent_amt[j]:
                        return (i + j) / 2
            elif temp > d//2:
                return i
            
for j in range(d, n):
    if expenditure[j] >= 2*median(spend_amt):
        notification += 1
    spend_amt[expenditure[j]] += 1
    spend_amt[expenditure[j - d]] -= 1

print(notification)
