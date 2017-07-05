import numpy as np
import copy

#################################################################################################
##                                     Class LEAD                                               ##
#################################################################################################
class LEAD:

    #--------------------     Initialization       -----------------------------
    def __init__(self):
        self.amplitudValues = []
        self.amplitudResolution = 0     # Minimum Amplitud Increment
        self.amplitudUnit = ""

        self.timeValues = []
        self.timeResolution = 0         # Minimum Time Increment
        self.samplingFrequency = 0
        self.timeUnit = ""

    #------------------     Functions       ------------------------------------
    # Getters and Setters

    # Amplitud
    def getAmplitudValues(self):
        return self.amplitudValues

    def setAmplitudValues(self, newValues, newUnit):
        self.amplitudValues = newValues
        self.setAmplitudUnit(newUnit)

    def getAmplitudResolution(self):
        return self.amplitudResolution

    def setAmplitudResolution(self,newResolution):
        self.amplitudResolution = newResolution

    def getAmplitudUnit(self):
        return self.amplitudUnit

    def setAmplitudUnit(self,newUnit):
        self.amplitudUnit = newUnit

    # Time

    def getTimeValues(self):
        return self.timeValues

    def setTimeValues(self, newValues, newUnit):
        self.timeValues = newValues
        self.setTimeUnit(newUnit)

    def getTimeResolution(self):
        return self.timeResolution

    def setTimeResolution(self,newResolution):
        self.timeResolution = newResolution
        self.samplingFrequency = 1/newResolution

    def getSamplingFrequency(self):
        return self.samplingFrequency

    def setSamplingFrequency(self,newFreq):
        self.samplingFrequency = newFreq
        self.timeResolution = 1/newFreq

    def getTimeUnit(self):
        return self.timeUnit

    def setTimeUnit(self,newUnit):
        self.timeUnit = newUnit

#################################################################################################
##                                     Class ECG                                               ##
#################################################################################################

class ECG:
    #--------------------     Initialization       -----------------------------
    def __init__(self):
        self.subjectName = "JOHN"
        self.LEAD_I = LEAD()
        self.LEAD_II = LEAD()
        self.LEAD_III = LEAD()
        self.LEAD_AVR = LEAD()
        self.LEAD_AVL = LEAD()
        self.LEAD_AVF = LEAD()
        self.LEAD_V1 = LEAD()
        self.LEAD_V2 = LEAD()
        self.LEAD_V3 = LEAD()
        self.LEAD_V4 = LEAD()
        self.LEAD_V5 = LEAD()
        self.LEAD_V6 = LEAD()

        self.incrementTimeValue = 0 # example with a sampling frequency of 500 Hz
        self.incrementTimeUnit = ""
        self.id_root = "2.16.840.1.114396.1.110673.5.2014131" # example
        #Id --> Required: The unique identifier (UID) for this particular AnnotatedECG
        self.globalEffectiveTimeLow = "20031029151120.000"
        self.globalEffectiveTimeLowIsInclusive = "true"
        #self.globalEffectiveTimeHigh = "20031029151121.500"
        self.globalEffectiveTimeHigh = "20031029151120.000"
        self.globalEffectiveTimeHighIsInclusive = "false"
        # EffectiveTime
        # Physiologically relevant time range assigned to the ECG findings derived from the
        # annotated ECG data in the aECG.
        self.clinicalTrialId = "1.3.6.1.4.1.21123.4"    #Example
        self.clinicalTrialExtension = "PROT123"
        # Clinical Trial ID
        # Required: The unique identifier for the trial. Composed of a root and optional extension.
        # The root must be included, and is a UID. The optional extension may be anything. The
        # combination of the root and extension must be universally unique.
        self.birthTime = "19360930"
        self.subjectGender = "M"
        # Gender codeSystem="2.16.840.1.113883.5.1"
        # F – Female
        # M – Male
        # UN – Undifferentiated
        self.subjectTrialId = "1.3.6.1.4.1.21123.4"    #Example
        self.subjectTrialExtension = "001"
        self.timepointCode = "1_H_POST_DOSE"
        # Timepoint code
        # Optional: This is the code naming the time point event. This could be the visit number, study
        # day, etc. The set of time point event codes is usually defined by the protocol. Therefore, the
        # codeSystem UID usually names the protocol.
        self.relativeTimepointCode = "25131"    # example
        # relativeTimepointCode
        # Required: The code for this relative time point. This code is most likely defined by the
        # protocol. Therefore, the codeSystem UID should name the protocol. For example, if the
        # protocol UID is “16.840.1.113883.3.1”, and the time point is “30 minutes post dosage” with
        # the code “POST_DOSAGE_30”, then the XML would like this:
        # <code code=”POST_DOSAGE_30” codeSystem=”16.840.1.113883.3.1”/>
        self.protocolTimepointCode = "1331_10001" # example
        # protocolTimepointCode
        # Required: This is the code naming the time point event as defined in the protocol. This could
        # be the visit number, study day, etc. The codeSystem UID usually names the protocol
        # defining this code.
        self.manufacturerModelName = "H12.Cont.3.10" # example
        self.manufacturerOrganizationName = "Mortara Instrument, Inc." # example
        self.seriesID = "2.16.840.1.114396.1.110673.5.2014131"
    #------------------     Functions       ------------------------------------
    # Getters and Setters
    def getLead(self, leadName):
        leadName = leadName.upper()
        if leadName == "I":
            Lead = self.LEAD_I
        elif leadName == "II":
            Lead = self.LEAD_II
        elif leadName == "III":
            Lead = self.LEAD_III
        elif leadName == "AVR":
            Lead = self.LEAD_AVR
        elif leadName == "AVL":
            Lead = self.LEAD_AVL
        elif leadName == "AVF":
            Lead = self.LEAD_AVF
        elif leadName == "V1":
            Lead = self.LEAD_V1
        elif leadName == "V2":
            Lead = self.LEAD_V2
        elif leadName == "V3":
            Lead = self.LEAD_V3
        elif leadName == "V4":
            Lead = self.LEAD_V4
        elif leadName == "V5":
            Lead = self.LEAD_V5
        elif leadName == "V6":
            Lead = self.LEAD_V6
        else:
            Lead = LEAD()
        return Lead

    def getLeadCopy(self, leadName):
        leadName = leadName.upper()
        if leadName == "I":
            Lead = copy.deepcopy(self.LEAD_I)
        elif leadName == "II":
            Lead = copy.deepcopy(self.LEAD_II)
        elif leadName == "III":
            Lead = copy.deepcopy(self.LEAD_III)
        elif leadName == "AVR":
            Lead = copy.deepcopy(self.LEAD_AVR)
        elif leadName == "AVL":
            Lead = copy.deepcopy(self.LEAD_AVL)
        elif leadName == "AVF":
            Lead = copy.deepcopy(self.LEAD_AVF)
        elif leadName == "V1":
            Lead = copy.deepcopy(self.LEAD_V1)
        elif leadName == "V2":
            Lead = copy.deepcopy(self.LEAD_V2)
        elif leadName == "V3":
            Lead = copy.deepcopy(self.LEAD_V3)
        elif leadName == "V4":
            Lead = copy.deepcopy(self.LEAD_V4)
        elif leadName == "V5":
            Lead = copy.deepcopy(self.LEAD_V5)
        elif leadName == "V6":
            Lead = copy.deepcopy(self.LEAD_V6)
        else:
            Lead = LEAD()
        return Lead

    def getSubjectName(self):
        return self.subjectName
    def setSubjectName(self,name):
        self.subjectName = name

    def getStrSignal(self, signal):
        result = ""
        if(len(signal)!=0):
            for i in range(0,len(signal)):
                if(i == len(signal)-1):
                    result = result + str(signal[i])
                else:
                    result = result + str(signal[i]) + "\t"
        else:
            result = "0"
        return result

    def getId_root(self):
        return self.id_root
    def setId_root(self, id_):
        self.id_root = id_

    def getGlobalEffectiveTimeLow(self):
        return self.globalEffectiveTimeLow
    def setGlobalEffectiveTimeLow(self, TimeLow):
        self.globalEffectiveTimeLow = TimeLow

    def getGlobalEffectiveTimeHigh(self):
        return self.globalEffectiveTimeHigh
    def setGlobalEffectiveTimeHigh(self, TimeHigh):
        self.globalEffectiveTimeHigh = TimeHigh

    def getGlobalEffectiveTimeLowIsInclusive(self):
        return self.globalEffectiveTimeLowIsInclusive
    def setGlobalEffectiveTimeLowIsInclusive(self, val):
        self.globalEffectiveTimeLowIsInclusive = val

    def getGlobalEffectiveTimeHighIsInclusive(self):
        return self.globalEffectiveTimeHighIsInclusive
    def setGlobalEffectiveTimeHighIsInclusive(self, val):
        self.globalEffectiveTimeHighIsInclusive = val

    def getClinicalTrialId(self):
        return self.clinicalTrialId
    def setClinicalTrialId(self, id_):
        self.clinicalTrialId = id_

    def getClinicalTrialExtension(self):
        return self.clinicalTrialExtension
    def setClinicalTrialExtension(self, extension):
        self.clinicalTrialExtension = extension

    def getBirthTime(self):
        return self.birthTime
    def setBirthTime(self, birthTime_):
        self.birthTime = birthTime_

    def getSubjectGender(self):
        return self.subjectGender
    def setSubjectGender(self, gender_):
        self.subjectGender = gender_

    def getSubjectTrialId(self):
        return self.subjectTrialId
    def setSubjectTrialId(self, id_):
        self.subjectTrialId = id_

    def getSubjectTrialExtension(self):
        return self.subjectTrialExtension
    def setSubjectTrialExtension(self, extension):
        self.subjectTrialExtension = extension

    def getTimepointCode(self):
        return self.timepointCode
    def setTimepointCode(self, code):
        self.timepointCode = code

    def getRelativeTimepointCode(self):
        return self.relativeTimepointCode
    def setRelativeTimepointCode(self, code):
        self.relativeTimepointCode = code

    def getProtocolTimepointCode(self):
        return self.protocolTimepointCode
    def setProtocolTimepointCode(self, code):
        self.protocolTimepointCode = code

    def getManufacturerModelName(self):
        return self.manufacturerModelName
    def setManufacturerModelName(self, name):
        self.manufacturerModelName = name

    def getManufacturerOrganizationName(self):
        return self.manufacturerOrganizationName
    def setManufacturerOrganizationName(self, name):
        self.manufacturerOrganizationName = name

    def getSeriesID(self):
        return self.seriesID
    def setSeriesID(self, id_):
        self.seriesID = id_

    def getIncrementTimeValue(self):
        return self.incrementTimeValue
    def setIncrementTimeValue(self, frec_):
        self.incrementTimeValue = frec_

    def getIncrementTimeUnit(self):
        return self.incrementTimeUnit
    def setIncrementTimeUnit(self, unit):
        self.incrementTimeUnit = unit

    def createEmptySignal(self, len_):
        signal = []
        for i in range(0,len_):
            signal.append(0)
        return signal

    def exportHL7aECGTemplate(self, location, leadName):
        Lead = self.getLeadCopy(leadName)
        # convert from mV to uV
        leadY_final_uV = Lead.getAmplitudValues()
        for i in range(0,len(leadY_final_uV)):
            leadY_final_uV[i] = 1000 * leadY_final_uV[i]
        Lead.setAmplitudValues(leadY_final_uV,'uV')
        Lead.setAmplitudResolution(1000*Lead.getAmplitudResolution())

        # Divide the Amplitud array by the resolution (HL7 condition)
        leadY_final_uVDivByResolution = Lead.getAmplitudValues()
        for i in range(0,len(leadY_final_uVDivByResolution)):
            leadY_final_uVDivByResolution[i] = leadY_final_uVDivByResolution[i]/Lead.getAmplitudResolution()
        Lead.setAmplitudValues(leadY_final_uVDivByResolution, 'uV')


        template ="""<?xml version = "1.0" encoding = "UTF-8"?>
<!-- FDA Annotated ECG -->
<AnnotatedECG xmlns="urn:hl7-org:v3" xmlns:voc="urn:hl7-org:v3/voc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 /HL7/aECG/2003-12/schema/PORT_MT020001.xsd" type="Observation" classCode="OBS">
<id root=\""""+self.getId_root()+"""\" /><code code="93000" codeSystem="2.16.840.1.113883.6.12" codeSystemName="CPT-4" displayName="Electrocardiogram" />
<text></text>
<effectiveTime>
<low value=\""""+self.getGlobalEffectiveTimeLow()+"""\" inclusive=\""""+self.getGlobalEffectiveTimeLowIsInclusive()+"""\" />
<high value=\""""+self.getGlobalEffectiveTimeHigh()+"""\" inclusive=\""""+self.getGlobalEffectiveTimeHighIsInclusive()+"""\" />
</effectiveTime>
<confidentialityCode />
<componentOf>
<timepointEvent>
<code code=\""""+self.getTimepointCode()+"""\" codeSystem="1.3.6.1.4.1.21123.4" />
<performer>
<studyEventPerformer>
<id /><assignedPerson>
<name>
</name>
</assignedPerson>
</studyEventPerformer>
</performer>
<componentOf>
<subjectAssignment>
<subject>
<trialSubject>
<id root=\""""+self.getSubjectTrialId()+"""\" extension=\""""+self.getSubjectTrialExtension()+"""\" /><subjectDemographicPerson >
<name>
"""+self.getSubjectName()+"""</name>
<administrativeGenderCode code=\""""+self.getSubjectGender()+"""\" codeSystem="2.16.840.1.113883.5.1" codeSystemName="AdministrativeGender" displayName=\""""+self.getSubjectGender()+"""\" />
<birthTime value=\""""+self.getBirthTime()+"""\" />
<raceCode />
</subjectDemographicPerson>
</trialSubject>
</subject>
<componentOf>
<clinicalTrial>
<id root=\""""+self.getClinicalTrialId()+"""\" extension=\""""+self.getClinicalTrialExtension()+"""\" /><author>
<clinicalTrialSponsor>
<sponsorOrganization >
<id /><name >
</name>
</sponsorOrganization>
</clinicalTrialSponsor>
</author>
</clinicalTrial>
</componentOf>
</subjectAssignment>
</componentOf>
</timepointEvent>
</componentOf>
<definition>
<relativeTimepoint>
<code code=\""""+self.getRelativeTimepointCode()+"""\" />
<componentOf>
<pauseQuantity />
<protocolTimepointEvent>
<code code=\""""+self.getProtocolTimepointCode()+"""\" />
<component>
<referenceEvent>
<code />
</referenceEvent>
</component>
</protocolTimepointEvent>
</componentOf>
</relativeTimepoint>
</definition>
<location>
<testingSite>
<id />
<location >
<name></name>
</location>
</testingSite>
</location>
<component>
<series>
<id root=\""""+self.getSeriesID()+"""\" /><code code="RHYTHM" codeSystem="2.16.840.1.113883.5.4" codeSystemName="ActCode" displayName="ECG Rhythm Waveforms" />
<effectiveTime>
<low value=\""""+self.getGlobalEffectiveTimeLow()+"""\" inclusive=\""""+self.getGlobalEffectiveTimeLowIsInclusive()+"""\" />
<high value=\""""+self.getGlobalEffectiveTimeHigh()+"""\" inclusive=\""""+self.getGlobalEffectiveTimeHighIsInclusive()+"""\" />
</effectiveTime><author>
<seriesAuthor>
<manufacturedSeriesDevice >
<id /><code code="AMPS_12_LEAD_ELECTROCARDIOGRAPH" codeSystem="1.3.6.1.4.1.21123.3.2" displayName="12 Lead Electrocardiograph" />
<manufacturerModelName >
"""+self.getManufacturerModelName()+"""
</manufacturerModelName>
<softwareName >
</softwareName>
</manufacturedSeriesDevice>
<manufacturerOrganization >
<name>\""""+self.getManufacturerOrganizationName()+"""\"</name>
</manufacturerOrganization>
</seriesAuthor>
</author>
<secondaryPerformer>
<seriesPerformer>
<id /></seriesPerformer>
</secondaryPerformer>
<component>
<sequenceSet>
<component>
<sequence>
<code code="TIME_ABSOLUTE" codeSystem="2.16.840.1.113883.5.4" codeSystemName="ActCode" displayName="Absolute Time" />
<value xsi:type="GLIST_TS">
<head value="20031029151120.000" />
<increment value=\""""+str(Lead.getTimeResolution())+"""\" unit=\""""+Lead.getTimeUnit()+"""\" />
</value>
</sequence>
</component>
<component>
<sequence>
<code code="MDC_ECG_LEAD_"""+leadName+"""\" codeSystem="2.16.840.1.113883.6.24" codeSystemName="MDC" />
<value xsi:type="SLIST_PQ">
<origin value="0.000" unit=\""""+Lead.getAmplitudUnit()+"""\" />
<scale value=\""""+str(Lead.getAmplitudResolution())+"""\" unit=\""""+Lead.getAmplitudUnit()+"""\" />
<digits>"""+self.getStrSignal(Lead.getAmplitudValues())+"""</digits>
</value>
</sequence>
</component>
</sequenceSet>
</component>
</series>
</component>
</AnnotatedECG>"""
        f = open(location, 'w')
        f.write(template)
