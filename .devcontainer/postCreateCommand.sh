#!/bin/bash

sh -c "$(curl -LsSf https://astral.sh/uv/0.6.3/install.sh)"
uv sync --frozen --dev
