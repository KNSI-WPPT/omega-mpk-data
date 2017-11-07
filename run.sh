#!/bin/bash

set -u

passfile="pwdfile"

if [[ -r $passfile ]] ; then
  # Prepare python environment
  virtualenv -p python3 ohm
  set +o nounset
  . ./ohm/bin/activate
  set -o nounset
  pip install -r requirements.txt

  # Export variables required by crawlers
  . "$passfile"
  export DB_CONNECTION=${DB_CONNECTION:?}

  # Start data crawlers
  python start.py

  deactivate
else
  echo "Password file not found or not readable."
  exit 1
fi
