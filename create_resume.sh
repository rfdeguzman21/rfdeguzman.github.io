#!/bin/sh

base=$(dirname $0)
footnote=$base/resume.footnote.md

# Create the footnote
echo '' > $footnote
echo '> ----------------  ' >> $footnote
echo "> Generated using pandoc $(pandoc --version | grep -m 1 pandoc | awk '{print $2}')  " >> $footnote
echo "> Last update: $(date '+%B %d, %Y')  " >> $footnote

# Create the docx
pandoc -s -o $base/src/downloads/RobinDeGuzmanCv.docx \
  $base/src/index.md \
  $base/src/experiences.md \
  $base/src/projects.md \
  $base/src/certificates.md \
  $base/src/skills.md \
  $base/src/education.md \
  $footnote
