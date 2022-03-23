#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
#!/bin/bash

set -e

NODE_OPTIONS=--max_old_space_size=8192
export NODE_OPTIONS

CUR_DIR=`pwd`

if [ -d "./build" ] ; then
	echo "Cleaning up old build"
	rm -rf "./build"
fi
mkdir -p ./build

printf '\nUpdating dependencies\n'
npm install

printf '\nBundling main app with Rollup\n'
PATH="$CUR_DIR/node_modules/.bin:$PATH"
export PATH
if [ -f "$CUR_DIR/package.json" ] ; then
	npm install
fi
rollup --config rollup.config.js

docker build -t workflowexecutor:1.0.0 .
docker save  workflowexecutor:1.0.0 | gzip > build/slmimage-workflowexecutor-1.0.0.tar.gz

cd build

ZIP=`which zip`

if [ -f "$ZIP" ] ; then 
	$ZIP -yr tcui_package.zip *
fi

TAR=`which tar`

if [ -f "$TAR" ] ; then 
	$TAR --exclude=./tcui_package.zip --exclude=./services -czf  workflowexecutor_slm_deployable.tar.gz *
	rm -f slmimage-workflowexecutor-1.0.0.tar.gz
fi

cd "$CUR_DIR"