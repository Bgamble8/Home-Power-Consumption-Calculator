# Bryan Gamble 251025705
# Home Power Consumption
# This program calculates the total cost of a homes electricity bill by using inputs of usage
# at different times and applying discounts

# Define rate constants
OFF_PEAK_RATE = 0.085
ON_PEAK_RATE = 0.176
MID_PEAK_RATE = 0.119

offPeakUsage = 1
# Sentinel Value to end loop
while offPeakUsage != 0:
    offPeakUsage = float(input("Enter kwh during Off Peak period: "))
    if offPeakUsage != 0:
        onPeakUsage = float(input("Enter kwh during on Peak period: "))
        midPeakUsage = float(input("Enter kwh during mid Peak period: "))
        senior = input("Is owner senior? (Y,y,N,n):")

        totalUsage = offPeakUsage + onPeakUsage + midPeakUsage

        # Off peak cost total
        offPeakCost = offPeakUsage * OFF_PEAK_RATE

        # On peak cost total
        onPeakCost = onPeakUsage * ON_PEAK_RATE

        # mid peak cost total
        midPeakCost = midPeakUsage * MID_PEAK_RATE

        totalCost = offPeakCost + onPeakCost + midPeakCost

# Total usage discount
        if totalUsage < 400:
            totalCost = totalCost * 0.96
# On peak discount
        elif onPeakUsage < 150:
            onPeakCost = onPeakCost * 0.95
            totalCost = offPeakCost + onPeakCost + midPeakCost
# Senior discount
        if senior == "y" or senior == "Y":
            totalCost = totalCost * 0.89
# Calculate total
        totalCost = totalCost * 1.13

        print("Electricity cost: $%.2f" % totalCost)
