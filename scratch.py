# # def can_cross_bridge(inventory):
# #     if "rope" in inventory:
# #         return True
# #     else:
# #         return False

# # if can_cross_bridge(["lantern"]):
# #     print("Crossed")
# # else:
# #     print("Stuck")

# # def has_key(inventory):
# #     if "key" in inventory:
# #         return True
# #     else:
# #         return False
# # if has_key(["stick"]):
# #     print("has")
# # else:
# #     print("has not")


# def can_afford(coins, price):
#     print("Checking...")
#     coins = coins - price      # takes the money
#     print("Here is your snack!")
#     return coins >= 0
# print(can_afford(5, 3))
# print(can_afford(5, 3))

# bag = ["pen", "book"]
# bag.append("pen")
# print(bag)
# print(len(bag))

# student = {"name": "Ada", "age": 12}
# print(student.get("grade"))
# print(student["grade"])


# def add_item(bag):
#     bag.append("ruler")

# my_bag = ["pen"]
# add_item(my_bag)
# print(my_bag)

items =  ["map"]
if "rope" not in items:
    items.append("rope")
if "rope" not in items:
    items.append("rope")
print(len(items))
if "lantern" in items:
    items.remove("lantern")
print(items)
print(len(items))