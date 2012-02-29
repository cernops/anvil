# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright (C) 2012 Yahoo! Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


# This is the base class for the various runners
class RunnerBase(object):
    def __init__(self, cfg, component_name, trace_dir):
        self.cfg = cfg
        self.component_name = component_name
        self.trace_dir = trace_dir

    def unconfigure(self):
        #cleans up anything configured by 
        #this runner for any apps for this component
        #returns how many files unconfigured
        return 0

    def configure(self, app_name, runtime_info):
        #returns how many files configured
        return 0

    def start(self, name, runtime_info):
        #returns a file name that contains what was started
        return None

    def stop(self, name):
        pass
