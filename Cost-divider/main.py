from member import Member
# class to maintain the name,contribution and due or over payment by members

members = []
more_payers = []
less_payers = []
total_cost = 0
average = 0
paying_details = {}

total_member = int(input("Enter the total number of people: "))
print("\n")

# collecting details of each members
for x in range(1,total_member+1):
    name = input(f"Enter the name of the member {x}: ")
    contribution = int(input(f"What is the contribution made by {name}?. Rs. "))
    members.append(Member(name,contribution))
    total_cost += contribution
    print("\n")

average = round(total_cost/total_member,2)

print(f"Total money spent is Rs.{total_cost} and each member should pay Rs. {average}")

# categorizing the members as more and less payers based on their contribution
for x in members:
    x.calculate(average)
    if x.status == 1:
        more_payers.append(x)
    else:
        less_payers.append(x)

# sorting the members according to the highest amount to receive or pay
more_payers.sort(key=lambda x: x.payment,reverse=True)
less_payers.sort(key=lambda x: x.payment,reverse=True)


# final logic for calculation of payment details from less payers to more payers
for less in less_payers:
    while less.payment > 0:
        for more in more_payers:
            if more.payment == 0:
                more_payers.remove(more)
                continue
            elif less.payment > more.payment:
                if less.name in paying_details:
                    paying_details[less.name][more.name] = more.payment
                else:
                    new_dict = {more.name : more.payment}
                    paying_details[less.name] = new_dict

                less.payment = less.payment - more.payment
                more.payment = 0
            else:
                if less.name in paying_details:
                    paying_details[less.name][more.name] = less.payment
                else:
                    new_dict = {more.name : less.payment}
                    paying_details[less.name] = new_dict

                more.payment = more.payment - less.payment
                less.payment = 0
                break

for x in paying_details:
    print(f"{x} should pay: ")
    for y in paying_details[x]:
        print("    ",end=" ")
        print(f"Rs {paying_details[x][y]} to {y}")
    print("\n")