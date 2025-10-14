# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from vmwarelib.actions import BaseAction


class CategoryListDetails(BaseAction):
    def run(self, **kwargs):
        """
        List all tag categories from vsphere with full details (name, description, etc)

        Args:
        - kwargs: inputs to the action
          - vsphere: Pre-configured vsphere connection details (config.yaml)

        Returns:
        - list: List of all tag category details including id, name, description, cardinality
        """
        self.connect_rest(kwargs.get("vsphere"))

        category_ids = self.tagging.category_list()
        categories = []

        for category_id in category_ids:
            category_details = self.tagging.category_get(category_id)
            categories.append(category_details)

        return categories
