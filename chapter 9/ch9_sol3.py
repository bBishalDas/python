def tables(n):
    table=""
    for x in range(1, 11):
        table+= f"{n} x {x} = {n*x}\n"
    
    with open(f"tablesfile/table_{n}", "w") as f:
        f.write(table)
    


for x in range(2, 21):
    tables(x)