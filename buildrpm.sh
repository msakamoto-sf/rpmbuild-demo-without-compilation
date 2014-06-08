#!/bin/sh
WORK_DIR=`pwd`
BUILD_NAME=helloworld
BUILD_SPEC=${BUILD_NAME}.spec
BUILD_TAR=${BUILD_NAME}.tar.gz
BUILD_DIR=${WORK_DIR}/rpmbuild
BUILD_TAR_PATH=${WORK_DIR}/rpmbuild/SOURCES/${BUILD_TAR}

/bin/rm -rf ${BUILD_DIR}
/bin/mkdir -p ${BUILD_DIR}/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
/bin/tar czf ${BUILD_TAR} ${BUILD_NAME}/
/bin/mv ${BUILD_TAR} ${BUILD_TAR_PATH}
/usr/bin/rpmbuild --define "_topdir ${BUILD_DIR}" -bb ${BUILD_SPEC}
