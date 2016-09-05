# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SMS-T1tttt_mGl-1500_mLSP-100_13TeV-pythia8_cfi --conditions auto:run2_mc --fast -n 10 --era Run2_2016 --eventcontent FEVTDEBUGHLT,DQM --relval 100000,1000 -s GEN,SIM,RECOBEFMIX,DIGI:pdigi_valid,L1,DIGI2RAW,L1Reco,RECO,EI,HLT:@relval2016,VALIDATION:@standardValidation,DQM:@standardDQM --datatier GEN-SIM-DIGI-RECO,DQMIO --beamspot Realistic50ns13TeVCollision --io SMS-T1tttt_mGl-1500_mLSP-100FS_13.io --python SMS-T1tttt_mGl-1500_mLSP-100FS_13.py --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --no_exec --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
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
    annotation = cms.untracked.string('SMS-T1tttt_mGl-1500_mLSP-100_13TeV-pythia8_cfi nevts:10'),
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
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v2', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters'),
        processParameters = cms.vstring('SUSY:all = off', 
            'SUSY:gg2gluinogluino = on', 
            'SUSY:qqbar2gluinogluino = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    SLHATableForPythia8 = cms.string('\nBlock MODSEL  # Model selection\n    1    0    # Generic MSSM\nBlock MINPAR  # Input parameters\n    3    1.00000000E+00  # tanb at m_Z   \n#\nBlock SMINPUTS  # SM parameters\n         1     1.27931277E+02  # alpha_em^-1(MZ)^MSbar\n         2     1.16639000E-05  # G_mu [GeV^-2]\n         3     1.17200000E-01  # alpha_s(MZ)^MSbar\n         4     9.11876000E+01  # m_Z(pole)\n         5     4.20000000E+00  # m_b(m_b), MSbar\n         6     1.74300000E+02  # m_t(pole)\n         7     1.77700000E+00  # m_tau(pole)\nBlock MASS  # Mass spectrum\n#   PDG code      mass          particle\n        24     8.04009772E+01  # W+\n        25     10.0E+4  # h0\n        35     10.0E+4  # H0\n        36     10.0E+4  # A0\n        37     10.0E+4  # H+\n   1000001     10.0E+4  # ~d_L\n   2000001     10.0E+4  # ~d_R\n   1000002     10.0E+4  # ~u_L\n   2000002     10.0E+4  # ~u_R\n   1000003     10.0E+4  # ~s_L\n   2000003     10.0E+4  # ~s_R\n   1000004     10.0E+4  # ~c_L\n   2000004     10.0E+4  # ~c_R\n   1000005     10.0E+4  # ~b_1\n   2000005     10.0E+4  # ~b_2\n   1000006     10.0E+4  # ~t_1 \n   2000006     10.0E+4  # ~t_2\n   1000011     10.0E+4  # ~e_L-\n   2000011     10.0E+4  # ~e_R-\n   1000012     10.0E+4  # ~nu_eL\n   1000013     10.0E+4  # ~mu_L-\n   2000013     10.0E+4  # ~mu_R-\n   1000014     10.0E+4  # ~nu_muL\n   1000015     10.0E+4  # ~tau_1-\n   2000015     10.0E+4  # ~tau_2-\n   1000016     10.0E+4  # ~nu_tauL\n   1000021     1.50E+3  # ~g \n   1000022     1.00E+2  # ~chi_10 \n   1000023     10.0E+4  # ~chi_20 \n   1000025     10.0E+4  # ~chi_30\n   1000035     10.0E+4  # ~chi_40\n   1000024     10.0E+4  # ~chi_1+ \n   1000037     10.0E+4  # ~chi_2+\n#\nBLOCK NMIX  # Neutralino Mixing Matrix\n  1  1     9.79183656E-01   # N_11\n  1  2    -8.70017948E-02   # N_12\n  1  3     1.75813037E-01   # N_13\n  1  4    -5.21520034E-02   # N_14\n  2  1     1.39174513E-01   # N_21\n  2  2     9.44472080E-01   # N_22\n  2  3    -2.71658234E-01   # N_23\n  2  4     1.21674770E-01   # N_24\n  3  1    -7.50233573E-02   # N_31\n  3  2     1.16844446E-01   # N_32\n  3  3     6.87186106E-01   # N_33\n  3  4     7.13087741E-01   # N_34\n  4  1    -1.27284400E-01   # N_41\n  4  2     2.94534470E-01   # N_42\n  4  3     6.50435881E-01   # N_43\n  4  4    -6.88462993E-01   # N_44\n#\nBLOCK UMIX  # Chargino Mixing Matrix U\n  1  1     9.15480281E-01   # U_11\n  1  2    -4.02362840E-01   # U_12\n  2  1     4.02362840E-01   # U_21\n  2  2     9.15480281E-01   # U_22\n#\nBLOCK VMIX  # Chargino Mixing Matrix V\n  1  1     9.82636204E-01   # V_11\n  1  2    -1.85542692E-01   # V_12\n  2  1     1.85542692E-01   # V_21\n  2  2     9.82636204E-01   # V_22\n#\nBLOCK STOPMIX  # Stop Mixing Matrix\n  1  1     1.0   # cos(theta_t)\n  1  2     0.0   # sin(theta_t)\n  2  1     0.0   # -sin(theta_t)\n  2  2     1.0   # cos(theta_t)\n#\nBLOCK SBOTMIX  # Sbottom Mixing Matrix\n  1  1     9.66726392E-01   # cos(theta_b)\n  1  2     2.55812594E-01   # sin(theta_b)\n  2  1    -2.55812594E-01   # -sin(theta_b)\n  2  2     9.66726392E-01   # cos(theta_b)\n#\nBLOCK STAUMIX  # Stau Mixing Matrix\n  1  1     4.51419848E-01   # cos(theta_tau)\n  1  2     8.92311672E-01   # sin(theta_tau)\n  2  1    -8.92311672E-01   # -sin(theta_tau)\n  2  2     4.51419848E-01   # cos(theta_tau)\n#\nBLOCK ALPHA  # Higgs mixing\n          -1.13676047E-01   # Mixing angle in the neutral Higgs boson sector\n#\nBLOCK HMIX Q=  2.90528802E+02  # DRbar Higgs Parameters\n         1     3.05599351E+02   # mu(Q)MSSM\n#\nBLOCK AU Q=  2.90528802E+02  # The trilinear couplings\n  1  1     0.00000000E+00   # A_u(Q) DRbar\n  2  2     0.00000000E+00   # A_c(Q) DRbar\n  3  3    -4.46245994E+02   # A_t(Q) DRbar\n#\nBLOCK AD Q=  2.90528802E+02  # The trilinear couplings\n  1  1     0.00000000E+00   # A_d(Q) DRbar\n  2  2     0.00000000E+00   # A_s(Q) DRbar\n  3  3    -8.28806503E+02   # A_b(Q) DRbar\n#\nBLOCK AE Q=  2.90528802E+02  # The trilinear couplings\n  1  1     0.00000000E+00   # A_e(Q) DRbar\n  2  2     0.00000000E+00   # A_mu(Q) DRbar\n  3  3    -4.92306701E+02   # A_tau(Q) DRbar\n#\nBLOCK MSOFT Q=  2.90528802E+02  # The soft SUSY breaking masses at the scale Q\n         1     6.39136864E+01   # M_1(Q)\n         2     1.22006983E+02   # M_2(Q)\n         3     3.90619532E+02   # M_3(Q)\n        21     4.42860395E+04   # mH1^2(Q)\n        22    -9.76585434E+04   # mH2^2(Q)\n        31     2.26648170E+02   # meL(Q)\n        32     2.26648170E+02   # mmuL(Q)\n        33     2.24355944E+02   # mtauL(Q)\n        34     2.08394096E+02   # meR(Q)\n        35     2.08394096E+02   # mmuR(Q)\n        36     2.03337218E+02   # mtauR(Q)\n        41     4.08594291E+02   # mqL1(Q)\n        42     4.08594291E+02   # mqL2(Q)\n        43     3.46134575E+02   # mqL3(Q)\n        44     3.98943379E+02   # muR(Q)\n        45     3.98943379E+02   # mcR(Q)\n        46     2.58021672E+02   # mtR(Q)\n        47     3.95211849E+02   # mdR(Q)\n        48     3.95211849E+02   # msR(Q)\n        49     3.90320031E+02   # mbR(Q)\n#\n#\n#\n#                             =================\n#                             |The decay table|\n#                             =================\n#\n# - The QCD corrections to the decays gluino -> squark  + quark\n#                                     squark -> gaugino + quark_prime\n#                                     squark -> squark_prime + Higgs\n#                                     squark -> gluino  + quark\n#   are included.\n#\n# - The multi-body decays for the inos, stops and sbottoms are included.\n#\n# - The loop induced decays for the gluino, neutralinos and stops\n#   are included.\n#\n# - The SUSY decays of the top quark are included.\n#\n#\n#\n#         PDG            Width\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000021     1.00000000E+00   # gluino decays\n#          BR         NDA      ID1       ID2\n     0.000000E+00    3     1000022       1       -1\n     0.000000E+00    3     1000022       2       -2\n     0.000000E+00    3     1000022       3       -3\n     0.000000E+00    3     1000022       4       -4\n     0.000000E+00    3     1000022       5       -5\n     1.000000E+00    3     1000022       6       -6\n#\n#         PDG            Width\nDECAY   1000006     0.00000000E+00   # stop1 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\n#\n#         PDG            Width\nDECAY   1000002     1.00000000E+00   # sup_L decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         2   # BR(~u_L -> ~chi_10 u)\n#\n#         PDG            Width\nDECAY   2000002     1.00000000E+00   # sup_R decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         2   # BR(~u_R -> ~chi_10 u)\n#\n#         PDG            Width\nDECAY   1000001     1.00000000E+00   # sdown_L decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         1   # BR(~d_L -> ~chi_10 d)\n#\n#         PDG            Width\nDECAY   2000001     1.00000000E+00   # sdown_R decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         1   # BR(~d_R -> ~chi_10 d)\n#\n#         PDG            Width\nDECAY   1000004     1.00000000E+00   # scharm_L decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         4   # BR(~c_L -> ~chi_10 c)\n#\n#         PDG            Width\nDECAY   2000004     1.00000000E+00   # scharm_R decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         4   # BR(~c_R -> ~chi_10 c)\n#\n#         PDG            Width\nDECAY   1000003     1.00000000E+00   # sstrange_L decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         3   # BR(~s_L -> ~chi_10 s)\n#\n#         PDG            Width\nDECAY   2000003     1.00000000E+00   # sstrange_R decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2     1000022         3   # BR(~s_R -> ~chi_10 s)\n#\n#         PDG            Width\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000015     0.00000000E+00   # stau_1 decays\nDECAY   2000015     0.00000000E+00   # stau_2 decays\n#\n#         PDG            Width\nDECAY   1000012     0.00000000E+00   # snu_elL decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\n#         PDG            Width\nDECAY   1000024     2.02592183E-05   # chargino1+ decays\n#           BR         NDA      ID1       ID2       ID3\n     0.33333333E+00    3     1000022       -11        12   # BR(~chi_1+ -> ~chi_10 e+   nu_e)\n     0.33333333E+00    3     1000022       -13        14   # BR(~chi_1+ -> ~chi_10 mu+  nu_mu)\n     0.33333333E+00    3     1000022       -15        16   # BR(~chi_1+ -> ~chi_10 tau+ nu_tau)\n#         PDG            Width\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\n'),
    comEnergy = cms.double(13000),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
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

