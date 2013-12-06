#
# This file and its contents are supplied under the terms of the
# Common Development and Distribution License ("CDDL)". You may
# only use this file in accordance with the terms of the CDDL.
#
# A full copy of the text of the CDDL should have accompanied this
# source. A copy of the CDDL is also available via the Internet at
# http://www.illumos.org/license/CDDL.
#

#
# Copyright (c) Aurelien Larcher. All rights reserved.
#
include ../../../make-rules/shared-macros.mk

COMPONENT_NAME=		matio
COMPONENT_VERSION=	1.5.2
COMPONENT_FMRI=		library/math/matio
COMPONENT_PROJECT_URL=	http://sourceforge.net/projects/matio/
COMPONENT_SRC=		$(COMPONENT_NAME)-$(COMPONENT_VERSION)
COMPONENT_ARCHIVE=	$(COMPONENT_SRC).tar.gz
COMPONENT_ARCHIVE_HASH=	\
    sha256:db02d0fb3373c3d766a606309b17e64a5d8da55610e921a9f1a0ec171e911d45
COMPONENT_ARCHIVE_URL=	http://sourceforge.net/projects/matio/files/matio/$(COMPONENT_VERSION)/$(COMPONENT_ARCHIVE)
COMPONENT_BUGDB=	$(COMPONENT_FMRI)
COMPONENT_LICENSE=	BSD	
COMPONENT_LICENSE_FILE= $(COMPONENT_NAME).license
COMPONENT_SUMMARY=	MAT File I/O Library - C library for reading and writing Matlab MAT files

include $(WS_MAKE_RULES)/prep.mk
include $(WS_MAKE_RULES)/configure.mk
include $(WS_MAKE_RULES)/ips.mk


CONFIGURE_OPTIONS+=	CFLAGS="$(CFLAGS) -I$(USRINCDIR)/hdf5 -D__EXTENSIONS__"
CONFIGURE_OPTIONS+=	--includedir=$(USRINCDIR)/$(COMPONENT_NAME)
CONFIGURE_OPTIONS+=	--enable-mat73=yes
CONFIGURE_OPTIONS+=	--with-hdf5=$(USRDIR)

# common targets
build:		$(BUILD_32_and_64)

install:	$(INSTALL_32_and_64)

BUILD_PKG_DEPENDENCIES =	$(BUILD_TOOLS)

include $(WS_MAKE_RULES)/depend.mk
