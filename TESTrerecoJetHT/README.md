The starting point to set up a re-reco cmsDriver is of course the cmsDriver used for data relvals + any needed special GT or customisation

When we start a new reprocessing campaign we also need to make local test for another reason: indeed we want to estimate parameters (time_event, size_event, size_memory) to be written in the master.conf file. The time_event parameter it is used by computing to make the job splitting. The size_memory parameter refers to RSS memory of the job, and it used by computing to assign to computing resources with enough memory. In this case, it is suggested to run on at least 100 events to get reliable estimates for these parameters
a monitoring utility has to be added into the cmsDriver
--customise Configuration/DataProcessing/Utils.addMonitoring 


"cmsDriver.py RECO -s RAW2DIGI,L1Reco,RECO,SKIM:JetHTJetPlusHOFilter,ALCA:HcalCalDijets+HcalCalIsoTrkFilter+HcalCalIsolatedBunchFilter,EI,PAT,DQM:@allForPrompt --runUnscheduled --nThreads 4 --data --era Run2_2016 --scenario pp --conditions 80X_dataRun2_2016LegacyRepro_v3 --eventcontent AOD,MINIAOD,DQM --datatier AOD,MINIAOD,DQMIO --customise Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016,Configuration/DataProcessing/Utils.addMonitoring --filein /store/data/Run2016H/JetHT/RAW/v1/000/281/010/00000/22FCEBCD-707E-E611-954B-FA163E0B3058.root -n 100 --python_filename=recoskim_Run2016H_JetHT.py --no_exec"

run the local test in this way:

"cmsRun -e -j recoskim_Run2016H_JetHT.xml recoskim_Run2016H_JetHT.py"

The output xml file will be used to find for instance PeakValueRss value for memory


Produce the cfg file for the harvesting step. This is needed if you have included the DQM step in the cmsDriver for re-reco

"cmsDriver.py step4 --data --filetype DQM --conditions 80X_dataRun2_2016LegacyRepro_v3 -s HARVESTING:@allForPrompt --scenario pp --filein file:RECO_RAW2DIGI_L1Reco_RECO_ALCA_EI_PAT_DQM_inDQM.root --python_filename=harvesting.py --no_exec"


Before injecting, it is important to printout the set of parameters associated to that workflow:

wmcontrol.py --test --req_file=master_Run2016H.conf


For the final injection:

wmcontrol.py --req_file=master_Run2016H.conf
