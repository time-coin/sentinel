#!/bin/bash
set -evx

mkdir ~/.dashcore

# safety check
if [ ! -f ~/.timecore/.time.conf ]; then
  cp share/time.conf.example ~/.timecore/time.conf
fi
