# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:phase1_2017_realistic -s DIGI,L1,DIGI2RAW --datatier GEN-SIM-RAW -n 10 --geometry DB:Extended --era Run2_2017 --eventcontent RAWSIM --io DIGIUP17PRODUL.io --python DIGIUP17PRODUL.py --no_exec --filein filelist:step1_dasquery.log --fileout file:step2.root --nThreads 8
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('DIGI2RAW',eras.Run2_2017)

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
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_10_5_0_pre1/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/224DA2A6-BA5A-FE44-8888-9608E3C3491F.root', 
        '/store/relval/CMSSW_10_5_0_pre1/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/22947840-2543-6A4A-B2BD-B9155495D0B3.root', 
        '/store/relval/CMSSW_10_5_0_pre1/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/2C3F1D6A-E892-1D44-9A70-E4E0E609694B.root', 
        '/store/relval/CMSSW_10_5_0_pre1/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/3342EB73-02EB-6346-B81B-3A7635DE89C2.root', 
        '/store/relval/CMSSW_10_5_0_pre1/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/53101FB7-F71D-2D46-BF45-FE15E6D0E5E2.root', 
        '/store/relval/CMSSW_10_5_0_pre1/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/ABFA3921-52E7-134C-87B6-D58052402997.root', 
        '/store/relval/CMSSW_10_5_0_pre1/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/ACB3CEC8-09F0-174B-AD93-84BA32EED0C5.root'
    ),
    inputCommands = cms.untracked.vstring(
        'keep *', 
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
        'drop *_genMetIC5GenJs_*_*'
    ),
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

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
