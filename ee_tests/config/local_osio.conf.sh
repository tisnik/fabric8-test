# Test config for running e2e tests against remote osio
# openshift.io credentials
export OSIO_USERNAME="${OSIO_USERNAME:-}"
export OSIO_PASSWORD="${OSIO_PASSWORD:-}"
export OSIO_URL="${OSIO_URL:-https://openshift.io}"

# github
export GITHUB_USERNAME="${GITHUB_USERNAME:-}"

# test params
export RELEASE_STRATEGY="${RELEASE_STRATEGY:-releaseStageApproveAndPromote}"
export QUICKSTART_NAME="${QUICKSTART_NAME:-'vertxHttp'}"



