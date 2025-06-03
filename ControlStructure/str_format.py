price = 12.3
qty = 3
total = price * qty
print("price is {} qty is {} total is {}".format(price,qty,total))
print("qty is {1} price is {0} total is {2}".format(price,qty,total))
print("qty is {q} price is {p} total is {t}".format(q = qty, p = price, t = total))
print(f"price is {price} qty is {qty} total is {total}")

print("Quantity is:{:d}".format(qty))
print("Quantity is:{:5d}".format(qty))
print("Quantity is:{:05d}".format(qty))

print("total is:{:f}".format(total))
print("total is:{:.2f}".format(total))
print("total is:{:7.2f}".format(total))
print("total is:{:07.2f}".format(total))

print("Quantity in binary is:{:b}".format(qty))
