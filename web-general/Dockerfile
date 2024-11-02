FROM python:3.8.19

# os setup
RUN apt-get update && apt-get -y install \
  python3-dev \
  python3-lxml \
  build-essential \
  libssl-dev \
  libffi-dev \
  libxml2-dev \
  libxslt1-dev \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/torscraper/web
WORKDIR /opt/torscraper/web

# Copy requirements first
COPY requirements.txt /opt/torscraper/web/requirements.txt

# Update pip and install fixed versions of problematic packages
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir \
    attrs==21.4.0 \
    zope.interface==5.4.0 \
    coinaddr==1.0.1

# Install other requirements
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade requests

# Install spacy model
RUN python -m spacy download en_core_web_lg

# Copy application files
COPY . /opt/torscraper/web/

# Set permissions for entrypoint script
RUN chmod +x /opt/torscraper/web/docker-entrypoint.sh

CMD ["/opt/torscraper/web/docker-entrypoint.sh"]