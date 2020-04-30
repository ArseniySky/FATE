#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from arch.api.utils import log_utils

LOGGER = log_utils.getLogger()


class ComponentBase(object):
    def run(self, component_parameters: dict = None, run_args: dict = None):
        pass

    def set_tracker(self, tracker):
        pass

    def save_data(self):
        pass

    def export_model(self):
        pass

    def set_taskid(self, taskid):
        pass

