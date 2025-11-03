l1=[23,52,34,23,56,23,52]
it=iter(l1)

while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break

print("this line printed")

# for x in l1:
#     print(x)
