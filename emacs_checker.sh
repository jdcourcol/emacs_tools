#!/bin/bash
SCRIPT=$(greadlink -f "$0")
SCRIPTPATH=`dirname ${SCRIPT}`
echo "script path" $SCRIPTPATH > /tmp/echo.txt
${SCRIPTPATH}/epylint.py "$1" ${SCRIPTPATH}/pylintrc $VIRTUAL_ENV 2>/dev/null
$VIRTUAL_ENV/bin/pep8 --config=${SCRIPTPATH}/pep8rc --repeat "$1"
true
