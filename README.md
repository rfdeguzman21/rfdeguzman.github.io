# Anaconda
```
conda create -n githubresume python=2.7.15
conda activate githubresume
conda deactivate githubresume

conda install pandoc
```

# Start dev server
```
conda activate githubresume
mkdocs serve
```

# Deploy changes to github
```
conda activate githubresume
mkdocs gh-deploy
```

# Convert to resume
```
pandoc -s -o src/downloads/robindeguzman_resume.docx \
  src/index.md src/experiences.md src/skills.md src/projects.md src/education.md

# or use
bash create_resume.sh
```

