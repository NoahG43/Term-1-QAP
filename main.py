# Purpose is to make a program for the insurance company
# Author: Noah Gosse
# Date: Dec 6 2021, Last Modified: Dec 14

# Modules

import datetime

# Default File

f = open("OSICDef.dat", "r")

PolicyNum = int(f.readline())
BasicRate = float(f.readline())
DiscRate = float(f.readline())
LiabOptRate = float(f.readline())
GlassCovRate = float(f.readline())
LoanCarRate = float(f.readline())
HSTRate = float(f.readline())
ProcFeeRate = float(f.readline())

f.close()

while True:

# User Inputs

    CustFirst = input("Enter your first name: ")
    CustLast = input("Enter your last name: ")
    StAdd = input("Enter your address: ")
    City = input("Enter your city: ")
    Prov = input("Enter your province: ")
    Postal = input("Enter your postal code: ")
    Phone = input("Enter your phone number: ")
    CarsIns = int(input("Enter the number of cars insured: "))
    LiabOpt = input("Would you like extra liability options (Y / N): ")
    GlassCov = input("Would you like glass coverage (Y / N): ")
    LoanCar = input("Would you like a loaner car (Y / N): ")
    PayMethod = input("How will you be paying (Full or Monthly (F / M)): ")

# Calculations

    if CarsIns > 1:
        Discount = BasicRate * (CarsIns - 1) * .25
    else:
        Discount = 0

    if LiabOpt.upper() == "Y":
        LiabCost = LiabOptRate * CarsIns
    else:
        LiabCost = 0

    if GlassCov.upper() == "Y":
        GlassCost = GlassCovRate * CarsIns
    else:
        GlassCost = 0

    if LoanCar.upper() == "Y":
        LoanCost = LoanCarRate * CarsIns
    else:
        LoanCost = 0

    InsPrem = BasicRate * CarsIns
    ExtraCosts = LiabCost + GlassCost + LoanCost
    TotalPrem = InsPrem + ExtraCosts - Discount
    HST = TotalPrem * .15
    TotalCost = TotalPrem + HST
    MonPay = (TotalCost + ProcFeeRate) / 12

# Receipt

    LiabOptRateStr = "${:,.2f}".format(LiabOptRate)
    LiabOptRatePad = "{:>10}".format(LiabOptRateStr)
    GlassCovRateStr = "${:,.2f}".format(GlassCovRate)
    GlassCovRatePad = "{:>10}".format(GlassCovRateStr)
    LoanCarRateStr = "${:,.2f}".format(LoanCarRate)
    LoanCarRatePad = "{:>10}".format(LoanCarRateStr)
    InsPremStr = "${:,.2f}".format(InsPrem)
    InsPremPad = "{:>10}".format(InsPremStr)
    DiscountStr = "{:,.2f}".format(Discount)
    DiscountPad = "{:>10}".format(DiscountStr)
    TotalPremStr = "${:,.2f}".format(TotalPrem)
    TotalPremPad = "{:>10}".format(TotalPremStr)
    ExtraCostsStr = "${:,.2f}".format(ExtraCosts)
    ExtraCostsPad = "{:>10}".format(ExtraCostsStr)
    HSTStr = "${:,.2f}".format(HST)
    HSTPad = "{:>10}".format(HSTStr)
    TotalCostStr = "${:,.2f}".format(TotalCost)
    TotalCostPad = "{:>10}".format(TotalCostStr)
    MonPayStr = "${:,.2f}".format(MonPay)
    MonPayPad = "{:>10}".format(MonPayStr)

    print()
    print("ONE STOP INSURANCE")
    print("PAYMENT RECEIPT")
    print("=================================")
    print("First Name:            {:<22}".format(CustFirst))
    print("Last Name:             {:<17}".format(CustLast))
    print("Address:               {:<9}".format(StAdd))
    print("City:                  {:<11}".format(City))
    print("Province:              {:<7}".format(Prov))
    print("Postal Code:           {:<14}".format(Postal))
    print("Phone Number:          {:<12}".format(Phone))
    print("=================================")
    print("Cars Insured:                 {:>3}".format(CarsIns))
    print("Extra Liability:       {:>3}".format(LiabOptRatePad))
    print("Glass Coverage:        {:>3}".format(GlassCovRatePad))
    print("Loaner Car:            {:>3}".format(LoanCarRatePad))
    print("=================================")
    print("Premium:               {:>3}".format(InsPremPad))
    print("Discount:              {:>3}".format(DiscountPad))
    print("=================================")
    print("Total Premium:         {:>3}".format(TotalPremPad))
    print("Extra Costs:           {:>3}".format(ExtraCostsPad))
    print("HST:                   {:>3}".format(HSTPad))
    print("Total Cost:            {:>3}".format(TotalCostPad))
    print("Monthly Payment:       {:>3}".format(MonPayPad))

    PolicyNum += 1
# Policies File

    f = open("Policies.dat", "a")

    f.write("{}, ".format(PolicyNum))
    f.write("{}, ".format(CustFirst))
    f.write("{}, ".format(CustLast))
    f.write("{}, ".format(StAdd))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(Postal))
    f.write("{}, ".format(Phone))
    f.write("{}, ".format(CarsIns))
    f.write("{}, ".format(LiabOpt))
    f.write("{}, ".format(GlassCov))
    f.write("{}, ".format(LoanCar))
    f.write("{}, ".format(PayMethod))
    f.write("{}\n".format(MonPay))

    f.close()

    print()
    print("Policy has been saved!")


# Write default values back

    f = open('OSICDef.dat', 'w')
    f.write("{}\n".format(str(PolicyNum)))
    f.write("{}\n".format(str(BasicRate)))
    f.write("{}\n".format(str(DiscRate)))
    f.write("{}\n".format(str(LiabOptRate)))
    f.write("{}\n".format(str(GlassCovRate)))
    f.write("{}\n".format(str(LoanCarRate)))
    f.write("{}\n".format(str(HSTRate)))
    f.write("{}\n".format(str(ProcFeeRate)))
    f.close()


# Prompt to continue

    print()
    Continue = input("Do you want to continue?:  (Y/N)")

    if Continue.upper() == "Y":
        break



# Exception Report

today = datetime.datetime.now()
print("ONE STOP INSURANCE COMPANY")
print("MONTHLY PAYMENT LISTING AS OF {}".format(today))
print()
print("POLICY CUSTOMER          TOTAL            TOTAL    MONTHLY")
print("NUMBER NAME             PREMIUM    HST    COST     PAYMENT")
print("="*58)


PolicyCtr = 0
TotalPremAcc = 0
HSTAcc = 0
TotalCostAcc = 0
MonPayAcc = 0

f = open("Policies.dat", "r")
for Policies in f:
    PoliciesData = Policies.split(",")
    PolicyNum = PoliciesData[0].strip()
    CustFirst = PoliciesData[1].strip()
    CustLast = PoliciesData[2].strip()
    PayMethod = PoliciesData[12].strip()
    TotalPrem = float(PoliciesData[13].strip())

    if PayMethod.upper() == "M":
        HST = TotalPrem * .15
        TotalCost = TotalPrem + HST
        MonPay = TotalCost + ProcFeeRate / 12
        TotalPremStr = "${:,.2f}".format(TotalPrem)
        TotalPremPad = "{:>3}".format(TotalPremStr)
        HSTStr = "${:,.2f}".format(HST)
        HSTPad = "{:>3}".format(HSTStr)
        TotalCostStr = "${:,.2f}".format(TotalCost)
        TotalCostPad = "{:>3}".format(TotalCostStr)
        MonPayStr = "${:,.2f}".format(MonPay)
        MonPayPad = "{:>3}".format(MonPayStr)

        print("{} {} {}         {}  {}   {}  {}".format(PolicyNum, CustFirst, CustLast, TotalPremPad, HSTPad, TotalCostPad, MonPayPad))

        PolicyCtr += 1
        TotalPremAcc += TotalPrem
        HSTAcc += HST
        TotalCostAcc += TotalCost
        MonPayAcc += MonPay

f.close()

print("="*58)
TotalPremAccStr = "${:,.2f}".format(TotalPremAcc)
TotalPremAccPad = "{:>3}".format(TotalPremAccStr)
HSTAccStr = "${:,.2f}".format(HSTAcc)
HSTAccPad = "{:>3}".format(HSTAccStr)
TotalCostAccStr = "${:,.2f}".format(TotalCostAcc)
TotalCostAccPad = "{:>3}".format(TotalCostAccStr)
MonPayAccStr = "${:,.2f}".format(MonPayAcc)
MonPayAccPad = "{:>3}".format(MonPayAccStr)
print("Total Policies {}        {}  {}  {} {}".format(PolicyCtr, TotalPremAccPad, HSTAccPad, TotalCostAccPad, MonPayAccPad))

# Detailed Report
today = datetime.datetime.now()
print()
print()
print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF {}".format(today))
print()
print("POLICY  CUSTOMER       INSURANCE    EXTRA    TOTAL")
print("NUMBER  NAME            PREMIUM     COSTS   PREMIUM")
print("="*54)


PolicyCtr = 0
InsPremAcc = 0
ExtraCostsAcc = 0
TotalPremAcc = 0

f = open("Policies.dat", "r")
for Policies in f:
    PoliciesData = Policies.split(",")
    PolicyNum = PoliciesData[0]
    CustFirst = PoliciesData[1]
    CustLast = PoliciesData[2]
    CarsIns = int(PoliciesData[8])

    if CarsIns > 1:
        Discount = BasicRate * .75
        InsPrem = BasicRate + (CarsIns - 1) * Discount
    else:
        InsPrem = BasicRate

    ExtraCosts = LiabOptRate + GlassCovRate + LoanCarRate
    TotalPrem = BasicRate + ExtraCosts

    InsPremStr = "${:,.2f}".format(InsPrem)
    InsPremPad = "{:>3}".format(InsPremStr)
    ExtraCostsStr = "${:,.2f}".format(ExtraCosts)
    ExtraCostsPad = "{:>3}".format(ExtraCostsStr)
    TotalPremStr = "${:,.2f}".format(TotalPrem)
    TotalPremPad = "{:>3}".format(TotalPremStr)

    print("{}  {} {}     {}   {} {}".format(PolicyNum, CustFirst, CustLast, InsPremPad, ExtraCostsPad, TotalPremPad))

    PolicyCtr += 1
    InsPremAcc += InsPrem
    ExtraCostsAcc += ExtraCosts
    TotalPremAcc += TotalPrem

f.close()
print("="*54)
InsPremAccStr = "${:,.2f}".format(InsPremAcc)
InsPremAccPad = "{:>3}".format(InsPremAccStr)
ExtraCostsAccStr = "${:,.2f}".format(ExtraCostsAcc)
ExtraCostsAccPad = "{:>3}".format(ExtraCostsAccStr)
TotalPremAccStr = "${:,.2f}".format(TotalPremAcc)
TotalPremAccPad = "{:>3}".format(TotalPremAccStr)
print("Total Policies: {}     {}   {}  {}".format(PolicyCtr, InsPremAccPad, ExtraCostsAccPad, TotalPremAccPad))
