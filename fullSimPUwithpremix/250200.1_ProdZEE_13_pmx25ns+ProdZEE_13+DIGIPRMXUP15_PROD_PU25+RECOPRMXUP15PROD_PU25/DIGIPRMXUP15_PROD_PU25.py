# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --datamix PreMix --conditions auto:run2_mc --pileup_input das:/RelValPREMIXUP15_PU25/CMSSW_8_0_19-PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/GEN-SIM-DIGI-RAW -s DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@relval2016 --datatier PREMIXRAW --era Run2_2016 --eventcontent PREMIXRAW --io DIGIPRMXUP15_PROD_PU25.io --python DIGIPRMXUP15_PROD_PU25.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 -n 100 --no_exec --filein file:step1.root --fileout file:step2.root --nThreads 4
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
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_25ns10e33_v2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('PREMIXRAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/00185563-0673-E611-A242-0025905A607E.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/005ED5F9-FE72-E611-AB76-0CC47A7C35A8.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/007F3291-0273-E611-8000-0CC47A78A2EC.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/0207D55B-0673-E611-9486-0CC47A7C3450.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/0226853D-0573-E611-95C6-0CC47A7C34E6.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/023A7B96-0173-E611-8EF0-0CC47A7C345C.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/02441FF3-0073-E611-A071-0CC47A7C347E.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/02BD61DA-0373-E611-9598-0CC47A7C361E.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/0411FD92-0473-E611-965E-0CC47A7C3572.root', '/store/relval/CMSSW_8_0_19/RelValPREMIXUP15_PU25/GEN-SIM-DIGI-RAW/PU25ns_80X_mcRun2_asymptotic_2016_TrancheIV_v2_Tr4GT_v2-v1/00000/046402FA-FE72-E611-A63E-0CC47A78A2F6.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v2', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step])

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

