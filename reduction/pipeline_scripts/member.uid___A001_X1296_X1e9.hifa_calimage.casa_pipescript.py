from recipes.almahelpers import fixsyscaltimes # SACM/JAO - Fixes
__rethrow_casa_exceptions = True
context = h_init()
context.set_state('ProjectSummary', 'proposal_code', '2017.1.01355.L')
context.set_state('ProjectSummary', 'piname', 'unknown')
context.set_state('ProjectSummary', 'proposal_title', 'unknown')
context.set_state('ProjectStructure', 'ous_part_id', 'X2079645644')
context.set_state('ProjectStructure', 'ous_title', 'Undefined')
context.set_state('ProjectStructure', 'ppr_file', '/opt/dared/opt/c5r1/mnt/dataproc/2017.1.01355.L_2017_12_28T16_53_47.892/SOUS_uid___A001_X1296_X1e3/GOUS_uid___A001_X1296_X1e4/MOUS_uid___A001_X1296_X1e9/working/PPR_uid___A001_X1296_X1ea.xml')
context.set_state('ProjectStructure', 'ps_entity_id', 'uid://A001/X1220/Xddd')
context.set_state('ProjectStructure', 'recipe_name', 'hifa_calimage')
context.set_state('ProjectStructure', 'ous_entity_id', 'uid://A001/X1220/Xdd9')
context.set_state('ProjectStructure', 'ousstatus_entity_id', 'uid://A001/X1296/X1e9')
try:
    hifa_importdata(vis=['uid___A002_Xc7fa6f_X3cc9', 'uid___A002_Xc81f73_X3a2e', 'uid___A002_Xc82bb8_X2f4d', 'uid___A002_Xc82bb8_X336f', 'uid___A002_Xc8592e_X7d0e'], session=['session_1', 'session_2', 'session_3', 'session_3', 'session_5'])
    fixsyscaltimes(vis = 'uid___A002_Xc8592e_X7d0e.ms')# SACM/JAO - Fixes
    fixsyscaltimes(vis = 'uid___A002_Xc82bb8_X2f4d.ms')# SACM/JAO - Fixes
    fixsyscaltimes(vis = 'uid___A002_Xc81f73_X3a2e.ms')# SACM/JAO - Fixes
    fixsyscaltimes(vis = 'uid___A002_Xc82bb8_X336f.ms')# SACM/JAO - Fixes
    fixsyscaltimes(vis = 'uid___A002_Xc7fa6f_X3cc9.ms')# SACM/JAO - Fixes
    h_save() # SACM/JAO - Finish weblog after fixes
    h_init() # SACM/JAO - Restart weblog after fixes
    hifa_importdata(vis=['uid___A002_Xc7fa6f_X3cc9', 'uid___A002_Xc81f73_X3a2e', 'uid___A002_Xc82bb8_X2f4d', 'uid___A002_Xc82bb8_X336f', 'uid___A002_Xc8592e_X7d0e'], session=['session_1', 'session_2', 'session_3', 'session_3', 'session_5'])
    hifa_flagdata(pipelinemode="automatic")
    hifa_fluxcalflag(pipelinemode="automatic")
    hif_rawflagchans(pipelinemode="automatic")
    hif_refant(pipelinemode="automatic")
    h_tsyscal(pipelinemode="automatic")
    hifa_tsysflag(pipelinemode="automatic")
    hifa_antpos(pipelinemode="automatic")
    hifa_wvrgcalflag(pipelinemode="automatic")
    hif_lowgainflag(pipelinemode="automatic")
    hif_setmodels(pipelinemode="automatic")
    hifa_bandpassflag(pipelinemode="automatic")
    hifa_spwphaseup(pipelinemode="automatic")
    hifa_gfluxscaleflag(pipelinemode="automatic")
    hifa_gfluxscale(pipelinemode="automatic")
    hifa_timegaincal(pipelinemode="automatic")
    hif_applycal(pipelinemode="automatic")
    hifa_imageprecheck(pipelinemode="automatic")
    hif_makeimlist(intent='PHASE,BANDPASS,CHECK')
    hif_makeimages(pipelinemode="automatic")
    hif_checkproductsize(maxcubelimit=40.0, maxproductsize=400.0, maxcubesize=30.0)
    hifa_exportdata(pipelinemode="automatic")
    hif_mstransform(pipelinemode="automatic")
    hifa_flagtargets(pipelinemode="automatic")
    hif_makeimlist(specmode='mfs')
    hif_findcont(pipelinemode="automatic")
    hif_uvcontfit(pipelinemode="automatic")
    hif_uvcontsub(pipelinemode="automatic")
    hif_makeimages(pipelinemode="automatic")
    hif_makeimlist(specmode='cont')
    hif_makeimages(pipelinemode="automatic")
    hif_makeimlist(pipelinemode="automatic")
    hif_makeimages(pipelinemode="automatic")
    hif_makeimlist(specmode='repBW')
    hif_makeimages(pipelinemode="automatic")
finally:
    h_save()
