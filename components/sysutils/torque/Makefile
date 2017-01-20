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
# Copyright 2016 Aurelien Larcher
#

include ../../../make-rules/shared-macros.mk

COMPONENT_NAME=       torque
COMPONENT_VERSION=    6.1.0
COMPONENT_SUMMARY=    TORQUE Resource Manager
COMPONENT_PROJECT_URL=http://www.adaptivecomputing.com/
COMPONENT_FMRI=       system/torque
COMPONENT_CLASSIFICATION=System/Services
COMPONENT_SRC=        $(COMPONENT_NAME)-$(COMPONENT_VERSION)
COMPONENT_ARCHIVE=    $(COMPONENT_SRC).tar.gz
COMPONENT_ARCHIVE_URL= \
    http://wpfilebase.s3.amazonaws.com/torque/$(COMPONENT_ARCHIVE)
COMPONENT_ARCHIVE_HASH= \
    sha256:c93585f024720df3e3e360eeb25df4990a9ed85362ac3e7adec6c7a13f8e62d2
#    sha256:a9a57ed03cfc51b972e11c94ce22bc62588dca396a344cb64831185bdacf4732
COMPONENT_LICENSE=    GPLv2

include $(WS_MAKE_RULES)/prep.mk
include $(WS_MAKE_RULES)/configure.mk
include $(WS_MAKE_RULES)/ips.mk

PATH=/usr/gnu/bin:/usr/bin

COMPONENT_PREP_ACTION= ( cd $(@D); \
        libtoolize --force --copy \
	&& aclocal \
	&& autoheader \
	&& automake --foreign --add-missing --force-missing --copy \
	&& autoconf )

CFLAGS+= -D_XOPEN_SOURCE=600 -D__EXTENSIONS__
CONFIGURE_OPTIONS+= --sysconfdir=$(ETCDIR)/torque

build:    $(BUILD_32)

install:  $(INSTALL_32)

test:    $(TEST_32)

