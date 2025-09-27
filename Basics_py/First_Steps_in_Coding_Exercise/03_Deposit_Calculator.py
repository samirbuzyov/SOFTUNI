# # Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент. Използвайте следната формула: 
# # сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# От конзолата се четат 3 реда:
#     1. Депозирана сума – реално число в интервала [100.00 … 10000.00]
#     2. Срок на депозита (в месеци) – цяло число в интервала [1…12]
#     3. Годишен лихвен процент – реално число в интервала [0.00 …100.00]

deposited_money = float(input())
time_for_deposited_money_in_months = int(input())
annual_interest_rate = float(input())
annual_interest_rate_percent = annual_interest_rate / 100

result = deposited_money + time_for_deposited_money_in_months * ((deposited_money * annual_interest_rate_percent) / 12)
print(result)