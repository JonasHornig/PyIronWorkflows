import numpy as np

def CreateStrainRange(ZeroStrainPoint_Percent:float = 0.0, Range_Percent:float = 0.1, NumberOfStrains: int = 5, Regime:str = "even"):
    StrainRange = []
    if Regime == "even":
        # Ensure that the strain distribution is centered around 0% strain
        if NumberOfStrains % 2 == 0:
            NumberOfStrains += 1
        
        StepSize = Range_Percent/int(NumberOfStrains/2)
        OneSidedStrain = [Strain.item() for Strain in np.linspace(ZeroStrainPoint_Percent+StepSize, Range_Percent, num=int(NumberOfStrains/2))]
        
        for Strain in reversed(OneSidedStrain):
            StrainRange.append(-1*Strain)
        StrainRange.append(ZeroStrainPoint_Percent)
        for Strain in OneSidedStrain:
            StrainRange.append(Strain)
    return StrainRange
