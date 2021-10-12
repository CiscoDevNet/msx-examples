#!/bin/bash
# Supported ENV variables:
# * SERVICE_JAR: Name of the jar file to execute (required)
# * JAVA_OPTS: A set of options that will be passed to the java command (optional)
#
# Arguments to this script will be passed as arguments to the Java application.

if [ "$SERVICE_JAR" = "" ]; then
    echo "Environment variable SERVICE_JAR not set or empty"
    exit 1
fi

JAVA_OPTS=${JAVA_OPTS:-" \\
  -Xss512K \\
  -Xms128M \\
  -Xmx256M \\
  -XX:MaxMetaspaceSize=128M \\
  -XX:MaxRAMPercentage=75 -XX:MinRAMPercentage=50 \\
  -XX:MaxHeapFreeRatio=15 -XX:MinHeapFreeRatio=10 \\
  -XX:ReservedCodeCacheSize=64M \\
  -XX:+UseStringDeduplication \\
  -XX:+HeapDumpOnOutOfMemoryError \\
  -XX:HeapDumpPath=/data/conf/dump.hprof"}

CMD="exec java -Djavax.net.ssl.trustStore=/keystore/msxtruststore.jks $@ $JAVA_OPTS -jar /service/$SERVICE_JAR"

echo "$CMD"
eval "$CMD"