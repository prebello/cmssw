# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --datatier AODSIM -n 10 --era Run2_2016 --conditions auto:run2_mc -s L1REPACK:FullMC,HLT:@relval2016,RAW2DIGI:L1TRawToDigi --process HLT2 --eventcontent AODSIM --customise_commands process.AODSIMoutput.outputCommands.append('drop L1GlobalTriggerReadoutRecord_gtDigis_*_HLT2') --inputCommands keep *,drop *_TriggerResults_*_HLT,drop *_hltTriggerSummaryAOD_*_HLT,drop *_hltGtStage2ObjectMap_*_HLT,drop *_l1extraParticles_*_RECO,drop L1GlobalTriggerReadoutRecord_gtDigis_*_RECO,drop *_cscSegments_*_RECO,drop *_dt4DSegments_*_RECO,drop *_rpcRecHits_*_RECO --io REHLTUP15_reHLT.io --python REHLTUP15_reHLT.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --no_exec --filein file:step3.root --fileout file:step4.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT2',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorRepack_FullMC_cff')
process.load('HLTrigger.Configuration.HLT_25ns10e33_v2_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:step3.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_TriggerResults_*_HLT', 
        'drop *_hltTriggerSummaryAOD_*_HLT', 
        'drop *_hltGtStage2ObjectMap_*_HLT', 
        'drop *_l1extraParticles_*_RECO', 
        'drop L1GlobalTriggerReadoutRecord_gtDigis_*_RECO', 
        'drop *_cscSegments_*_RECO', 
        'drop *_dt4DSegments_*_RECO', 
        'drop *_rpcRecHits_*_RECO'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:step4.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v2', '')

# Path and EndPath definitions
process.L1RePack_step = cms.Path(process.SimL1Emulator)
process.raw2digi_step = cms.Path(process.L1TRawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.L1RePack_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.endjob_step,process.AODSIMoutput_step])

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

# Customisation from command line
process.AODSIMoutput.outputCommands.append('drop L1GlobalTriggerReadoutRecord_gtDigis_*_HLT2')

# Customisation from command line
process.AODSIMoutput.outputCommands.append('drop L1GlobalTriggerReadoutRecord_gtDigis_*_HLT2')