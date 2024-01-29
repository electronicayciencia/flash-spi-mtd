#!/bin/bash
# Unmount data filesystem.

set -e
set -u

sync /tmp/secret
umount /tmp/secret
rmmod block2mtd

