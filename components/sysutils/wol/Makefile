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
# Copyright 2017 <contributor name>
#

include ../../../make-rules/shared-macros.mk

COMPONENT_NAME=         wol.c
IPS_COMPONENT_NAME=     wol
COMPONENT_VERSION=      0.0.1
GIT_COMMIT_HASH=        b9d89af91a8bd70770d272205020c3dc32c94dff
COMPONENT_SUMMARY=	wol.c - A simple Wake-on-LAN utility written in C
COMPONENT_PROJECT_URL=  https://github.com/msanders/wol.c
COMPONENT_FMRI=         system/management/wol
COMPONENT_CLASSIFICATION=System/Hardware
COMPONENT_SRC=          $(COMPONENT_NAME)-$(GIT_COMMIT_HASH)
COMPONENT_ARCHIVE=      $(COMPONENT_NAME)-$(COMPONENT_VERSION).tar.gz
COMPONENT_ARCHIVE_URL= \
  https://github.com/msanders/wol.c/archive/$(GIT_COMMIT_HASH).tar.gz
COMPONENT_ARCHIVE_HASH= \
  sha256:072400d11af31ef1b84a1da7ea48bd3777cfabbc1ebf757ad966254f1db926b6
COMPONENT_LICENSE=      MIT

include $(WS_MAKE_RULES)/prep.mk
include $(WS_MAKE_RULES)/justmake.mk
include $(WS_MAKE_RULES)/ips.mk

COMPONENT_BUILD_ENV += CC="$(CC)"
COMPONENT_BUILD_ENV += CFLAGS="$(CFLAGS)"
COMPONENT_BUILD_ENV += LDFLAGS="$(LDFLAGS)"

COMPONENT_INSTALL_ENV += PREFIX="$(USRDIR)"

COMPONENT_PRE_INSTALL_ACTION= \
  ($(MKDIR) $(PROTOUSRBINDIR) $(PROTOUSRSHAREMAN1DIR))

build:		$(BUILD_64)

install:	$(INSTALL_64)

test:		$(NO_TESTS)

# Auto-generated dependencies
REQUIRED_PACKAGES += system/library
