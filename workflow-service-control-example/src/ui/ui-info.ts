// Copyright © 2021 Cisco Systems, Inc.  All Rights Reserved.
//
// This is the UI information file to provide build details to the platform.
// It is used to populate component versions, as well as define a way to put a cache breaker
// on the file load.

class UIInfo {
  buildDate = '__UI_BUILDDATE__';
  buildVersion = '__BUILD_VERSION__';
  servicepackName = '__SERVICE_PACK_NAME__';
  buildNumber = '__BUILD_NUMBER__';
  versionId = '__BUILD_VERSION_ID__';
}

export { UIInfo as infoClass };
