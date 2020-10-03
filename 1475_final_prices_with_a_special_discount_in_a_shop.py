"""
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

"""

def finalPrices(prices):
    i = 0
    while i <= len(prices)-1:
        for j in range(i+1, len(prices)):
            if prices[i] >= prices[j] and j > i:
                prices[i] = prices[i] - prices[j]
                break

        i += 1

    return prices
print(finalPrices([8,4,6,2,3]))
print(finalPrices([1,2,3,4,5]))
print(finalPrices([10,1,1,6])) 