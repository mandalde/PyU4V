# The MIT License (MIT)
# Copyright (c) 2016 Dell Inc. or its subsidiaries.

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Lab2.py
This python scrtipt will create a snapvx snapshot on the specified storage group and timestamp the name.  Each snapshot is preserved
for 24 hours.

REST call create_new_snap from
"""
import argparse
from PyU4V.rest_univmax import rest_functions
from time import strftime

######################################################################
# Define and Parse CLI arguments    and instantiate session for REST #
######################################################################

PARSER = argparse.ArgumentParser(description='Example implementation of a Python REST client for EMC Unisphere Taking SnapVX Snapshots.')
RFLAGS = PARSER.add_argument_group('Required arguments')
RFLAGS.add_argument('-sgname', required=True, help='Storage group name, typically the application name e.g. oraclefinace')
ARGS = PARSER.parse_args()

#Variables are initiated to appent REST to the Storage Group and Initiator
#SG and IG will append _SG or _IG to the name passed by the user.  e.g. REST_Oracle_IG and REST_ORACLE_IG



SGNAME = ARGS.sgname
sg_id=SGNAME

ru = rest_functions()


snap_name=("REST_Snap_")+strftime ("%d%m%Y%H%M%S")  #assign name to snap with date and time appended to name

if 200 in ru.create_sg_snapshot(sg_id,snap_name):
    print("Snapshot has been created for storage group %s with the name %s" %(sg_id, snap_name))
else:
    print ("There was a problem creating the snapshot please check the symapi log file on the Unipshere server for more information")