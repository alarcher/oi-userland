#
# This file and its contents are supplied under the terms of the
# Common Development and Distribution License ("CDDL"), version 1.0.
# You may only use this file in accordance with the terms of version
# 1.0 of the CDDL.
#
# A full copy of the text of the CDDL should have accompanied this
# source.  A copy of the CDDL is also available via the Internet at
# http://www.illumos.org/license/CDDL.
#

#
# Copyright 2015 Aur√elien Larche.  All rights reserved.
#

include ../../make-rules/shared-macros.mk

COMPONENT_NAME= clang-upc

COMPONENT_VERSION= 3.5.1
COMPONENT_REVISION=0
COMPONENT_SUMMARY= Extension of Clang/LLVM to support Unified Parallel C
COMPONENT_PROJECT_URL = https://clangupc.github.io/
COMPONENT_SRC= $(COMPONENT_NAME)-$(COMPONENT_VERSION)-$(COMPONENT_REVISION)
COMPONENT_ARCHIVE= $(COMPONENT_SRC).tar.gz
COMPONENT_ARCHIVE_HASH= \
  sha256:9a4fe6dbe878d7b6d66d6876a8b9fd4aa4d3dd7ecfc92bd9c4acd0c8e2ce82fe
COMPONENT_ARCHIVE_URL= \
  http://upc.lbl.gov/download/clang-upc/$(COMPONENT_ARCHIVE)

include ../../make-rules/prep.mk
include ../../make-rules/configure.mk
include ../../make-rules/ips.mk

# GNU install should be first
PATH=/usr/gnu/bin:/usr/sbin:/usr/bin:/usr/bin/perl5

PATCH_LEVEL=0

CC=/usr/bin/gcc
CXX=/usr/bin/g++
CONFIGURE_PREFIX=/usr/clang-upc/3.5

CONFIGURE_OPTIONS+= --enable-static

COMPONENT_TEST_TARGETS = check-all
COMPONENT_TEST_ENV += PATH=/usr/gnu/bin:/usr/bin

COMPONENT_POST_INSTALL_ACTION = \
for file in `echo $(PROTO_DIR)/$(CONFIGURE_PREFIX)/bin/*`; do \
elfedit -e 'dyn:runpath $$ORIGIN/../lib' $$file ; \
done
# && \
#for file in `echo $(PROTO_DIR)/$(CONFIGURE_PREFIX)/lib/*.so`; do \
#elfedit -e 'dyn:delete RUNPATH' $$file ; \
#elfedit -e 'dyn:delete RPATH' $$file ; \
#done

build: $(BUILD_64)

install: $(INSTALL_64)

test: $(TEST_64)
