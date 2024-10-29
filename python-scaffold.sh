#! /bin/bash

mkdir src/
echo "Create src directory"

mkdir data/
echo "Create data directory"

mkdir data/raw
echo "Create location for raw data"

while true; do
  read -p "Initialize UV?" yesno
  case $yesno in
  [Yy]*)
    echo "Initializing uv..."
    uv init
    ;;
  [Nn]*)
    echo "skipping uv initialization..."
    exit
    ;;
  *) echo "Must answer either yes or no" ;;
  esac
done
exit
