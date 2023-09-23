#!/usr/bin/env bash

# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

set -e

# Define the URL directly in the script
PRESIGNED_URL="YOUR_URL_HERE"

TARGET_FOLDER="."             # where all files should end up
mkdir -p ${TARGET_FOLDER}

# Define the list of models to download
MODEL_SIZE="7B,13B,70B,7B-chat,13B-chat,70B-chat"

echo "Downloading LICENSE and Acceptable Usage Policy"
wget --continue ${PRESIGNED_URL/'*'/"LICENSE"} -O ${TARGET_FOLDER}"/LICENSE"
wget --continue ${PRESIGNED_URL/'*'/"USE_POLICY.md"} -O ${TARGET_FOLDER}"/USE_POLICY.md"

echo "Downloading tokenizer"
wget --continue ${PRESIGNED_URL/'*'/"tokenizer.model"} -O ${TARGET_FOLDER}"/tokenizer.model"
wget --continue ${PRESIGNED_URL/'*'/"tokenizer_checklist.chk"} -O ${TARGET_FOLDER}"/tokenizer_checklist.chk"
CPU_ARCH=$(uname -m)
if [ "$CPU_ARCH" = "arm64" ]; then
    (cd ${TARGET_FOLDER} && md5 tokenizer_checklist.chk)
else
    (cd ${TARGET_FOLDER} && md5sum -c tokenizer_checklist.chk)
fi

for m in ${MODEL_SIZE//,/ }
do
    # Rest of the script remains the same
    # ...
done
