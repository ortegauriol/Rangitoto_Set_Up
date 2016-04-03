import os
class ToolData(object):
    pass
import sys
from socket import gethostname
host = gethostname()

cfg             = get_config()
cfg.config_dir  = os.path.join(os.environ['BCI_CONFIG'], 'combined')

if host == 'amcflip':
    polaris_dir     = os.environ['DBOX'] + '/ses/polaris/code'
elif host == 'UOA304332':
    polaris_dir     = os.path.normpath( os.environ['BCI_MODULES'] + '/polaris')

cfg.trigger     = 'DAQ_DATA'

# cfg.scale       = 1e6            # counts / m
cfg.scale       = 1e3            # counts / m
cfg.offset      = (0, 0, 0)      # in counts
cfg.x1          = (1, 0, 0)      # unitvector to point along x axis
cfg.y1          = (0, 1, 0)      # unitvector to point along y axis
cfg.gui_xrng    = (-.5,    .38)  # in m
cfg.gui_yrng    = (-.24,  .141)
cfg.gui_zrng    = (-.20,   .37)

# TOOLS
cfg.tool_dir    = os.path.normpath(polaris_dir + '/tool_definitions')

ST568 = ToolData()
ST568.name = 'ST568'

CT315 = ToolData()
CT315.name = 'CT315'

P717 = ToolData()
P717.name = 'P717'
P717.Ti = (42.5553894,   -10.26094437, -1751.98681641)
P717.Qi = (-0.23793141,   -0.74044655,    -0.52624678,  0.34379044)
P717.Ni = (54.54597092, -101.40107727, -1738.73937988)
# these co-ords agree to within 1 mm with the physical measurements I made:
# distance 92.88 mm here vs 93.57 mm measured
# vec btw tip and first ball (ref pt) of P717 (0.09255, 0, 0.013775) in m

#cfg.tool_list = [ST568, CT315, P717]
cfg.tool_list = [CT315]

cfg.tools = [x.name for x in cfg.tool_list]
