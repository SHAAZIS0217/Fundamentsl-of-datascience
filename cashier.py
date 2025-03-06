item_price=[120,100,230,200]
qnty=[1,2,3,4]
dis=10
tax=8
tot_p=0
for i in range(len(qnty)):
    tot_p+=item_price[i]*qnty[i]

print("total price = ",tot_p)

tot_dis=tot_p*(dis/100)
price_after_dis = tot_p - tot_dis

print("total price after discount ",price_after_dis)

tot_t=price_after_dis*(tax/100)
tot_cost=price_after_dis+tot_t

print("total cost to be paid is ",tot_cost)
