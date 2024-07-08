#!/bin/zsh

# Check if conda is installed
if command -v conda &> /dev/null
then
    # Check if conda is initialized by listing environments
    if conda info --envs &> /dev/null
    then
        echo "conda test OK"
    else
        echo "Conda is installed but not initialized."
    fi
else
    echo "Conda is not installed."
fi
