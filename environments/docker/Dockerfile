# syntax=docker/dockerfile:1.3-labs
FROM selenium/standalone-firefox:92.0

USER root

RUN <<EOF
apt-get update
# Japanese locale
apt-get install -y --no-install-recommends language-pack-ja
# Python installation dependencies
apt-get install -y --no-install-recommends \
  build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev
apt-get clean
rm -rf /var/lib/apt/lists/*
cd tmp
wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tar.xz
tar xJf Python-3.8.12.tar.xz
cd Python-3.8.12
./configure
make
make install
cd ..
rm -rf Python-3.8.12.tar.xz Python-3.8.12
python3.8 -m pip install --no-cache-dir helium~=3.0.8
EOF

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja

USER 1200
