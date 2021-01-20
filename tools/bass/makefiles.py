#!/usr/bin/python3.5
#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#
# This is all very naive and will hurt pythonists' eyes.
#

import os
import re
import subprocess
import warnings

from .component import Component


class Keywords(object):
    def __init__(self):
        self.variables = {
            "BUILD_BITS":
            ["NO_ARCH",
             "32",
             "64",
             "32_and_64",
             "64_and_32"],
            "BUILD_STYLE":
                ["ant",
                 "attpackagemake",
                 "cmake",
                 "configure",
                 "gem",
                 "justmake",
                 "makemaker",
                 "meson",
                 "ocaml",
                 "setup.py",
                 "waf"],
            "MK_BITS":
            ["NO_ARCH",
             "32",
             "64",
             "32_and_64"],
            "COMPONENT_NAME": [],
            "COMPONENT_VERSION": [],
            "COMPONENT_REVISION": [],
            "COMPONENT_FMRI": [],
            "COMPONENT_CLASSIFICATION": [],
            "COMPONENT_SUMMARY": [],
            "COMPONENT_PROJECT_URL": [],
            "COMPONENT_SRC": ["$(COMPONENT_NAME)-$(COMPONENT_VERSION)"],
            "COMPONENT_ARCHIVE": [],
            "COMPONENT_ARCHIVE_URL": [],
            "COMPONENT_ARCHIVE_HASH": [],
            "COMPONENT_LICENSE": [],
            "COMPONENT_LICENSE_FILE": []
        }
        self.targets = {
            "build": [ "BUILD_$(MK_BITS)"],
            "install": ["INSTALL_$(MK_BITS)"],
            "test": ["TEST_$(MK_BITS)", "NO_TESTS"],
            "system-test": ["SYSTEM_TEST_$(MK_BITS)", "SYSTEM_TESTS_NOT_IMPLEMENTED"]
        }

class Item(object):
    def __init__(self, line=None, content=[]):
        self.idx = line 
        self.str = content 
    def line(self):
        return self.idx
    def include_line(self):
        return "include "+self.str[0]+"\n"
    def variable_assignment(self, variable):
        return "{:<24}".format(variable+"=")+self.str[0]
    def target_definition(self, target):
        ss = "{0:<24}{1}".format(target+":", self.str[0])
        for s in self.str[1:]:
            ss += "\n\t" + s
        ss+= "\n"
        return ss

class Makefile(object):
    def __init__(self, path=None, debug=False):
        self.debug = debug
        self.path = path
        self.component = Component()
        self.includes = []
        self.variables = {}
        self.targets = {}
        makefile = os.path.join(path, 'Makefile')
        with open(makefile, 'r') as f:
            self.contents = f.readlines()
        self.update()

    def update(self):
        # Construct list of keywords
        kw = Keywords()

        # Variable is set
        m = None
        # Target is set
        t = None
        # Rule definition
        d = None
        for idx, line in enumerate(self.contents):
            # Continuation of target line
            if t is not None:
                r = re.match(r"^[\s]*(.*)[\s]*([\\]?)[\s]*$", line)
                # Concatenate
                self.targets[t].str[0] += "\\".join(r.group(1))
                # Check for continuation or move to definition
                if not r.group(2):
                    d = t 
                    t = None
                continue
            if d is not None:
                # Concatenate
                r = re.match(r"^[\t][\s]*(.*)[\s]*$", line)
                # End of definition
                if r is None:
                    d = None
                    continue
                self.targets[d].str += [r.group(1)]
            # Continuation line of variable
            if m is not None:
                r = re.match(r"^[\s]*(.*)[\s]*([\\]?)[\s]*$", line)
                self.variables[m].str += [r.group(1)]
                if not r.group(2):
                    m = None
                continue
            if re.match(r"^#", line):
                continue
            # Check for include
            r = re.match(r"^include[\s]+(.*)", line)
            if r is not None:
               self.includes += [Item(idx, [r.group(1)])]
            else:
                found = False
                # Collect known variables
                for k in list(kw.variables.keys()):
                    r = re.match(
                        r"^[\s]*("+k+r")[\s]*=[\s]*([^\\]*)[\s]*([\\]?)[\s]*$", line)
                    if r is not None:
                        found = True
                        v = r.group(2)
                        if v in self.variables.keys():
                            warnings.warn("Variable '"+v+"' redefined line "+idx)
                        self.variables[k] = Item(idx, [v])
                        if r.group(3):
                            m = k
                        break
                if found is True:
                    continue
                # Collect known targets
                for k in list(kw.targets.keys()):
                    r = re.match(
                        "^"+k+r"[\s]*:[\s]*(.*)[\s]*([\\]?)[\s]*$", line)
                    if r is not None:
                        found = True
                        v = r.group(1)
                        if v in self.targets.keys():
                            warnings.warn("Target '"+v+"' redefined line "+idx)
                        self.targets[k] = Item(idx, [v])
                        if r.group(2):
                            t = k
                            d = None
                        else:
                            t = None
                            d = k
                        break
                if found is True:
                    continue

    def display(self):
        print(self.path)
        print("includes:")
        print("---------")
        for i in iter(self.includes):
            print("{0:>3}: {1}".format(i.line(), i.include_line()))
        print("variables:")
        print("----------")
        for k,i in iter(self.variables.items()):
            print("{0:>3}: {1}".format(i.line(),i.variable_assignment(k)))
        print("targets:")
        print("--------")
        for k,i in iter(self.targets.items()):
            print("{0:>3}: {1}".format(i.line(),i.target_definition(k)))
        print('-' * 78)

    def run(self, targets):
        path = self.path
        result = []

        if self.debug:
            logger.debug('Executing \'gmake %s\' in %s', targets, path)

        proc = subprocess.Popen(['gmake', '-s', targets],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                cwd=path,
                                universal_newlines=True)
        stdout, stderr = proc.communicate()

        for out in stdout.splitlines():
            result.append(out.rstrip())

        if self.debug:
            if proc.returncode != 0:
                logger.debug('exit: %d, %s', proc.returncode, stderr)

        return result

    @staticmethod
    def value(variable):
        return "$("+variable+")"

    @staticmethod
    def makefile_path(name):
        return os.path.join("$(WS_MAKE_RULES)", name+".mk")

    @staticmethod
    def target_value(name, bits):
        return Makefile.value(name.upper()+"_"+bits)

