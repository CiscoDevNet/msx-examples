#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
#!/bin/bash

set -e

NODE_OPTIONS=--max_old_space_size=8192
export NODE_OPTIONS

printf '\nBundling main app with Rollup\n'
PATH="$CUR_DIR/node_modules/.bin:$PATH"
export PATH
if [ -f "$CUR_DIR/package.json" ] ; then
	npm install
fi
rollup --config rollup.config.js
