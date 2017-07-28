#
# eval `scramv1 runtime -csh`
# # set CRAB environment
# source  /afs/cern.ch/cms/ccs/wm/scripts/Crab/crab.sh
# voms-proxy-init

import os
import  sys,time,json
from    dbs.apis.dbsClient import DbsApi
from    time import gmtime
import commands
url="https://cmsweb.cern.ch/dbs/prod/global/DBSReader"
api=DbsApi(url=url)

#from Configuration.Skimming.autoSkim import autoSkim
from autoSkim import autoSkim

#print autoSkim

from Configuration.AlCa.autoAlca import AlCaRecoMatrixRereco
# USING LOCAL autoAlca.py
#from autoAlca import autoAlca

#print autoAlca

#========================================================
# TOP level configuration goes here
# NOTE: you need to edit the cmsDriver commands below directly in the code

#
# acquisition_era = "Run2016D"
#
# GT = "80X_dataRun2_2016SeptRepro_v3"
# proc_string = "23Sep2016"
#



def prepare(era, proc_string, GT):

    acquisition_era = era
    if("Run2016B" in era):
        acquisition_era = "Run2016B"

    customera = {}
    customera["Run2016B"] = 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016,RecoTracker/Configuration/customizeMinPtForHitRecoveryInGluedDet.customizeHitRecoveryInGluedDetTkSeedsOnly'
    customera["Run2016C"] = 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016,RecoTracker/Configuration/customizeMinPtForHitRecoveryInGluedDet.customizeHitRecoveryInGluedDetTkSeedsOnly'
    customera["Run2016D"] = 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016,RecoTracker/Configuration/customizeMinPtForHitRecoveryInGluedDet.customizeHitRecoveryInGluedDetTkSeedsOnly'
    customera["Run2016E"] = 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016,RecoTracker/Configuration/customizeMinPtForHitRecoveryInGluedDet.customizeHitRecoveryInGluedDetTkSeedsOnly'
    customera["Run2016F"] = 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016,RecoTracker/Configuration/customizeMinPtForHitRecoveryInGluedDet.customizeHitRecoveryInGluedDetTkSeedsOnly'
    customera["Run2016G"] = 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016'
    customera["Run2016H"] = 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016'


    jsonFile = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt'

    default_priority = 85000

    pd_blacklist = ["HighMultiplicity",
#                    "NoBPTX",
                    "L1MinimumBias",
                    "HLTPhysics", #FIXME should be?
                    "HLTPhysics0",
                    "HLTPhysics1",
                    "HLTPhysics2",
                    "HLTPhysics3",
                    "HcalNZS",
                    "HcalHPDNoise",
                    "Commissioning",
                    "Cosmics",
                    "EmptyBX"]
#    for ds in api.listDatasets(dataset='/HIN*/%s*/RAW' % acquisition_era):
#        pd_blacklist.append(ds['dataset'].split('/')[1])
        
#    for ds in api.listDatasets(dataset='/L1MinimumBias*/%s*/RAW' % acquisition_era):
#        pd_blacklist.append(ds['dataset'].split('/')[1])

#    for ds in api.listDatasets(dataset='/ZeroBias*/%s*/RAW' % acquisition_era):
#        pd_tmp = ds['dataset'].split('/')[1]
#        if(pd_tmp != 'ZeroBias'):
#            pd_blacklist.append(pd_tmp)

#reads all datasets for each era then all, but JetHT,  are appended in the blacklist 

    for ds in api.listDatasets(dataset='/*/%s*/RAW' % acquisition_era):
        pd_tmp = ds['dataset'].split('/')[1]
        if(pd_tmp != 'JetHT'):
            pd_blacklist.append(pd_tmp)
            

    print 'list of blacklisted PDs:'
    print pd_blacklist
    #FIXME: add mapping of priority for PD which need higher-priority
    #JEC: ZeroBias/SinglePhoton/JetHT/DoubleEG/DoubleMu

    pd_priorities = {}
    # these are the PDs for JME
    pd_priorities['ZeroBias'] = 90000
    pd_priorities['SinglePhoton'] = 90000
    pd_priorities['JetHT'] = 90000
    pd_priorities['DoubleEG'] = 90000
    pd_priorities['DoubleMuon'] = 90000
    pd_priorities['SingleElectron'] = 90000
    pd_priorities['SingleMuon'] = 90000
    pd_priorities['MuonEG'] = 90000
    pd_priorities['Charmonium'] = 90000
    pd_priorities['MuOnia'] = 90000


    campaign = acquisition_era
    num_core = 4

    if (era == 'Run2016B-v2') :
        proc_string = proc_string+'_ver2'
    if (era == 'Run2016B-v1') :
        proc_string = proc_string+'_ver1'


    #=======================================================
    # Here we get some variables from the environment
    username = os.environ['USER']
    cmssw_version = os.environ['CMSSW_VERSION']
    print 'USER: %s' % username
    print 'CMSSW_VERSION: %s' % cmssw_version


    #======================================================

    with open(jsonFile) as data_file:
        data = json.load(data_file)
    #print data.keys()
    AlltheRuns = map(int,data.keys())
    print sorted(AlltheRuns)
    print "# of runs in the JSON: ", len(AlltheRuns)
    # select runs in Run2016B
    #FIXME: is this really needed
    #theRuns = filter(lambda x: ((x >= 272007) and (x <= 275376)), AlltheRuns)
    theRuns = AlltheRuns
    print sorted(theRuns)

#    theDatasets = api.listDatasets(data_tier_name='RAW', acquisition_era_name='%s' % era)
    theDatasets = api.listDatasets(data_tier_name='RAW', processed_ds_name='*%s*' % era)


    print theDatasets

#theDatasetsAOD = api.listDatasets( dataset='/*/*Run2016B-v2*PromptReco*/AOD' % acquisition_era )
#theDatasetsAOD = api.listDatasets( data_tier_name='AOD', acquisition_era_name='Run2016B')
    theDatasetsAOD = api.listDatasets( data_tier_name='AOD', processed_ds_name='*%s*' % acquisition_era)


    print '# of RAW datasets matching era %s: %i' %(acquisition_era, len(theDatasets))
    #print theDatasets
    print '# of AOD datasets matching era %s: %i' %(acquisition_era, len(theDatasetsAOD))
    #print theDatasetsAOD
    theDatasetsToProcessAOD = []
    theDatasetsToProcess = []

    for mydataset in theDatasetsAOD:
        tempdataset = mydataset['dataset']
        theDatasetsToProcessAOD.append((tempdataset.split('/'))[1])

    print '# of PDs having AOD dataset in prompt %i' % len(theDatasetsToProcessAOD)
    #NOTE: this is NOT the # of PDs since here there is multiplicity due to various prompt reco version making each PD to appear n times
    #print theDatasetsToProcessAOD

    if not os.path.exists(era):
        os.makedirs(era)
    previous_dir = os.getcwd()
    os.chdir(era)

    nd = 0
    twiki=file('twiki_%s.twiki' % campaign, 'w')
    twiki.write('---+++ !%s \n\n' % acquisition_era)
    twiki.write('| *DataSet* | *prepID monitoring* | *run* |\n')


    master=file('master_'+era+'.conf','w')
    master.write("[DEFAULT] \n")
    master.write("group=ppd \n")
    master.write("user=%s \n" % username)
    master.write("request_type=ReReco \n")
    master.write("release=%s \n" % cmssw_version)
    master.write("globaltag=%s \n" % GT)
    master.write("\n")
    master.write("campaign="+campaign+"\n")
    master.write("\n")
    master.write("processing_string="+proc_string+" \n")
    master.write("\n")
    master.write("priority=%i \n" % default_priority)
    master.write("time_event=4 \n")
    master.write("size_event=500 \n")
    master.write("size_memory = 7000 \n")
    master.write("multicore=%i \n" % num_core)

    cfg_harvesting_file_name = 'harvesting.py'
    master.write("harvest_cfg=%s \n" % cfg_harvesting_file_name)

    harvesting_command = 'cmsDriver.py step4 --data --filetype DQM --conditions %s -s HARVESTING:@allForPrompt --scenario pp --filein file:RECO_RAW2DIGI_L1Reco_RECO_ALCA_EI_PAT_DQM_inDQM.root --python_filename=%s --no_exec' % (GT, cfg_harvesting_file_name)
    if not os.path.isfile(cfg_harvesting_file_name):
        print 'creating harvesting cfg...'
        st_and_out_harvst = commands.getstatusoutput(harvesting_command)
        if st_and_out_harvst[0] != 0:
            print '[ERROR] cfg creation failed with message: %s' % st_and_out_harvst[1]



    master.flush()

    for oneDS in theDatasets:

        theDataset= oneDS['dataset']
        pd_name = theDataset.split('/')[1]
        era_version = theDataset.split('/')[2]

        print '--- dataset %s' % theDataset
        print '--- era %s' % era_version

        if (("v1" in era_version) and (era=="Run2016B-v2") ) :
            print ' wrong era'
            continue

        if (("v2" in era_version) and (era=="Run2016B-v1") ) :
            print ' wrong era'
            continue

        if pd_name in theDatasetsToProcessAOD:
            if pd_name in pd_blacklist:
                print '    PD is blacklisted'
                continue
            print '    adding to re-reco matrix'

            #print oneDS
            #print api.listRuns(dataset=theDataset)
            runs = api.listRuns(dataset=theDataset)[0]['run_num']
            if("NoBPTX" in (pd_name) ) :
                inter = set(runs)
            else :
                inter = set(runs) & set(theRuns)

            if("PA" in (pd_name) ) :
                print ' wrong PA dataset'
                continue

                
            input_file_name = 'file:pippo.root'
            if len(inter) > 0 :
                theDatasetsToProcess.append(theDataset)
                if("MinimumBias" in (pd_name) ) :
                    #print sorted(runs)
                    #print sorted(inter)
                    print "     # of runs in the dataset: ", len(runs)
                    print "     # of runs in the intersection: ", len(inter)
                    #input_file_name = api.listFiles(dataset=theDataset, run_num=inter[0])[0]['logical_file_name']

                #input_file_name = api.listFiles(dataset=theDataset, run_num=list(inter)[0])[0]['logical_file_name']

                nd = nd+1
                theruns = sorted(inter)

    #            pd_name_short = pd_name.replace("_0T","")
    #            print "dataset = ", pd_name
    #            print "dataset_short = ", pd_name_short

                cfg_file_name = 'recoskim_%s_%s.py' % (era, pd_name)
                prep_id = "ReReco-"+campaign+"-"+pd_name+"-"+proc_string+"-"+(format(nd, '04d'))
                #print cfg_file_name
                # Now write the section of the cfg specific to this PD/request
                master.write("\n")
                master.write('[%s-%s-%s]\n' % (era_version, pd_name, proc_string))
                master.write("dset_run_dict={\""+theDataset+"\" : "+str(theruns)+" }\n")
                master.write("cfg_path=%s\n" % cfg_file_name)
                master.write("request_id=%s \n" % prep_id)
                # here create the cfg file

                alcaseq = ''
                skimseq = ''
                recotier = ''
                keepreco = False

    #            if ( ("NoBPTX" in pd_name) or ("DoubleMuon" in pd_name) or ("EmptyBX" in pd_name) or
    #            ("ZeroBias" in pd_name) or ("MinimumBias" in pd_name) or ("SingleMu" in pd_name) ) :
    #                keepreco = True
    #                recotier = 'RECO,'
                if ("NoBPTX" in pd_name) :
                    recotier = 'RECO,'
                    

                if pd_name in pd_priorities.keys():
                    master.write("priority=%i \n" % pd_priorities[pd_name])

                if pd_name in autoSkim.keys():
                    skimseq='SKIM:%s,'%(autoSkim[pd_name])
    #            if pd_name_short in autoSkim.keys():
    #                recotier = 'RECO,'

                if pd_name in AlCaRecoMatrixRereco.keys():
                    alcaseq='ALCA:%s,'%(AlCaRecoMatrixRereco[pd_name])

                #if ( (pd_name in autoSkim.keys()) and (not(keepreco)) ) :
                #    #            if ( (pd_name_short in autoSkim.keys()) and (not(keepreco)) ) :
                #    master.write("transient_output = [\"RECOoutput\"]")
                #    master.write("\n")
                #    recotier='RECO,'

                reco_command = 'cmsDriver.py RECO -s RAW2DIGI,L1Reco,RECO,%sEI,PAT,DQM:@allForPrompt --runUnscheduled --nThreads %i --data --era Run2_2016 --scenario pp --conditions %s --eventcontent %sAOD,MINIAOD,DQM --datatier %sAOD,MINIAOD,DQMIO --customise %s --filein %s -n 100 --python_filename=%s --no_exec' % (skimseq+alcaseq, num_core, GT, recotier, recotier, str(customera[campaign]), input_file_name, cfg_file_name)

#                reco_command = 'cmsDriver.py RECO -s RAW2DIGI,L1Reco,RECO,%sEI,PAT,DQM:@allForPrompt --runUnscheduled --nThreads %i --data --era Run2_2016 --scenario pp --conditions %s --eventcontent %sAOD,MINIAOD,DQM --datatier %sAOD,MINIAOD,DQMIO --customise %s --filein %s -n 100 --python_filename=%s --no_exec' % (skimseq+alcaseq, num_core, GT, recotier, recotier, customera[campaign], input_file_name, cfg_file_name)
                print '    cmsDriver command: %s' % reco_command

                if not os.path.isfile(cfg_file_name):
                    print '     creating the cfg...'
                    st_and_out = commands.getstatusoutput(reco_command)
                    if st_and_out[0] != 0:
                        print '[ERROR] cfg creation failed with message: %s' % st_and_out[1]

                master.flush()
                twiki.write("| %s | [[https://cms-pdmv.cern.ch/pmp/historical?r=%s][%s]] | %s |\n"  %(theDataset, prep_id, prep_id, str(theruns)))
    #            reco_command = 'cmsDriver.py RECO -s RAW2DIGI,L1Reco,RECO,EI,PAT,DQM:@standardDQM+@miniAODDQM --runUnscheduled --nThreads '+num_core+ ' --data --scenario pp --conditions %s --eventcontent %sAOD,MINIAOD,DQM --datatier %sAOD,MINIAOD,DQMIO --customise Configuration/DataProcessing/RecoTLR.%s --filein blah.root -n 100 --python_filename=reco_%s_boff_%s.py --no_exec'%(GT, recotier, recotier, customera[campaign], campaign, pd_name)
    #            print reco_command
    #            os.system(reco_command)

    #                skim_command='cmsDriver.py skim -s SKIM:%s --data --no_output --conditions %s --runUnscheduled --nThreads %s --python_filename skim_%s_boff_%s.py --no_exec'%(autoSkim[pd_name_short],GT,num_core,campaign,pd_name)
    #                print skim_command
    #                os.system(skim_command)


    #            print "request_id=ReReco-"+era_version.rstrip('-v1')+"-10Dec2015-"+(format(nd, '04d'))
            else:
                print '    [WARNING] dataset has no runs in DCS JSON, skipping'

        else:
            print '    no AOD for this in prompt-reco: skipping'

    ################################

    ##### printout for twiki
    #            print "|"+theDataset+"|"+str(theruns)+"|"
    ################################
    twiki.close()
    master.close()
    os.chdir(previous_dir)

    print
    print
    #print theDatasetsToProcess
    print "\n".join(theDatasetsToProcess)
    print "number of datasets with run overlap: %s"%(len(theDatasetsToProcess))
    print "number of datasets with AOD: %s"%(len(theDatasetsToProcessAOD))
