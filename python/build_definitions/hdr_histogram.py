#
# Copyright (c) YugaByte, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations
# under the License.
#

import os

from yugabyte_db_thirdparty.build_definition_helpers import *  # noqa


class HdrHistogramDependency(Dependency):
    def __init__(self) -> None:
        super(HdrHistogramDependency, self).__init__(
            name='HdrHistogram_c',
            version='0.11.6-yb',
            url_pattern='https://github.com/rachelphan1508/HdrHistogram_c/archive/refs/tags/{0}.tar.gz',
            build_group=BUILD_GROUP_COMMON)
        self.copy_sources = True

    def build(self, builder: BuilderInterface) -> None:
        log_prefix = builder.log_prefix(self)
        builder.build_with_cmake(self,
                                 ['-DCMAKE_BUILD_TYPE=Release'])
        builder.log_output(log_prefix, ['cp', 'include/hdr/hdr_histogram.h', builder.prefix_include])
