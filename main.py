# Stephanie Thompson
# Paint Calculator

cansNeeded = 0.0
sqftPerGallon = float(350.0)
gallonsPerCan = 1.0

# Create var and Prompt for wall height input
wallHeight = float(input("Enter wall height (feet): "))

# Create var Prompt for wall width input
wallWidth = float(input("Enter wall width (feet): "))

# Calculate and output wall area
wallArea = wallHeight * wallWidth
print("Total wall area = ", wallArea)

# Calculate and output number of gallons needed
gallonsNeeded = wallArea / sqftPerGallon
print("Amount needed in gallons for job:", gallonsNeeded, "gallons")

# Calculate and output number of pints needed
quartsNeeded = wallArea / (sqftPerGallon / 4)
print("Amount needed in quarts for job:", quartsNeeded, "quarts")
