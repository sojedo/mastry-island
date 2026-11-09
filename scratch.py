# # # # # def can_cross_bridge(inventory):
# # # # #     if "rope" in inventory:
# # # # #         return True
# # # # #     else:
# # # # #         return False

# # # # # if can_cross_bridge(["lantern"]):
# # # # #     print("Crossed")
# # # # # else:
# # # # #     print("Stuck")

# # # # # def has_key(inventory):
# # # # #     if "key" in inventory:
# # # # #         return True
# # # # #     else:
# # # # #         return False
# # # # # if has_key(["stick"]):
# # # # #     print("has")
# # # # # else:
# # # # #     print("has not")


# # # # def can_afford(coins, price):
# # # #     print("Checking...")
# # # #     coins = coins - price      # takes the money
# # # #     print("Here is your snack!")
# # # #     return coins >= 0
# # # # print(can_afford(5, 3))
# # # # print(can_afford(5, 3))

# # # # bag = ["pen", "book"]
# # # # bag.append("pen")
# # # # print(bag)
# # # # print(len(bag))

# # # # student = {"name": "Ada", "age": 12}
# # # # print(student.get("grade"))
# # # # print(student["grade"])


# # # # def add_item(bag):
# # # #     bag.append("ruler")

# # # # my_bag = ["pen"]
# # # # add_item(my_bag)
# # # # print(my_bag)

# # # # items =  ["map"]
# # # # if "rope" not in items:
# # # #     items.append("rope")
# # # # if "rope" not in items:
# # # #     items.append("rope")
# # # # print(len(items))
# # # # if "lantern" in items:
# # # #     items.remove("lantern")
# # # # print(items)
# # # # print(len(items))

# # # def rename(names):
# # #     names = ["Zed"]

# # # def add_name(names):
# # #     names.append("Zed")

# # # team = ["Ada"]
# # # rename(team)
# # # print(team)
# # # add_name(team)
# # # print(team)


# def pick_up(player, item):
#     if item not in player["inventory"]:
#         player["inventory"].append(item)

# p = {"energy": 5, "inventory": []}
# pick_up(p, "rope")
# pick_up(p, "rope")
# result = pick_up(p, "lantern")
# print(result)
# print(p["inventory"])
# # print(p["inventory"])
# # print(p["energy"])

def add_once(inventory, item):
    if item not in inventory:
        inventory.append(item)
bag = ["map"]
add_once(bag, "rope")
add_once(bag, "rope")
add_once(bag, "lantern")
print(bag)