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

LABEL \
    io.hass.name="Radicale" \
    io.hass.description="Radicale is a small but powerful CalDAV (calendars, todo-lists) and CardDAV (contacts) server" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    org.label-schema.description="Radicale is a small but powerful CalDAV (calendars, todo-lists) and CardDAV (contacts) server" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="Radicale" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="" \
    org.label-schema.usage="" \
    org.label-schema.vcs-ref=${BUILD_REF}
