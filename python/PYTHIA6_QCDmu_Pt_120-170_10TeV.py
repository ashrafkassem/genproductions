import FWCore.ParameterSet.Config as cms

from Configuration.GenProduction.PythiaUESettings_cfi import *
source = cms.Source("PythiaSource",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.044),
    comEnergy = cms.untracked.double(10000.0),
    crossSection = cms.untracked.double(249300.),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1         ! QCD',
                                        'CKIN(3)=120     ! pthat min.',
                                        'CKIN(4)=170     ! pthat max.',
                                        'PARJ(71)=20000.  ! max. proper lifetime time ctau in mm',
                                        'MDCY(C130,1)=1   ! decay k0-longs',
                                        'MDCY(C211,1)=1   ! decay pions',
                                        'MDCY(C321,1)=1   ! decay kaons'),
 
       
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


mugenfilter = cms.EDFilter("MCSmartSingleParticleFilter",
                           MinPt = cms.untracked.vdouble(5.,5.),
                           MinEta = cms.untracked.vdouble(-2.5,-2.5),
                           MaxEta = cms.untracked.vdouble(2.5,2.5),
                           ParticleID = cms.untracked.vint32(13,-13),
                           Status = cms.untracked.vint32(1,1),
                           # Decay cuts are in mm
                           MaxDecayRadius = cms.untracked.vdouble(1500.,1500.),
                           MinDecayZ = cms.untracked.vdouble(-3000.,-3000.),
                           MaxDecayZ = cms.untracked.vdouble(3000.,3000.)
)


configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.5 $'),
    annotation = cms.untracked.string('PYTHIA6-QCD->mu pthat=120-170 at 10TeV with Muon preselection (pt > 5 |eta| < 2.5)')
)

ProductionFilterSequence = cms.Sequence(mugenfilter)

