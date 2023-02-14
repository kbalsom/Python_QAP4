# Program written for the One Stop Insurance Company
# to enter and calculate new insurance policy information for its customers.

# Program Written by: Kara Balsom
# Date Written: March 28, 2022

# Import Libraries:

import datetime

# Set Up Current Date:
CurDate = datetime.datetime.now()

# Read Data from OSICDef.dat:
while True:
    f = open("OSICDef.dat", "r")

    POLICY_NUMBER = int(f.readline())
    BASIC_PREMIUM = float(f.readline())
    ADDITIONAL_CARS_DISCOUNT = float(f.readline())
    EXTRA_LIABILITY_COVERAGE = float(f.readline())
    COST_GLASS_COVERAGE = float(f.readline())
    COST_LOANER_CAR_COVERAGE = float(f.readline())
    HST_RATE = float(f.readline())
    MONTHLY_PAYMENT_PROCESSING_FEE = float(f.readline())

    f.close()

# User Inputs and Validations:

    while True:
        CustFirstName = input("Enter Customer's First Name: ").title()

        if CustFirstName == "":
            print("Customer's First Name cannot be Blank - Please Re-enter.")
        else:
            break

    while True:
        CustLastName = input("Enter the Customer's Last Name: ").title()

        if CustLastName == "":
            print("Customer's Last Name cannot be Blank - Please Re-enter.")
        else:
            break

    while True:
        PhoneNum = input("Please enter the Customer's Phone Number (0000000000): ")

        if PhoneNum == "":
            print("Customer's Phone Number cannot be Blank - Please Re-enter.")
        elif PhoneNum.isdigit() == False:
            print("Customer's Phone Number can only Contain Numbers (0000000000) - Please Re-enter.")
        elif len(PhoneNum) != 10:
            print("Customer's Phone Number must be 10 Digits Long (0000000000) - Please Re-enter.")
        else:
            break

    while True:
        StreetAdd = input("Enter the Customer's Street Address: ").title()

        if StreetAdd == "":
            print("Customer's Street Address cannot be Blank - Please Re-enter.")
        else:
            break

    while True:
        City = input("Enter City: ").title()

        if City == "":
            print("City cannot be Blank - Please Re-enter.")
        else:
            break

    while True:
        Province = input("Enter Province / Territory (XX): ").upper()

        if Province == "":
            print("Province / Territory cannot be Blank (XX) - Please Re-enter.")
        elif Province.isalpha() == False:
            print("Province / Territory cannot Include Numbers - Please Re-enter.")
        elif len(Province) != 2:
            print("Province / Territory must be 2 Letters (XX) - Please Re-enter.")

        else:
            break

    while True:
        Postal = input("Enter Postal Code (A1A1A1): ").upper()

        if Postal == "":
            print("Postal Code cannot be Blank (A1A1A1) - Please Re-enter.")
        elif len(Postal) != 6:
            print("Postal Code must be 6 characters - Please Re-enter.")
        else:
            break

    while True:
        try:
            NumCars = int(input("Enter the Number of Cars being Insured: "))
        except:
            print("Number of Cars can only Contain Numbers - Please Re-enter.")
        else:
            if NumCars == 0:
                print("Number of Cars cannot be 0 - Please Re-enter.")
            else:
                break

    while True:
        OptExtLiab = input("Do You Want Optional Extra Liability up to $ 1,000,000? (Y / N):  ").upper()

        if OptExtLiab == "":
            print("Please Enter Y if Extra Liability was Selected, or N if Extra Liability was Not Selected.")
        elif OptExtLiab != "Y" and OptExtLiab != "N":
            print("Please Enter Y if Extra Liability was Selected, or N if Extra Liability was Not Selected.")
        else:
            break

    while True:
        OptGlassCov = input("Do You Want Optional Glass Coverage? (Y / N):  ").upper()

        if OptGlassCov == "":
            print("Please Enter Y if Glass Coverage was Selected, or N if Glass Coverage was Not Selected.")
        elif OptGlassCov != "Y" and OptGlassCov != "N":
            print("Please Enter Y if Glass Coverage was Selected, or N if Glass Coverage was Not Selected.")
        else:
            break

    while True:
        OptLoaner = input("Do You Want Optional Loaner Car Coverage? (Y / N):  ").upper()

        if OptLoaner == "":
            print("Please Enter Y if Loaner Car Coverage was Selected, or N if Loaner Car Coverage was Not Selected.")
        elif OptLoaner != "Y" and OptLoaner != "N":
            print("Please Enter Y if Loaner Car Coverage was Selected, or N if Loaner Car Coverage was Not Selected.")
        else:
            break

    while True:
        PayOpt = input("Do You Want to Pay in Full or Monthly? (F / M):  ").upper()

        if PayOpt == "":
            print("Please Enter F if Pay in Full was Selected, or M if Pay Monthly was Selected.")
        elif PayOpt != "F" and PayOpt != "M":
            print("Please Enter F if Pay in Full was Selected, or M if Pay Monthly was Selected.")
        else:
            break

# Calculations:

    if NumCars == 1:
        InsPrem = BASIC_PREMIUM
    else:
        InsPrem = BASIC_PREMIUM + (BASIC_PREMIUM * ADDITIONAL_CARS_DISCOUNT) * (NumCars - 1)

    if OptExtLiab == "Y":
        LiabilityCost = EXTRA_LIABILITY_COVERAGE * NumCars
    else:
        LiabilityCost = 0

    if OptGlassCov == "Y":
        GlassCost = COST_GLASS_COVERAGE * NumCars
    else:
        GlassCost = 0

    if OptLoaner == "Y":
        LoanerCost = COST_LOANER_CAR_COVERAGE * NumCars
    else:
        LoanerCost = 0

    TotExtCost = LiabilityCost + GlassCost + LoanerCost

    TotInsPrem = InsPrem + TotExtCost

    TotHST = TotInsPrem * HST_RATE

    TotCost = TotInsPrem + TotHST

    MonthPayment = (TotCost + MONTHLY_PAYMENT_PROCESSING_FEE) / 12

    if PayOpt == "M":
        Payment = MonthPayment
    else:
        Payment = TotCost

    PolicyDate = CurDate

    if CurDate.day > 25:
        CurDate = CurDate.replace(day=1)
        NewYear = CurDate.year
        NewMonth = CurDate.month + 2
        NewDay = CurDate.day
        NewDate = datetime.date(NewYear, NewMonth, NewDay)

    else:
        CurDate = CurDate.replace(day=1)
        NewYear = CurDate.year
        NewMonth = CurDate.month + 2
        NewDay = CurDate.day
        NewDate = datetime.date(NewYear, NewMonth, NewDay)

# Format Data:

    CustName = CustFirstName + " " + CustLastName
    PolicyNum = str(POLICY_NUMBER) + "-" + CustFirstName[0] + CustLastName[0]
    InsPremDsp = "${:,.2f}".format(InsPrem)
    LiabilityCostDsp = "${:,.2f}".format(LiabilityCost)
    GlassCostDsp = "${:,.2f}".format(GlassCost)
    LoanerCostDsp = "${:,.2f}".format(LoanerCost)
    TotExtCostDsp = "${:,.2f}".format(TotExtCost)
    TotInsPremDsp = "${:,.2f}".format(TotInsPrem)
    TotHSTDsp = "${:,.2f}".format(TotHST)
    TotCostDsp = "${:,.2f}".format(TotCost)
    PaymentDsp = "${:,.2f}".format(Payment)

# Print Receipt:

    print()
    print("           One Stop Insurance Company")
    print("        New Insurance Policy Information")
    print("=" * 48)

    print("Customer Info:")
    print("_" * 48)
    print("Customer Name:              {:>20}".format(CustName))
    print("Customer Phone Number:                {:<10}".format(PhoneNum))
    print("Customer Address:      {:>25}".format(StreetAdd))
    print("                      {:>15}, {:<2} {:<6}".format(City, Province, Postal))
    print("=" * 48)

    print("Policy Information:")
    print("_" * 48)
    print("Policy Number:                           {:>7}".format(PolicyNum))
    print("Number of Cars:                                {:>1}".format(NumCars))
    print("Extra Liability Coverage:                      {:>1}".format(OptExtLiab))
    print("Glass Coverage:                                {:>1}".format(OptGlassCov))
    print("Loaner Car Coverage:                           {:>1}".format(OptLoaner))
    print("Payment Option:                                {:>1}".format(PayOpt))
    print("=" * 48)

    print("Payment:")
    print("_" * 48)
    print("Insurance Premium:                    {:>10}".format(InsPremDsp))
    print("Extra Costs:")
    print()
    print("Extra Liability Total:                {:>10}".format(LiabilityCostDsp))
    print("Glass Coverage Total:                 {:>10}".format(GlassCostDsp))
    print("Loaner Total:                         {:>10}".format(LoanerCostDsp))
    print()
    print("Total Extra Costs:                    {:>10}".format(TotExtCostDsp))
    print()
    print("Total Insurance Cost:                 {:>10}".format(TotInsPremDsp))
    print("Total HST:                            {:>10}".format(TotHSTDsp))
    print("=" * 48)
    print("Total Cost:                           {:>10}".format(TotCostDsp))
    if PayOpt == "M":
        print("Total Monthly Payment:                {:>10}".format(PaymentDsp))
        print("First Payment Due:                    {:>10}".format(str(NewDate)))
    print("=" * 48)
# Save Data to Policies.dat file:

    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(PolicyNum)))
    f.write("{}, ".format(str(PolicyDate.strftime("%d-%b-%y"))))
    f.write("{}, ".format(CustFirstName))
    f.write("{}, ".format(CustLastName))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(StreetAdd))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Province))
    f.write("{}, ".format(Postal))
    f.write("{}, ".format(str(NumCars)))
    f.write("{}, ".format(OptExtLiab))
    f.write("{}, ".format(OptGlassCov))
    f.write("{}, ".format(OptLoaner))
    f.write("{}, ".format(float(round(InsPrem, 2))))
    f.write("{}, ".format(float(round(TotExtCost, 2))))
    f.write("{}, ".format(float(round(TotInsPrem, 2))))
    f.write("{}, ".format(PayOpt))
    f.write("{}\n".format(float(round(TotCost, 2))))

# Close the File:

    f.close()

# Display Saved Message to User:

    print()
    print("Policy Processed and Saved.")

# Update Policy Number:

    POLICY_NUMBER += 1

# Overwrite the OSICDef.dat File:

    f = open("OSICDef.dat", "w")

    f.write("{}\n".format(str(POLICY_NUMBER)))
    f.write("{}\n".format(str(BASIC_PREMIUM)))
    f.write("{}\n".format(str(ADDITIONAL_CARS_DISCOUNT)))
    f.write("{}\n".format(str(EXTRA_LIABILITY_COVERAGE)))
    f.write("{}\n".format(str(COST_GLASS_COVERAGE)))
    f.write("{}\n".format(str(COST_LOANER_CAR_COVERAGE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(MONTHLY_PAYMENT_PROCESSING_FEE)))

# Close the File:

    f.close()

# Allow User to Enter Another Policy:

    while True:
        Continue = input("Would You Like to Process Another Policy? (Y / N): ").upper()

        if Continue == "":
            print("Please Enter Y if You Want to Continue, or N if You Want to Exit.")
        elif Continue != "Y" and Continue != "N":
            print("Please Enter Y if You Want to Continue, or N if You Want to Exit.")
        elif Continue == "N":
            print("Thank You for Choosing One Stop Insurance Company!")
            exit()
        else:
            break

# Overwrite the OSICDef.dat File:

f = open("OSICDef.dat", "w")

f.write("{}\n".format(str(POLICY_NUMBER)))
f.write("{}\n".format(str(BASIC_PREMIUM)))
f.write("{}\n".format(str(ADDITIONAL_CARS_DISCOUNT)))
f.write("{}\n".format(str(EXTRA_LIABILITY_COVERAGE)))
f.write("{}\n".format(str(COST_GLASS_COVERAGE)))
f.write("{}\n".format(str(COST_LOANER_CAR_COVERAGE)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(MONTHLY_PAYMENT_PROCESSING_FEE)))

# Close the File:

f.close()









