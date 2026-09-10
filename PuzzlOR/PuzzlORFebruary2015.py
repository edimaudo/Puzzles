#generate first set of coins
output = []
coinOption = [1,5,10,20]

for a in coinOption:
    for b in coinOption:
        for c in coinOption:
            for d in coinOption:
                for g in coinOption:
                    if a + b + c == 11 and a + d + g == 21:
                        output.extend([a,b,c,d,g])

output2 = []
for e in coinOption:
    for f in coinOption:
        for h in coinOption:
            for i in coinOption:
                if output[3] + e + f == 12 and output[1] + e + h == 16 and output[2] + f + i == 11 and output[4] + h + i == 25:
                    output2.extend([e,f,h,i])
                
finalOutput = [[output[0],output[1],output[2]],[output[3],output2[0],output2[1]],[output[4],output2[2],output2[3]]]
print(finalOutput)
