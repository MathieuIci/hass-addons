#!/bin/bash

# Depending on if Radicale is currently running with SSL, use an appropriate cURL command to see if Radicale is responsive.

if pgrep -f "/usr/bin/radicale.*--server-ssl true.*" > /dev/null; then
    curl --fail --silent --show-error --insecure https://localhost:5232/.web/ | grep "Radicale Web Interface" || exit 1;
else
    curl --fail --silent --show-error http://localhost:5232/.web/ | grep "Radicale Web Interface" || exit 1;
fi
exit 0
