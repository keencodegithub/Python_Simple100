profit = int(input("Your profit(K)?"))
print("your profit is: %d" % profit)

benefit = 0

profitLimit = [1000, 600, 400, 200, 100, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

for i in range(len(profitLimit)):
    if profit > profitLimit[i]:
        print('Your profit is over than %d' % profitLimit[i])
        benefit += (profit - profitLimit[i]) * rate[i]
        profit -= profitLimit[i]
        print('The subtotal benefit you got at this moment is %d' % benefit)

print ('Your total benefit is %d' %benefit)


# if profit > 1000:
#     benefit += (profit - 1000) * 0.01
#     profit = 1000
#
# if profit > 600:
#     benefit += (profit - 600) * 0.015
#     profit = 600
#
# if profit > 400:
#     benefit += (profit - 400) * 0.03
#     profit = 400
#
# if profit > 200:
#     benefit += (profit - 200) * 0.05
#     profit = 200
#
# if profit > 100:
#     benefit += (profit - 100) * 0.075
#     profit = 100
#
# if profit <= 100:
#     benefit += profit * 0.1
#
# print("your benefit is : %d" % benefit)



# 这种解法更高效--------------------------------------------------
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# i = int(raw_input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print (i-arr[idx])*rat[idx]
#         i=arr[idx]
# print r
