FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu20.04

RUN /bin/sh -ex;\
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y ssh git mesa-utils tmux; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*; 

RUN /bin/sh -ex;\
    wget -qO- https://astral.sh/uv/install.sh | sh; \
    echo "source /root/.local/bin/env" >> /root/.bashrc;

RUN /bin/sh -ex; \
    # SSH 設定
    sed -i \
    -e "s/#Port.*/Port 22/" \
    -e "s/#PermitRootLogin.*/PermitRootLogin yes/" \
    -e "s/#PasswordAuthentication.*/PasswordAuthentication no/" \
    -e "s/#PubkeyAuthentication.*/PubkeyAuthentication yes/" \
    -e "s/#PermitEmptyPasswords.*/PermitEmptyPasswords no/" \
    -e "s/#UsePAM.*/UsePAM yes/" \
    -e "s/#UseDNS.*/UseDNS no/" \
    -e "s/#ChallengeResponseAuthentication.*/ChallengeResponseAuthentication no/" /etc/ssh/sshd_config;

EXPOSE 22

COPY --chown=root:root --chmod=755 ./init.sh /init.sh

WORKDIR /root

ENV PATH="/root/.local/bin:${PATH}"

RUN /bin/sh -ex;\
    git clone https://github.com/teddy92729/RGFNet.git; \
    cd RGFNet; \
    uv python install 310; \
    uv venv; \
    uv pip install -e .; \
    uv pip install timm lightning mamba-ssm einops;


CMD ["sh", "-c", "/init.sh"]
