# budget = float(input())
# n = int(input())
# m = int(input())
# p = int(input())

# n_price = n * 250
# m_price = (35/100 * n_price) * m
# p_price = (0.1 * n_price) * p
# total = n_price + m_price + p_price

# if n > m:
#     total *= (1-0.15)


# if budget > total:
#     left_budget = budget - total
#     print(f'You have {left_budget:.2f} leva left!')
# else:
#     needed_more = total - budget
#     print(f'Not enough money! You need {needed_more :.2f} leva more!')




budget = float(input()) 
n = int(input()) 
m = int(input())  
p = int(input()) 


n_price = n * 250  
m_price = (35 / 100 * n_price) * m  
p_price = (0.1 * n_price) * p  


total = n_price + m_price + p_price


if n > m:
    total *= (1 - 0.15)


if budget >= total:
    left_budget = budget - total 
    print(f'You have {left_budget:.2f} leva left!')
else:
    needed_more = total - budget  
    print(f'Not enough money! You need {needed_more:.2f} leva more!')