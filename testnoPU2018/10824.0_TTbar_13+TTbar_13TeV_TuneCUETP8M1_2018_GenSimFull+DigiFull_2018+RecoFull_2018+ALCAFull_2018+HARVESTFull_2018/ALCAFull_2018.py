# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --conditions auto:phase1_2018_realistic -s ALCA:TkAlMuonIsolated+TkAlMinBias+MuAlOverlaps+EcalESAlign+TkAlZMuMu --datatier ALCARECO -n 10 --geometry DB:Extended --era Run2_2018 --eventcontent ALCARECO --io ALCAFull_2018.io --python ALCAFull_2018.py --no_exec --filein file:step3.root --fileout file:step4.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('ALCA',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step3.root'),
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


# Additional output definition
process.ALCARECOStreamEcalESAlign = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalESAlign')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('EcalESAlign')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('EcalESAlign.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep ESDCCHeaderBlocksSorted_ecalPreshowerDigis_*_*', 
        'keep ESDigiCollection_ecalPreshowerDigis_*_*', 
        'keep ESKCHIPBlocksSorted_ecalPreshowerDigis_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_ecalAlCaESAlignTrackReducer_*_*', 
        'keep SiStripClusteredmNewDetSetVector_ecalAlCaESAlignTrackReducer_*_*', 
        'keep TrackingRecHitsOwned_ecalAlCaESAlignTrackReducer_*_*', 
        'keep recoTrackExtras_ecalAlCaESAlignTrackReducer_*_*', 
        'keep recoTracks_ecalAlCaESAlignTrackReducer_*_*', 
        'keep recoBeamSpot_offlineBeamSpot_*_*')
)
process.ALCARECOStreamMuAlOverlaps = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlOverlaps')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('MuAlOverlaps')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('MuAlOverlaps.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOMuAlOverlaps_*_*', 
        'keep *_ALCARECOMuAlOverlapsGeneralTracks_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_muonDTDigis_*_*', 
        'keep *_muonRPCDigis_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt2DSegments_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)
process.ALCARECOStreamTkAlMinBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBias')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlMinBias')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlMinBias.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMinBias_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*', 
        'keep *_offlineBeamSpot_*_*')
)
process.ALCARECOStreamTkAlMuonIsolated = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolated')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlMuonIsolated')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlMuonIsolated.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMuonIsolated_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)
process.ALCARECOStreamTkAlZMuMu = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMu')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlZMuMu')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlZMuMu.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlZMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*')
)

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOEcalESAlign_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlZMuMu_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOMuAlOverlaps_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMuonIsolated_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamEcalESAlignOutPath = cms.EndPath(process.ALCARECOStreamEcalESAlign)
process.ALCARECOStreamMuAlOverlapsOutPath = cms.EndPath(process.ALCARECOStreamMuAlOverlaps)
process.ALCARECOStreamTkAlMinBiasOutPath = cms.EndPath(process.ALCARECOStreamTkAlMinBias)
process.ALCARECOStreamTkAlMuonIsolatedOutPath = cms.EndPath(process.ALCARECOStreamTkAlMuonIsolated)
process.ALCARECOStreamTkAlZMuMuOutPath = cms.EndPath(process.ALCARECOStreamTkAlZMuMu)

# Schedule definition
process.schedule = cms.Schedule(process.pathALCARECOEcalESAlign,process.pathALCARECOTkAlZMuMu,process.pathALCARECOTkAlMinBias,process.pathALCARECOMuAlOverlaps,process.pathALCARECOMuAlOverlapsGeneralTracks,process.pathALCARECOTkAlMuonIsolated,process.endjob_step,process.ALCARECOStreamEcalESAlignOutPath,process.ALCARECOStreamMuAlOverlapsOutPath,process.ALCARECOStreamTkAlMinBiasOutPath,process.ALCARECOStreamTkAlMuonIsolatedOutPath,process.ALCARECOStreamTkAlZMuMuOutPath)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
