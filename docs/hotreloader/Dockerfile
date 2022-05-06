FROM coppit/inotify-command

RUN apk add  --update --no-cache make python3
RUN ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip

# TODO: Gather versions from pyproject.toml
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install sphinx sphinxcontrib-napoleon furo