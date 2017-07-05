# python3 example.py
import ecg
import numpy as np

path = "output/ecg.xml"
leadName = "I"
volt = np.array([0.466666666667,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.933333333333,0.4,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,0.0,0.0666666666667,0.0666666666667,0.0666666666667,0.1,0.1,0.0666666666667,0.0666666666667,0.0,0.0,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0666666666667,-0.1,-0.1,-0.1,-0.1,-0.133333333333,0.133333333333,0.833333333333,0.866666666667,0.766666666667,0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,0.0,0.0,0.0666666666667,0.0666666666667,0.1,0.133333333333,0.133333333333,0.133333333333,0.0666666666667,0.0666666666667,0.0,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.0666666666667,-0.1,-0.1,-0.0666666666667,-0.1,0.1,0.6,0.766666666667,0.333333333333,0.0333333333333,-0.1,-0.1,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,0.0,0.0333333333333,0.0666666666667,0.1,0.1,0.1,0.1,0.0666666666667,0.0666666666667,0.0,-0.0333333333333,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.0666666666667,-0.1,-0.1,-0.1,-0.0666666666667,0.133333333333,0.7,0.833333333333,0.133333333333,0.0,-0.1,-0.1,-0.1,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,0.0,0.0666666666667,0.0666666666667,0.1,0.0,0.0,-0.1,-0.0666666666667,-0.0666666666667,0.0,0.0,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.1,0.1,0.1,0.1,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.1,0.1,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.133333333333,0.133333333333,0.166666666667,0.133333333333,0.166666666667,0.0,-0.733333333333,-0.933333333333,-0.933333333333,-0.266666666667,0.0333333333333,0.166666666667,0.166666666667,0.166666666667,0.166666666667,0.166666666667,0.133333333333,0.133333333333,0.133333333333,0.1,0.1,0.0666666666667,0.0666666666667,0.0333333333333,0.0,-0.0333333333333,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,0.0,0.0666666666667,0.0666666666667,0.0666666666667,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.1,0.1,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.1,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.0666666666667,-0.2,-0.9,-0.966666666667,-0.4,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.133333333333,0.1,0.1,0.1,0.0666666666667,0.0666666666667,0.0666666666667,0.0333333333333,0.0,-0.0333333333333,-0.0666666666667,-0.1,-0.1,-0.1,-0.1,-0.0666666666667,0.0,0.0,0.0333333333333,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.1,0.1,0.1,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0333333333333,0.0,0.0,0.0333333333333,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,-0.0333333333333,-0.866666666667,-0.966666666667,-0.866666666667,-0.133333333333,0.133333333333,0.1,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0333333333333,0.0333333333333,0.0,0.0,-0.0333333333333,-0.1,-0.1,-0.133333333333,-0.133333333333,-0.166666666667,-0.133333333333,-0.133333333333,-0.1,-0.0666666666667,-0.0333333333333,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.0333333333333,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.0,0.0,-1.0,-1.36666666667,-1.36666666667,-1.0,-0.533333333333,-0.0666666666667,0.0,0.0,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0,0.0,0.0,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.0333333333333,-0.0666666666667,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0,0.0,0.1,-0.0666666666667,-0.866666666667,-1.23333333333,-1.16666666667,-0.466666666667,-0.133333333333,0.0,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0333333333333,0.0333333333333,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0333333333333,0.0333333333333,0.0333333333333,0.0666666666667,0.0666666666667,0.0333333333333,0.0666666666667,0.0333333333333,0.0333333333333,0.0666666666667,0.0666666666667,0.0333333333333,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0666666666667,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.0,0.0,-0.0333333333333,-0.0333333333333,0.0666666666667,0.0,-0.233333333333,-1.23333333333,-1.1,-0.633333333333,-0.333333333333,-0.0666666666667,0.0,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0333333333333,0.0,0.0,0.0,0.0,0.0,0.0333333333333,0.0,0.0333333333333,0.0,0.0,0.0,-0.166666666667,-0.166666666667,-0.166666666667,-0.2,-0.2,-0.166666666667,-0.166666666667,0.133333333333,1.43333333333,1.7,1.7,0.5,-0.1,-0.233333333333,-0.233333333333,-0.2,-0.2,-0.2,-0.166666666667,-0.166666666667,-0.166666666667,-0.133333333333,-0.133333333333,-0.133333333333,-0.1,-0.0666666666667,-0.0333333333333,0.0,0.0666666666667,0.1,0.1,0.0666666666667,0.0666666666667,-0.0333333333333,-0.1,-0.1,-0.1,-0.133333333333,-0.133333333333,-0.1,-0.1,-0.1,-0.1,-0.1,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.133333333333,-0.1,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.1,-0.1,-0.1,-0.1,-0.1,0.4,1.56666666667,1.86666666667,1.83333333333,0.5,-0.233333333333,-0.133333333333,-0.1,-0.1,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0,0.0666666666667,0.1,0.133333333333,0.166666666667,0.233333333333,0.266666666667,0.266666666667,0.266666666667,0.233333333333,0.2,0.1,0.0666666666667,0.0333333333333,0.0,0.0,0.0,0.0,0.0333333333333,0.0333333333333,0.0666666666667,0.0666666666667,0.0666666666667,0.0333333333333,0.0333333333333,0.0333333333333,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.0,-0.0333333333333,0.433333333333,1.8,1.9,0.8,0.2,-0.2,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0666666666667,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0,0.0333333333333,0.0666666666667,0.0666666666667,0.133333333333,0.166666666667,0.2,0.2,0.233333333333,0.2,0.166666666667,0.133333333333,0.0666666666667,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0,0.0,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0666666666667,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.0,0.0,0.0,0.0,0.0,0.0,-0.0333333333333,-0.0333333333333,-0.0333333333333,-0.0333333333333,0.4,1.56666666667,1.83333333333,1.83333333333,0.266666666667,-0.166666666667,-0.0666666666667
])

# -------------              ECG Object            -----------------------------

example = ecg.ECG()
print("ECG object Created")
Lead = example.getLead(leadName)
# Define units for voltage for each lead
Lead.setAmplitudValues(volt,'mV')

Lead.setTimeResolution(20)       # Resolution in mS
Lead.setAmplitudResolution(0.05)  # Resolution in mV

# -------------     Save in HL7 aECG format (.xml)     -------------------------
example.exportHL7aECGTemplate(path, "I")
print(".xml created (HL7-aECG)")
