## when break is used whole loop is exited immediatly

for a in range(100):
    if a==50:
        break
    print(a)

## when continue is used only the iteration
# in which continue is true will be left and loop will move again    

for b in range(100):
    if b==50:
        continue
    print(b)