# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step5 --conditions auto:run2_mc --filein file:step3.root -s ALCA:TkAlMuonIsolated+TkAlMinBias+MuAlOverlaps+EcalESAlign+EcalTrg --datatier ALCARECO -n 1000 --era Run2_2016 --eventcontent ALCARECO --io ALCATTUP15.io --python ALCATTUP15.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --no_exec --fileout file:step5.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('ALCA',eras.Run2_2016)

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
    input = cms.untracked.int32(1000)
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
    annotation = cms.untracked.string('step5 nevts:1000'),
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
process.ALCARECOStreamEcalTrg = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalTrg')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('EcalTrg')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('EcalTrg.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep CaloTowersSorted_towerMaker_*_*', 
        'keep EBDigiCollection_ecalDigis_ebDigis_*', 
        'keep EEDigiCollection_ecalDigis_eeDigis_*', 
        'keep ESDCCHeaderBlocksSorted_ecalPreshowerDigis_*_*', 
        'keep ESDigiCollection_ecalPreshowerDigis_*_*', 
        'keep ESKCHIPBlocksSorted_ecalPreshowerDigis_*_*', 
        'keep EcalRecHitsSorted_ecalPreshowerRecHit_EcalRecHitsES_*', 
        'keep EcalRecHitsSorted_ecalRecHit_EcalRecHitsEB_*', 
        'keep EcalRecHitsSorted_ecalRecHit_EcalRecHitsEE_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep EcalTriggerPrimitiveDigisSorted_ecalDigis_EcalTriggerPrimitives_*', 
        'keep EcalUncalibratedRecHitsSorted_ecalMultiFitUncalibRecHit_EcalUncalibRecHitsEB_*', 
        'keep EcalUncalibratedRecHitsSorted_ecalMultiFitUncalibRecHit_EcalUncalibRecHitsEE_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep L1MuGMTCands_gtDigis_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1MuRegionalCands_gtDigis_CSC_*', 
        'keep L1MuRegionalCands_gtDigis_DT_*', 
        'keep L1MuRegionalCands_gtDigis_RPCb_*', 
        'keep L1MuRegionalCands_gtDigis_RPCf_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep TrajectorysToOnerecoGsfTracksAssociation_electronGsfTracks_*_*', 
        'keep edmTriggerResults_TriggerResults_*_*', 
        'keep floatedmValueMap_offlinePrimaryVerticesWithBS_*_*', 
        'keep floats_generalTracks_MVAValues_*', 
        'keep intedmValueMap_offlinePrimaryVerticesWithBS_*_*', 
        'keep recoBeamSpot_offlineBeamSpot_*_*', 
        'keep recoCaloClusters_cleanedHybridSuperClusters_hybridBarrelBasicClusters_*', 
        'keep recoCaloClusters_hfEMClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_hybridBarrelBasicClusters_*', 
        'keep recoCaloClusters_hybridSuperClusters_uncleanOnlyHybridBarrelBasicClusters_*', 
        'keep recoCaloClusters_multi5x5BasicClustersCleaned_multi5x5BarrelBasicClusters_*', 
        'keep recoCaloClusters_multi5x5BasicClustersCleaned_multi5x5EndcapBasicClusters_*', 
        'keep recoCaloClusters_multi5x5BasicClustersUncleaned_multi5x5BarrelBasicClusters_*', 
        'keep recoCaloClusters_multi5x5BasicClustersUncleaned_multi5x5EndcapBasicClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_uncleanOnlyMulti5x5EndcapBasicClusters_*', 
        'keep recoCaloClusters_particleFlowEGamma_EBEEClusters_*', 
        'keep recoCaloClusters_particleFlowEGamma_ESClusters_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_particleFlowBasicClusterECALBarrel_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_particleFlowBasicClusterECALEndcap_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_particleFlowBasicClusterECALPreshower_*', 
        'keep recoCaloClusters_uncleanedHybridSuperClusters_hybridBarrelBasicClusters_*', 
        'keep recoElectronSeeds_electronMergedSeeds_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoSuperClusters_cleanedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_hfEMClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoSuperClusters_multi5x5SuperClustersCleaned_multi5x5BarrelSuperClusters_*', 
        'keep recoSuperClusters_multi5x5SuperClustersCleaned_multi5x5EndcapSuperClusters_*', 
        'keep recoSuperClusters_multi5x5SuperClustersUncleaned_multi5x5BarrelSuperClusters_*', 
        'keep recoSuperClusters_multi5x5SuperClustersUncleaned_multi5x5EndcapSuperClusters_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_multi5x5EndcapSuperClusters_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_uncleanOnlyMulti5x5EndcapSuperClusters_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_particleFlowSuperClusterECALBarrel_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_particleFlowSuperClusterECALEndcapWithPreshower_*', 
        'keep recoSuperClusters_uncleanedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_uncleanedOnlyCorrectedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_uncleanedOnlyMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoVertexs_offlinePrimaryVerticesWithBS_*_*', 
        'keep recoVertexsedmAssociation_offlinePrimaryVerticesWithBS_*_*', 
        'keep uchars_generalTracks_QualityMasks_*')
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
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
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

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOEcalESAlign_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOEcalTrg_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOMuAlOverlaps_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMuonIsolated_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v2', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamEcalESAlignOutPath = cms.EndPath(process.ALCARECOStreamEcalESAlign)
process.ALCARECOStreamEcalTrgOutPath = cms.EndPath(process.ALCARECOStreamEcalTrg)
process.ALCARECOStreamMuAlOverlapsOutPath = cms.EndPath(process.ALCARECOStreamMuAlOverlaps)
process.ALCARECOStreamTkAlMinBiasOutPath = cms.EndPath(process.ALCARECOStreamTkAlMinBias)
process.ALCARECOStreamTkAlMuonIsolatedOutPath = cms.EndPath(process.ALCARECOStreamTkAlMuonIsolated)

# Schedule definition
process.schedule = cms.Schedule(process.pathALCARECOEcalESAlign,process.pathALCARECOEcalTrg,process.pathALCARECOTkAlMinBias,process.pathALCARECOMuAlOverlaps,process.pathALCARECOTkAlMuonIsolated,process.endjob_step,process.ALCARECOStreamEcalESAlignOutPath,process.ALCARECOStreamEcalTrgOutPath,process.ALCARECOStreamMuAlOverlapsOutPath,process.ALCARECOStreamTkAlMinBiasOutPath,process.ALCARECOStreamTkAlMuonIsolatedOutPath)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)


