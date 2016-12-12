#
# This file and its contents are supplied under the terms of the
# Common Development and Distribution License ("CDDL"). You may
# only use this file in accordance with the terms of the CDDL.
#
# A full copy of the text of the CDDL should have accompanied this
# source. A copy of the CDDL is also available via the Internet at
# http://www.illumos.org/license/CDDL.
#

#
# Copyright 2016 Aurelien Larcher <aurelien.larcher@gmail.com>
#

include ../../../make-rules/shared-macros.mk

COMPONENT_NAME= memtest86+
COMPONENT_VERSION= 5.01
IPS_COMPONENT_VERSION= 5.0.1
COMPONENT_SUMMARY= Memtest86+ - standalon memory testing tool for x86 systems
COMPONENT_PROJECT_URL= http://www.memtest.org/
COMPONENT_FMRI= diagnostic/$(COMPONENT_NAME)
COMPONENT_CLASSIFICATION= Applications/System Utilities
COMPONENT_SRC=		$(COMPONENT_NAME)-$(COMPONENT_VERSION)
COMPONENT_ARCHIVE=	$(COMPONENT_SRC).tar.gz
COMPONENT_ARCHIVE_URL= http://www.memtest.org/download/$(COMPONENT_VERSION)/$(COMPONENT_ARCHIVE)
COMPONENT_ARCHIVE_HASH= \
	sha256:142127b7953fbd829b1057fb64a78d3340c2b771484230a7347e94530a0d9039
COMPONENT_LICENSE= GPLv2

include $(WS_MAKE_RULES)/prep.mk
include $(WS_MAKE_RULES)/justmake.mk
include $(WS_MAKE_RULES)/ips.mk

PATCH_LEVEL=0

COMPONENT_PREP_ACTION= $(CP) $(COMPONENT_DIR)/files/io.h $(SOURCE_DIR)

build:		$(BUILD_32)

install:	$(INSTALL_32)

test:		$(TEST_32)
