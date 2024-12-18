ARG BUILD_FROM
FROM $BUILD_FROM

# https://docs.docker.com/engine/reference/builder/

ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

COPY rootfs /

RUN apk add --no-cache --virtual=build-dependencies \
        gcc \
        libffi-dev \
        musl-dev \
        python3-dev \
        py-pip \
    && apk add --no-cache \
        curl \
        python3 \
        shadow \
        su-exec \
        tzdata \
        py3-setuptools \
        py3-pip \
        py3-requests \
        py3-wheel \
        py3-bcrypt \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install radicale passlib[bcrypt] \
    && python3 -m pip install /usr/local/lib/python/radicale_homeassistant_password_auth/ \
    && apk del --purge build-dependencies

#TODO Find a way to use the config's value in the below curl command
#HEALTHCHECK --interval=120s --timeout=10s --start-period=5s --retries=3 \
#    CMD curl --fail https://localhost:5232 || exit 1
