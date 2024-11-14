print("\033c")

def calculateTip(bill, tip):
    total = bill * (1 + (0.01 * tip))
    
    return total

billAmount = 1000
tipPerc = 10

totalBill = calculateTip(billAmount, tipPerc)

print(f"Bill : ${billAmount}")
print(f"Tip Percentage : {tipPerc}%")
print(f"Tip : ${totalBill - billAmount}")
print(f"Total Bill : ${totalBill}")