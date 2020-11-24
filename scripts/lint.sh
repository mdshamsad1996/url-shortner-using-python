#!/usr/bin/env bash

EXIT_CODE=0

pylint url_shortner || EXIT_CODE=1

pycodestyle url_shortner || EXIT_CODE=1

exit ${EXIT_CODE}
