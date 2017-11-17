# This file and its contents are supplied under the terms of the
# Common Development and Distribution License ("CDDL"). You may
# only use this file in accordance with the terms of the CDDL.
#
# A full copy of the text of the CDDL should have accompanied this
# source. A copy of the CDDL is also available via the Internet at
# http://www.illumos.org/license/CDDL.
#

#
# Copyright 2017 <contributor name>
#

include ../../../make-rules/shared-macros.mk

COMPONENT_NAME=        icinga2
COMPONENT_VERSION=     2.7.2
COMPONENT_SUMMARY=     Icinga 2 - an open source monitoring system
COMPONENT_PROJECT_URL= https://github.com/icinga
COMPONENT_FMRI=        system/monitoring/icinga2
COMPONENT_CLASSIFICATION=Applications/System Utilities
COMPONENT_SRC=          $(COMPONENT_NAME)-$(COMPONENT_VERSION)
COMPONENT_ARCHIVE=      $(COMPONENT_SRC).tar.gz
COMPONENT_ARCHIVE_URL= \
  https://github.com/Icinga/icinga2/archive/v$(COMPONENT_VERSION).tar.gz
COMPONENT_ARCHIVE_HASH= \
  sha256:7e9691ad3389f04a53042d88c1ac8a37e2c9aaf8287856cad3fa48825adaee84
COMPONENT_LICENSE=     GPLv2

include $(WS_MAKE_RULES)/prep.mk
include $(WS_MAKE_RULES)/cmake.mk
include $(WS_MAKE_RULES)/ips.mk

PATH=$(PG_BINDIR.$(BITS)):$(MYSQL_BINDIR.$(BITS)):$(PATH.gnu)

CPPFLAGS+= $(CPP_XPG6MODE)

CMAKE_BINDIR.64 = $(CMAKE_BINDIR.32)
CMAKE_SBINDIR.64= $(CMAKE_SBINDIR.32)

CMAKE_OPTIONS+= -DICINGA2_WITH_MYSQL=OFF
CMAKE_OPTIONS+= -DICINGA2_WITH_PGSQL=OFF

build: $(BUILD_64)

install: $(INSTALL_64)

test: $(NO_TESTS)

