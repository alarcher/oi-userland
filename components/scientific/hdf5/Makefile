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
# Copyright 2014 (c) Aurelien Larcher. All rights reserved.
#
include ../../../make-rules/shared-macros.mk

COMPONENT_NAME=           hdf5
COMPONENT_VERSION=        1.10.1
COMPONENT_FMRI=           library/c++/hdf5
COMPONENT_SUMMARY= \
	HDF5 - Data model, library, and file format for storing and managing data
COMPONENT_PROJECT_URL=    http://www.hdfgroup.org
COMPONENT_CLASSIFICATION= System/Libraries
COMPONENT_SRC=            $(COMPONENT_NAME)-$(COMPONENT_VERSION)
COMPONENT_ARCHIVE=        $(COMPONENT_SRC).tar.bz2
COMPONENT_ARCHIVE_HASH=	\
  sha256:9c5ce1e33d2463fb1a42dd04daacbc22104e57676e2204e3d66b1ef54b88ebf2
COMPONENT_ARCHIVE_URL= \
  https://www.hdfgroup.org/package/bzip2/?wpdmdl=4300
COMPONENT_LICENSE=        NCSA

include $(WS_MAKE_RULES)/prep.mk
include $(WS_MAKE_RULES)/configure.mk
include $(WS_MAKE_RULES)/ips.mk

CONFIGURE_OPTIONS  +=		CFLAGS="$(CFLAGS) -D_LARGEFILE_SOURCE -D__EXTENSIONS__"
CONFIGURE_OPTIONS  +=		--includedir=$(CONFIGURE_PREFIX)/include/hdf5
CONFIGURE_OPTIONS  +=		--disable-static
CONFIGURE_OPTIONS  +=		--enable-fortran
CONFIGURE_OPTIONS  +=		--enable-cxx

build:		$(BUILD_32_and_64)

install:	$(INSTALL_32_and_64)

test:	$(TEST_32_and_64)

REQUIRED_PACKAGES += library/zlib
REQUIRED_PACKAGES += system/library
REQUIRED_PACKAGES += system/library/g++-4-runtime
REQUIRED_PACKAGES += system/library/gcc-4-runtime
REQUIRED_PACKAGES += system/library/gfortran-4-runtime
REQUIRED_PACKAGES += system/library/math
