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

class LoggingFile():
    def __init__(self, FilePath: str, Mode: str = "w"):
        self.FilePath = FilePath
        self.File = open(FilePath, Mode)

    def LogEvent(self, Event, NewLine: bool = True):
        self.File.write(f"{datetime.now():%H:%M:%S} | {Event}" + ("\n" if NewLine else ""))
        self.File.flush()

    
    def LogInformation(self, Input, NewLine: bool = True):
        self.File.write(str(Input) + "\n" if NewLine else str(Input))
        self.File.flush()

    def Close(self):
        self.File.close()

    def __del__(self):
        if not self.File.closed:
            self.File.close()