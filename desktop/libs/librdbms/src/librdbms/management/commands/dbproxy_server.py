#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import subprocess

from django.core.management.base import NoArgsCommand
import spark.conf


LOG = logging.getLogger(__name__)


class Command(NoArgsCommand):
  """
  Starts DBProxy server for providing a JDBC gateway.
  """

  help = 'start DBProxy server for providing a JDBC gateway'

  def handle(self, *args, **kwargs):
    env = os.environ.copy()

    args.append("com.cloudera.hue.livy.server.Main")

    LOG.info("Executing %r (%r) (%r)" % (args[0], args, env))

    # Use exec, so that this takes only one process.
    os.execvpe(args[0], args, env)
