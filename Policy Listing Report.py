import datetime

CurDate = datetime.datetime.now()

# Format and Print Headings:

print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF {}".format(CurDate.strftime("%d-%b-%y")))
print()
print("POLICY    CUSTOMER                   INSURANCE       EXTRA       TOTAL")
print("NUMBER    NAME                        PREMIUM        COSTS      PREMIUM")
print("=" * 72)


# Set Up Customer Counter:

PolicyCtr = 0

# Set Up Total Cost Accumulator:

InsPremAcc = 0
ExtCostAcc = 0
TotPremAcc = 0


# Read Data from CustExtra.dat:

f = open("Policies.dat", "r")

for PolDataLine in f:
    PolLine = PolDataLine.split(",")

    PolNum = PolLine[0].strip()
    CustFirstName = PolLine[2].strip()
    CustLastName = PolLine[3].strip()
    InsPrem = float(PolLine[13].strip())
    TotExtCost = float(PolLine[14].strip())
    TotInsPrem = float(PolLine[15].strip())

# Format Display Values:

    CustName = CustFirstName + " " + CustLastName
    InsPremDsp = "${:,.2f}".format(InsPrem)
    TotExtCostDsp = "${:,.2f}".format(TotExtCost)
    TotInsPremDsp = "${:,.2f}".format(TotInsPrem)


# Print Report:

    print("{:>7}   {:<20}       {:>9}    {:>9}    {:>9}".format(PolNum, CustName, InsPremDsp, TotExtCostDsp, TotInsPremDsp))

# Calculate Totals:

    PolicyCtr += 1
    InsPremAcc += InsPrem
    ExtCostAcc += TotExtCost
    TotPremAcc += TotInsPrem

# Close file:

f.close()

# Format and Print Totals:

InsPremAccDsp = "${:,.2f}".format(InsPremAcc)
ExtCostAccDsp = "${:,.2f}".format(ExtCostAcc)
TotPremAccDsp = "${:,.2f}".format(TotPremAcc)
print("=" * 72)
print("Total Policies: {:>3}                 {:>10}   {:>10}   {:>10}".format(PolicyCtr, InsPremAccDsp, ExtCostAccDsp, TotPremAccDsp))

