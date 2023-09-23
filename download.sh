#!/usr/bin/env bash

# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

set -e

# Define the URL directly in the script
PRESIGNED_URL="https://download.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoidTFzZHA3Y2VoMTlrcHB5Z3d1c2c1ajBsIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvZG93bmxvYWQubGxhbWFtZXRhLm5ldFwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY5NTU5MDA3MX19fV19&Signature=lVXZyMAe4Bmx%7EMzBy0V9CskbUTTu%7ErjzyC8eRQIUg8iqDngo7aNiqjdTGLFKfoO2XJuYUHmui7PBCf6PD9HYos2UIYnnbLKSaCWOcLB3DXIe41bEbo40C-RUN2WFM5lWja7V8LmbWo%7Eu1vhM5%7EczMsNZ8oA88zgluTX51xml769pnrpiPsB0NyEkBLxi093B5spzqCXjQCMx5142xJvyoHZUpaOu8HtjyszIzq-6dZi-Op4WqiMSW6FPiykBySneFCx3NYsjp%7EECPQneea-dAvUL-6ox%7EDboKi5PAPvfgxMrt9tWF%7ENag5JC6Cdd06CDSjLwJe7%7ELDZYWYTPogI%7E6Q__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=6739864882773456"

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
