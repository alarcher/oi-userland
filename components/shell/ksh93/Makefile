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
# Copyright (c) 2012, 2013, Oracle and/or its affiliates. All rights reserved.
#
include ../../../make-rules/shared-macros.mk

COMPONENT_NAME=       ksh93
KSH93_RELEASE=        v
KSH93_RELEASE_NUM=    22
COMPONENT_VERSION=    2016-01-10
COMPONENT_FMRI=       shell/ksh93
COMPONENT_PROJECT_URL=http://kornshell.com/
COMPONENT_SUMMARY=    Ksh93 - The AT&T Korn Shell
COMPONENT_CLASSIFICATION=System/Shells
COMPONENT_SRC_NAME=   $(COMPONENT_NAME)$(KSH93_RELEASE)
COMPONENT_SRC=        $(COMPONENT_NAME)-$(COMPONENT_SRC_NAME)
COMPONENT_ARCHIVE=    $(COMPONENT_SRC_NAME)-$(COMPONENT_VERSION).tar.gz
COMPONENT_ARCHIVE_HASH= \
  sha256:44a3f00a713c48889339f163cf1571fd327db1784f3f4ba6c0bc1759f4063ce4
COMPONENT_ARCHIVE_URL= i\
  https://github.com/alarcher/ksh93/archive/$(COMPONENT_SRC_NAME).tar.gz 

# Packaging information.
# Note how the AT&T "version letter symbol date" code is translated 
# into the IPS version number:
# 
# shell/ksh93@93.<letter representation>.<0 or 1>.<yymmdd>
#
# <letter representation> is the numeric place in the alphabet of the 
# major version letter.
# 
# <0 or 1> is the presence or absence of the "+" symbol in the AT&T
# version code. The "+" represents a point/bugfix release and would appear as
# "93<version letter>+" in the human readable form.
#
# EXAMPLE:
# AT&T Version string: 93u+ 2011-02-08
# IPS Version number: 93.21.1.20110208
#
IPS_COMPONENT_VERSION= 93.$(KSH_RELEASE_NUM).0.$(filter-out -,$(COMPONENT_VERSION))
IPS_HUMAN_VERSION= "93$(KSH93_RELEASE) $(COMPONENT_VERSION)"

include $(WS_MAKE_RULES)/prep.mk
include $(WS_MAKE_RULES)/attpackagemake.mk
include $(WS_MAKE_RULES)/ips.mk

# Fixup HOSTTYPE to match uname output and bits
HOSTTYPE32=sol11.$(shell uname -p)
HOSTTYPE64=sol11.$(shell uname -p)-64

# We override LD_B_DIRECT because -B direct has unfortunate consequences for the
# interposition used by the Safe/Fast IO library (i.e. it becomes neither safe
# nor fast, and causes the build to deadly embrace). 
LD_B_DIRECT=

# Disable nmake's probing of runpaths
CC.RUNPATH=
CC.LD.RUNPATH=
CC.LD.ORIGIN=
CC.DLL.ORIGIN=

# Prevent nmake from taking o er the entire machine
NPROC=$(filter -j%,$(COMPONENT_BUILD_ARGS))

# Set the built to build all targets, install all of ast-base, and test ksh93.
COMPONENT_BUILD_TARGETS += 
COMPONENT_TEST_TARGETS = ksh93

# Add the two tarball paths to the paths to be cleaned
CLEAN_PATHS+= build $(COMPONENT_NAME_1).$(COMPONENT_VERSION_1) \
              $(COMPONENT_NAME).$(COMPONENT_VERSION)

# ksh.kshrc needs to be installed with the ksh package
COMPONENT_POST_INSTALL_ACTION= \
	@$(MKDIR) -p $(PROTO_DIR)/etc/; \
	$(CP) ksh.kshrc $(PROTO_DIR)/etc/ 

# common targets
build:		$(BUILD_32_and_64)
	
install:	$(INSTALL_32_and_64)	
		
test:		$(TEST_32_and_64)

BUILD_PKG_DEPENDENCIES= $(BUILD_TOOLS)

PKG_PROTO_DIRS +=   $(COMPONENT_DIR)/files

