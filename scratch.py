def can_cross_bridge(inventory):
    if "rope" in inventory:
        return True
    else:
        return False

if can_cross_bridge(["lantern"]):
    print("Crossed")
else:
    print("Stuck")

def has_key(inventory):
    if "key" in inventory:
        return True
    else:
        return False
if has_key(["stick"]):
    print("has")
else:
    print("has not")

    
