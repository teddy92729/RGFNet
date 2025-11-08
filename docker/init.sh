#!/bin/bash

set -ex
trap 'exit 0' SIGTERM

if [ -z "$AUTHORIZED_KEYS_FILE" ]; then
    echo "Error: AUTHORIZED_KEYS_FILE is not set."
    exit 1
fi

mkdir -p /root/.ssh
cp "$AUTHORIZED_KEYS_FILE" /root/.ssh/authorized_keys
chmod 644 /root/.ssh/authorized_keys

if [ $? -ne 0 ]; then
    echo "Error: Failed to copy public key file."
    exit 1
fi
echo "Public key copied successfully."

if [ "$SSH_KEY_FILE" ]; then
    cp "$SSH_KEY_FILE" /root/.ssh/id
    chmod 600 /root/.ssh/id
    git config --system core.sshCommand "ssh -i /root/.ssh/id -o IdentitiesOnly=yes"
    echo "SSH key configured for Git."
fi

# Display environment variables for debugging
env

echo "Starting SSH daemon..."
mkdir -p /run/sshd
chmod 755 /run/sshd
exec /usr/sbin/sshd -D 