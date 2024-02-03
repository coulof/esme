# Use an official Ubuntu base image
FROM ubuntu:latest

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install TeX Live and some basic tools. This line installs the full TeX Live scheme.
# You can replace `texlive-full` with specific packages like `texlive-base` plus any
# additional LaTeX packages you require to reduce the image size.
RUN apt-get update && \
    apt-get install -y texlive-full && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY esme /usr/local/share/texmf/tex/latex/esme
COPY esmeDL /usr/local/share/texmf/tex/latex/esmeDL
RUN texhash

# Set the working directory to /data
WORKDIR /data

# By default, run a shell. You can change this to your specific build command
# For example, to compile a LaTeX file: CMD ["pdflatex", "yourfile.tex"]
CMD ["/bin/bash"]

