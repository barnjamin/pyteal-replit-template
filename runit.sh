#!/bin/bash

if [ ! -d ".venv" ]
then
  echo "Performing initial setup"
  echo "Creating virtural env"
  python -m venv .venv
  echo "Sourcing venv"
  source .venv/bin/activate
  echo "Installing pyteal"
  pip install "git+https://github.com/algorand/pyteal@feature/abi"
  deactivate
fi

source .venv/bin/activate
python main.py

