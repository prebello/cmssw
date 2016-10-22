# import the definition of the steps and input files:
from  Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = Matrix()

# each workflow defines a name and a list of steps to be done. 
 
# if no explicit name/label given for the workflow (first arg),
# the name of step1 will be used

# 50 ns at 8 TeV
workflows[200]=['',['ZEE','DIGIPU1','RECOPU1','HARVEST']]
#workflows[201]=['',['ZmumuJets_Pt_20_300','DIGIPU2','RECOPU2','HARVEST']]
workflows[202]=['',['TTbar','DIGIPU1','RECOPU1','HARVEST']]
workflows[203]=['',['H130GGgluonfusion','DIGIPU1','RECOPU1','HARVEST']]
workflows[204]=['',['QQH1352T','DIGIPU1','RECOPU1','HARVEST']]
workflows[205]=['',['ZTT','DIGIPU1','RECOPU1','HARVEST']]

#heavy ions tests
workflows[300]=['Pyquen_GammaJet_pt20_2760GeV',['Pyquen_GammaJet_pt20_2760GeV','DIGIHIMIX','RECOHIMIX','HARVESTHI']]
workflows[301]=['Pyquen_DiJet_pt80to120_2760GeV',['Pyquen_DiJet_pt80to120_2760GeV','DIGIHIMIX','RECOHIMIX','HARVESTHI']]
workflows[302]=['Pyquen_ZeemumuJets_pt10_2760GeV',['Pyquen_ZeemumuJets_pt10_2760GeV','DIGIHIMIX','RECOHIMIX','HARVESTHI']]

# 50 ns at 13 TeV and POSTLS1
workflows[50200]=['',['ZEE_13','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]
workflows[50202]=['',['TTbar_13','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]
workflows[50203]=['',['H125GGgluonfusion_13','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]
workflows[50204]=['',['QQH1352T_13','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]
workflows[50205]=['',['ZTT_13','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]
workflows[50206]=['',['ZMM_13','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]
workflows[50207]=['',['NuGun_UP15','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]
workflows[50208]=['',['SMS-T1tttt_mGl-1500_mLSP-100_13','DIGIUP15_PU50','RECOUP15_PU50','HARVESTUP15_PU50']]

# 25 ns at 13 TeV and POSTLS1
workflows[25200]=['',['ZEE_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25202]=['',['TTbar_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25203]=['',['H125GGgluonfusion_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25204]=['',['QQH1352T_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25205]=['',['ZTT_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25206]=['',['ZMM_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25207]=['',['NuGun_UP15','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25208]=['',['SMS-T1tttt_mGl-1500_mLSP-100_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25209]=['',['QCD_FlatPt_15_3000HS_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]

# LHE-based fullSim PU  workflows
workflows[25210]=['',['TTbar012Jets_NLO_Mad_py8_Evt_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25211]=['',['GluGluHToZZTo4L_M125_Pow_py8_Evt_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25212]=['',['VBFHToZZTo4Nu_M125_Pow_py8_Evt_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25213]=['',['VBFHToBB_M125_Pow_py8_Evt_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]

workflows[25214]=['',['TTbarLepton_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]

# more 25 ns at 13 TeV and POSTLS1 requested by Mia Tosi

workflows[25215]=['',['ZpEE_2250_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25216]=['',['ZpMM_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]
workflows[25217]=['',['ZpTT_1500_13','DIGIUP15_PU25','RECOUP15_PU25','HARVESTUP15_PU25']]

# fullSim PU version of test customized reHLT workflow
# DIGIUP15_reHLT: as DIGIUP15 but: DIGI without pdigi_valid, no L1 step, no HLT step, and store only RAWSIM instead of FEVTDEBUGHLT, and datatier GEN-SIM-RAW instead of GEN-SIM-DIGI-RAW-HLTDEBUG
# RECOUP15_reHLT: as RECOUP15 but: no L1Reco, no PAT, no VALIDATION/DQM, and store only RAWAODSIM instead of RECOSIM,MINIAODSIM,DQM, and datatier GEN-SIM-DIGI-RAW instead of GEN-SIM-RECO,MINIAODSIM,DQMIO
# REHLTUP15_reHLT: do only L1REPACK and HLT ==> the McM reHLT campaign setup, output AODSIM eventcontent and AODSIM datatier
# MINIAODUP15_reHLT: do only PAT step + DQM/VALIDATION ==> the McM miniAOD campaign setup (except DQMs), write MINIAODSIM,DQMIO datatier and MINIAODSIM,DQM event content.
# HARVESTMINIAODUP15_reHLT: HARVEST step for DQMs from last MINIAODUP15_reHLT step.
#workflows[8025206] = ['', ['ZMM_13_reHLT','DIGIUP15_PU25_reHLT','RECOUP15_PU25_reHLT','REHLTUP15_PU25_reHLT', 'MINIAODUP15_PU25_reHLT', 'HARVESTMINIAODUP15_PU25_reHLT']]

# reHLT normal fullSim PU workflows
workflows[80025200]=['',['ZEE_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025202]=['',['TTbar_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025203]=['',['H125GGgluonfusion_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025204]=['',['QQH1352T_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025205]=['',['ZTT_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025206]=['',['ZMM_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025207]=['',['NuGun_UP15','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025208]=['',['SMS-T1tttt_mGl-1500_mLSP-100_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025214]=['',['TTbarLepton_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]

# reHLT workflows of the LHE-based fullSim PU workflows above
workflows[80025210]=['',['TTbar012Jets_NLO_Mad_py8_Evt_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025211]=['',['GluGluHToZZTo4L_M125_Pow_py8_Evt_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025212]=['',['VBFHToZZTo4Nu_M125_Pow_py8_Evt_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]
workflows[80025213]=['',['VBFHToBB_M125_Pow_py8_Evt_13','REHLTUP15_reHLT','MINIAODUP15_reHLT','HARVESTMINIAODUP15_reHLT']]


#fastsim
workflows[25400] = ['ZEE_13',["FS_ZEE_13_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[25402] = ['TTbar_13',["FS_TTbar_13_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[25403] = ['H125GGgluonfusion_13',["FS_H125GGgluonfusion_13_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
#workflow[25404]
workflows[25405] = ['ZTT_13',["FS_ZTT_13_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[25406] = ['ZMM_13',["FS_ZMM_13_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[25407] = ['NuGen_UP15',["FS_NuGun_UP15_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[25408] = ['SMS-T1tttt_mGl-1500_mLSP-100_13',["FS_SMS-T1tttt_mGl-1500_mLSP-100_13_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]]
workflows[25409] = ['QCD_FlatPt_15_3000HS_13',["FS_QCD_FlatPt_15_3000HS_13_UP15_PU25","HARVESTUP15FS","MINIAODMCUP15FS"]] 

