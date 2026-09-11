#!/bin/bash
set -e
cd "$(dirname "$0")"
source venv/bin/activate

export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

exec python odoo/odoo-bin -c odoo.dev.conf "$@"