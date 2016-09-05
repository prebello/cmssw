# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run2_mc --pileup_input das:/RelValMinBias_13/CMSSW_7_1_20_patch2-MCRUN2_71_V1_GsRealBS-v1/GEN-SIM -n 10 --era Run2_2016 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2016 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --pileup AVE_35_BX_25ns --io DIGIUP15_PU25.io --python DIGIUP15_PU25.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --no_exec --filein filelist:step1_dasquery.log --fileout file:step2.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_25ns10e33_v2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_1_20_patch2/RelValH125GGgluonfusion_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/40E15B63-C081-E511-8504-0025905A6090.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValH125GGgluonfusion_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/4AA307A9-C181-E511-90A2-0025905A6090.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValH125GGgluonfusion_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F40C1E60-C281-E511-A521-0025905A6090.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(10485760),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(35.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/02A753B5-AD81-E511-B976-002618943915.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/102620B1-AD81-E511-94EA-0026189438B0.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/28160373-B581-E511-A005-0025905A60D2.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/2A7CD5CA-AF81-E511-9736-00261894393B.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/34B23D7D-AF81-E511-A9CC-00261894396D.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/5EB6574D-B581-E511-9C97-0025905A60D2.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/A2049BB6-B281-E511-A0F9-0025905B8576.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F08E84FB-AB81-E511-8E87-002590596468.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F4C45783-B281-E511-AF12-002618943932.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F623580F-AC81-E511-B6E2-0026189438B0.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v2', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

