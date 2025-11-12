# Usa imagem base com Java 21 (Debian bookworm)
FROM mcr.microsoft.com/devcontainers/java:1-21-bookworm

# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/java:1-21-bookworm

# Instala Maven e dependências do Firefox
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      maven \
      wget \
      tar \
      xz-utils \
      libgtk-3-0 \
      libx11-xcb1 \
      libdbus-glib-1-2 \
      libxt6 \
      libxcomposite1 \
      libxrandr2 \
      libasound2 \
      libnss3 \
      libxdamage1 \
      libpango-1.0-0 \
      libpangocairo-1.0-0 \
      libcairo2 \
      libatk1.0-0 \
      libatk-bridge2.0-0 \
      ca-certificates && \
    rm -rf /var/lib/apt/lists/*


# Instala dependências mínimas para rodar o Firefox ESR e o Selenium
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      wget \
      tar \
      xz-utils \
      libgtk-3-0 \
      libx11-xcb1 \
      libdbus-glib-1-2 \
      libxt6 \
      libxcomposite1 \
      libxrandr2 \
      libasound2 \
      libnss3 \
      libxdamage1 \
      libpango-1.0-0 \
      libpangocairo-1.0-0 \
      libcairo2 \
      libatk1.0-0 \
      libatk-bridge2.0-0 \
      ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# 🦊 Baixa e instala o Firefox ESR (.tar.xz oficial da Mozilla)
RUN wget -O /tmp/firefox.tar.xz "https://download.mozilla.org/?product=firefox-esr-latest&os=linux64&lang=en-US" && \
    tar -xf /tmp/firefox.tar.xz -C /opt/ && \
    ln -sf /opt/firefox/firefox /usr/bin/firefox && \
    rm /tmp/firefox.tar.xz

# 🧩 Baixa e instala o geckodriver mais recente
RUN GECKO_VER=$(wget -qO- "https://api.github.com/repos/mozilla/geckodriver/releases/latest" | grep '"tag_name"' | sed -E 's/.*"v([^"]+)".*/\1/') && \
    wget -O /tmp/geckodriver.tar.gz "https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VER}/geckodriver-v${GECKO_VER}-linux64.tar.gz" && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz

# Define variáveis de ambiente Java
ENV JAVA_HOME=/usr/lib/jvm/msopenjdk-21
ENV PATH="${PATH}:${JAVA_HOME}/bin"
