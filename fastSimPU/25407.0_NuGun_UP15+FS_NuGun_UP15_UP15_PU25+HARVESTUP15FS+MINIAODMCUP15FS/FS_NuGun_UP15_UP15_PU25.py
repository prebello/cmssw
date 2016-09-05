# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SingleNuE10_cfi.py --conditions auto:run2_mc --pileup_input das:/RelValMinBiasFS_13_ForMixing/CMSSW_8_0_19-80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2_FastSim-v1/GEN-SIM-RECO --fast -n 10 --era Run2_2016 --eventcontent FEVTDEBUGHLT,DQM --relval 100000,500 -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO,EI,HLT:@relval2016,VALIDATION:@standardValidation,DQM:@standardDQM --beamspot Realistic50ns13TeVCollision --datatier GEN-SIM-DIGI-RECO,DQMIO --pileup AVE_35_BX_25ns --io FS_NuGun_UP15_UP15_PU25.io --python FS_NuGun_UP15_UP15_PU25.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --no_exec --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('FastSimulation.Configuration.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('HLTrigger.Configuration.HLT_25ns10e33_v2_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('FastSimulation.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleNuE10_cfi.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(10485760),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step1_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(35.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_8_0_19/RelValMinBiasFS_13_ForMixing/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2_FastSim-v1/00000/24E759BD-FF72-E611-89F6-0025905A497A.root', '/store/relval/CMSSW_8_0_19/RelValMinBiasFS_13_ForMixing/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2_FastSim-v1/00000/326610E5-0273-E611-8055-0025905A60D6.root', '/store/relval/CMSSW_8_0_19/RelValMinBiasFS_13_ForMixing/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2_FastSim-v1/00000/88925CE4-0273-E611-A6F2-0CC47A7C35F4.root', '/store/relval/CMSSW_8_0_19/RelValMinBiasFS_13_ForMixing/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2_FastSim-v1/00000/E6D36FB7-FF72-E611-BB11-0CC47A7C34A6.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v2', '')

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MaxE = cms.double(10.01),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinE = cms.double(9.99),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        PartID = cms.vint32(12)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single Nu E 10')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.prevalidation_step = cms.Path(process.prevalidation)
process.dqmoffline_step = cms.Path(process.DQMOffline)
process.dqmofflineOnPAT_step = cms.Path(process.PostDQMOffline)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.validation_step = cms.EndPath(process.genstepfilter+process.validation)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.L1Reco_step,process.reconstruction_step,process.eventinterpretaion_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.FEVTDEBUGHLToutput_step,process.DQMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFastSim 

#call to customisation function customizeHLTforFastSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFastSim(process)

# End of customisation functions

