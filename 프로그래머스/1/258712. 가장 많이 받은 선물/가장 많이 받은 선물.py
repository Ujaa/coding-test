def solution(friends, gifts):
    gift_table = dict()
    gift_receive = dict()
    
    for friend in friends:
        gift_table[friend] = dict()
        gift_table[friend]["gift_count"] = 0
        gift_table[friend]["gift_give"] = 0
        gift_table[friend]["gift_receive"] = 0
        gift_receive[friend] = 0
        
        for friend_receive in friends:
            gift_table[friend][friend_receive] = 0
    
    for gift in gifts:
        give, receive = gift.split()
        gift_table[give][receive] += 1
        gift_table[give]["gift_count"] += 1
        gift_table[give]["gift_give"] += 1
        gift_table[receive]["gift_count"] -= 1
        gift_table[receive]["gift_receive"] += 1

    for f1, f2 in combination(friends, 2):
        if(gift_table[f1][f2] != 0 or gift_table[f2][f1] != 0) and gift_table[f1][f2] != gift_table[f2][f1]:
            if gift_table[f1][f2] > gift_table[f2][f1]:
                gift_receive[f1] += 1
            elif gift_table[f1][f2] < gift_table[f2][f1]:
                gift_receive[f2] += 1
        if (gift_table[f1][f2] == 0 and gift_table[f2][f1] == 0) or gift_table[f1][f2] == gift_table[f2][f1]:
            if gift_table[f1]["gift_count"] > gift_table[f2]["gift_count"]:
                gift_receive[f1] += 1 
            elif gift_table[f1]["gift_count"] < gift_table[f2]["gift_count"]:
                gift_receive[f2] += 1

    return max(gift_receive.values())
    
def combination(arr, r):
    result = []
    
    def helper(current, start):
        if len(current) == r:
            result.append(current)
            return
        
        for i in range(start, len(arr)):
            helper(current + [arr[i]], i + 1)
    
    helper([], 0)
    return result
        