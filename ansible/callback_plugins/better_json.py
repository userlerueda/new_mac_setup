# (c) 2016, Matt Martz <matt@sivel.net>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
from ansible.utils.color import colorize, hostcolor
from termcolor import colored
from ansible import constants as C
import pprint
__metaclass__ = type

import json

from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'better_json'

    def __init__(self, display=None):
        super(CallbackModule, self).__init__(display)
        self.results = []

    def _new_play(self, play):
        return {
            'play': {
                'name': play.name,
                'id': str(play._uuid)
            },
            'tasks': []
        }

    def _new_task(self, task):
        return {
            'task': {
                'name': task.name,
                'id': str(task._uuid)
            },
            'hosts': {}
        }

    def v2_playbook_on_play_start(self, play):
        self.results.append(self._new_play(play))

    def v2_playbook_on_task_start(self, task, is_conditional):
        self.results[-1]['tasks'].append(self._new_task(task))

    def v2_runner_on_failed(self, result, **kwargs):
        host = result._host
        task = result._task
        self.results[-1]['tasks'][-1]['hosts'][host.name] = result._result
        msg_result = result._result
        if "ansible_facts" not in msg_result.keys():
            changed = msg_result["changed"]
            delta = msg_result["msg"]["delta"]
            msg = "HOST: {:<10} {:<90} {} Time {}".format(
                host, task, colored("Error", C.COLOR_ERROR), delta)
            self._display.display(msg)
        else:
            # Facts not relevant so skipping
            pass


    def v2_runner_on_unreachable(self, result, **kwargs):
        C.COLOR_UNREACHABLE

    def v2_runner_on_skipped(self, result, **kwargs):
        host = result._host
        task = result._task
        self.results[-1]['tasks'][-1]['hosts'][host.name] = result._result
        msg_result = result._result
        if "ansible_facts" not in msg_result.keys():
            changed = msg_result["changed"]
            msg = "HOST: {:<10} {:<90} {}".format(
                host, task, colored("Skipped", C.COLOR_SKIP))
            self._display.display(msg)
        else:
            # Facts not relevant so skipping
            pass


    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        task = result._task
        self.results[-1]['tasks'][-1]['hosts'][host.name] = result._result
        msg_result = result._result
        if "ansible_facts" not in msg_result.keys():
            changed = msg_result["changed"]
            # delta = msg_result["results"][0]["delta"]
            if changed:
                msg = "HOST: {} {} {}".format(
                    host, task, colored("OK", C.COLOR_CHANGED))
            else:
                msg = "HOST: {} {} {}".format(
                    host, task, colored("OK", C.COLOR_OK))
            self._display.display(msg)
        else:
            # Facts not relevant so skipping
            pass

    def v2_playbook_on_stats(self, stats):
        """Display info about playbook statistics"""

        hosts = sorted(stats.processed.keys())

        summary = {}
        for h in hosts:
            s = stats.summarize(h)
            summary[h] = s

        output = {
            'plays': self.results,
            'stats': summary
        }

        # self._display.display(json.dumps(output, indent=4, sort_keys=True))
