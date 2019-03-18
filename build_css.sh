set -e
set -x
export NPATH=`pwd`/node_modules
cd ./static/pcss && find *.pcss | grep -v "^_" | xargs node ${NPATH}/postcss-cli/bin/postcss -d ../css --no-map "$@" --ext .css
echo '--------- BUILD COMPLETED ---------'
