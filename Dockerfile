FROM python:3.9.4-alpine

RUN apk update \
   && apk add --no-cache build-base
   
RUN python -m pip install --upgrade pip

RUN adduser -D janus
USER janus
WORKDIR /home/janus

ENV PATH="/home/janus/.local/bin:${PATH}"

COPY --chown=janus:janus . ./

RUN pip install .

# CMD ["janus-sentinel", "/home/janus/conf/janus-sentinel.yml"]
CMD ["janus-proxy", "/home/janus/conf/janus-proxy.yml"]