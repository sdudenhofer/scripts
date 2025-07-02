#! /bin/bash

mkdir app/
echo "Create src directory"

mkdir app/core/
echo "Created core folder"

mkdir app/api/v1
echo "Created location for api version 1"

mkdir app/db/
echo "Created db data location"

mkdir app/schemas/
echo "Created schema location"

mkdir app/services
echo "Create services location"

mkdir app/tests
echo "Base test folder created"


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
