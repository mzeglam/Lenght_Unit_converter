def lengthUnitConverter():
	
    global unitconvert
    unitconvert={'Meter':1.0,'Kilometer':10**-3, 'Centimeter':10**2,'Millimeter':10**3, 'Micrometer':10**6,'Nanometer':10**9,
                'Yard':1.09361, 'Mile':6.21371*10**-4, "Foot":3.28084, 'Inch':39.37008}
    print("Welcome to Zeglam's Lenght Unit Converter")
    print(f"The units that this program support are \n{list(unitconvert.keys())}")
    
    fromUnit=input("\nWhat is the unit you would like to convert from: ").capitalize()
    while fromUnit not in list(unitconvert.keys()):
        print(f'{fromUnit} is not support in this program or it is not a length unit')
        print('\nPlease, choose the unit that is support in this program')
        fromUnit=input("\nWhat is the unit you would like to convert from: ").capitalize()
    
    toUnit=input("\nWhat is the unot you would like to convert to: ").capitalize()
    while toUnit not in list(unitconvert.keys()):
        print(f'{toUnit} is not support in this program or it is not a length unit')
        print('\nPlease, choose the unit that is support in this program')
        toUnit=input("\nWhat is the unit you would like to convert from: ").capitalize()
    
    value=float(input("\nWhat is the value that you would like to convert: "))
    
    newUnit=Length(fromUnit,toUnit,value)
    newUnit.lengthconvert()
    print(newUnit)
    print("\nThanks for using Zeglam's Length Unit Converter")
    return 

class Length():
    def __init__(self, fromUnit, toUnit, value):
        self.fromUnit=fromUnit
        self.toUnit=toUnit
        self.value=value
        self.result=None
        
    def __str__(self):
        return (f'\n{self.value} {self.fromUnit} is equal to {self.result} {self.toUnit}')
    
    def lengthconvert(self):
        self.result=self.value*unitconvert[self.toUnit]/unitconvert[self.fromUnit]
        return 
