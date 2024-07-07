#!/usr/bin/env bash
#
# Ensure shell scripts conform to shellcheck.
#

set -o errexit
set -o pipefail
set -o nounset

readonly DEBUG=${DEBUG:-unset}
if [ "${DEBUG}" != unset ]; then
    set -x
fi

WORKDIR=$(realpath .)

SHELLCHECK_COMMAND=$(which shellcheck 2> /dev/null)
if [ -z "$SHELLCHECK_COMMAND" ]; then
  SHELLCHECK_COMMAND="docker run --rm -v $WORKDIR:$WORKDIR -w $WORKDIR koalaman/shellcheck:stable"
fi

$SHELLCHECK_COMMAND $@
