# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --conditions auto:run2_mc --pileup_input das:/RelValMinBias_13/CMSSW_7_1_20_patch2-MCRUN2_71_V1_GsRealBS-v1/GEN-SIM -n 10 --era Run2_2016 --eventcontent PREMIX --relval 100000,100 -s GEN,SIM,DIGIPREMIX:pdigi_valid,L1,DIGI2RAW --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --evt_type SingleNuE10_cfi --io PREMIXUP15_PU25.io --python PREMIXUP15_PU25.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --no_exec --fileout file:step1.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('DIGI2RAW',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_PreMix_cff')
process.load('SimGeneral.MixingModule.digi_noNoise_cfi')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
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
    annotation = cms.untracked.string('SingleNuE10_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = process.PREMIXEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(35.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/02A753B5-AD81-E511-B976-002618943915.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/102620B1-AD81-E511-94EA-0026189438B0.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/28160373-B581-E511-A005-0025905A60D2.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/2A7CD5CA-AF81-E511-9736-00261894393B.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/34B23D7D-AF81-E511-A9CC-00261894396D.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/5EB6574D-B581-E511-9C97-0025905A60D2.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/A2049BB6-B281-E511-A0F9-0025905B8576.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F08E84FB-AB81-E511-8E87-002590596468.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F4C45783-B281-E511-AF12-002618943932.root', '/store/relval/CMSSW_7_1_20_patch2/RelValMinBias_13/GEN-SIM/MCRUN2_71_V1_GsRealBS-v1/00000/F623580F-AC81-E511-B6E2-0026189438B0.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersNoNoiseValid)
process.esDigiToRaw.Label = cms.string('mix')
process.SiStripDigiToRaw.FedReadoutMode = cms.string('PREMIX_RAW')
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
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXoutput_step = cms.EndPath(process.PREMIXoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.PREMIXoutput_step)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


