# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run2_mc -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2016 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG -n 10 --era Run2_2016 --eventcontent FEVTDEBUGHLT --io DIGIUP15.io --python DIGIUP15.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --no_exec --filein filelist:step1_dasquery.log --fileout file:step2.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
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
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/00595450-D081-E511-AD0D-002618943949.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/028A0A83-CD81-E511-93CB-0025905B85AE.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/10E766AC-D281-E511-A66E-002618943922.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/249171D5-D181-E511-84CD-0026189438DD.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/2A1616F6-D681-E511-A221-0025905A60BE.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/2E3E0956-D081-E511-BDF5-002618943984.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/42CCA281-CD81-E511-8032-0025905A6118.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/4C3AAD80-CE81-E511-A62B-00261894387E.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/5001FD7B-9E82-E511-AC2C-0025905B8572.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/5C2F8BD1-D181-E511-AFE1-002618FDA28E.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/806AF46A-CF81-E511-BFE6-0025905B8610.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/96E2FDBE-CF81-E511-B827-002618943949.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/9EE5DC57-D481-E511-B11C-00261894397B.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/ACF6EEF7-D081-E511-8F8B-0026189438EB.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/E8513DFE-D081-E511-89B8-0026189438BF.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/EA83F7CB-D381-E511-ABC9-002618943950.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F297A2CE-D281-E511-8B65-00261894380D.root', 
        '/store/relval/CMSSW_7_1_20_patch2/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F604A780-CE81-E511-97B3-00261894387E.root'),
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

