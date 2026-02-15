#!/bin/bash

sh -c "$(curl -LsSf https://astral.sh/uv/install.sh)"
uv sync --frozen --dev
