#
# eval `scramv1 runtime -csh`
# # set CRAB environment
# source  /afs/cern.ch/cms/ccs/wm/scripts/Crab/crab.sh
# voms-proxy-init

from prepare_conf import prepare


prepare(era = "Run2016B-v1", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
prepare(era = "Run2016B-v2", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
prepare(era = "Run2016C", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
prepare(era = "Run2016D", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
prepare(era = "Run2016E", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
prepare(era = "Run2016F", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
prepare(era = "Run2016G", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
prepare(era = "Run2016H", proc_string = "28Jul2017", GT = "80X_dataRun2_2016LegacyRepro_v3")
