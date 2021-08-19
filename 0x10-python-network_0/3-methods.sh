#!/bin/bash
curl '$1' -s | grep 'Allow' | cut -d ' ' -f2-
