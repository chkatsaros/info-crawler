FROM kalilinux/kali-rolling AS build-deps 
RUN set -eux; \
    apt update -y; \
    apt install unzip -y --no-install-recommends; \
    rm -rf /var/lib/apt/lists/* 

FROM build-deps AS build 
WORKDIR /build
ADD https://github.com/owasp-amass/amass/releases/download/v3.23.2/amass_linux_amd64/zip .
RUN set -eux; \
    unzip amass_linux_amd64; \
    ./amass_linux_amd64/amass --version

FROM kalilinux/kali-rolling AS runtime
RUN set -eux; \
    apt update -y; \
    apt install emailharvester theharvester -y --no-install-recommends; \
    rm -rf /var/lib/apt/lists/* 
COPY --from=build /build/amass_Linux_amd64/amass /usr/local/bin/amass

# InfoCrawler installation
WORKDIR /app
COPY . .
RUN set -eux; \
    python3 -m venv .venv; \
    .venv/bin/pip install -r requirements.txt

ENV PATH="/app/.venv/bin:${PATH}"
ENTRYPOINT [ "/app/info-crawler.py" ]
CMD ["--help"]

