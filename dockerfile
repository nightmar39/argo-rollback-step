FROM python:3.10.9-slim
RUN apt-get update -y && apt-get install curl bash -y

RUN curl -L "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" -o /usr/local/bin/kubectl 

RUN chmod +x /usr/local/bin/kubectl \ 
    && curl -sSL https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64 -o /usr/local/bin/argocd \
    && chmod +x /usr/local/bin/argocd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY app /

ENTRYPOINT /bin/bash