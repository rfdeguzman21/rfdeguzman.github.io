# Anaconda
```
conda create -n githubresume python=2.7.15
conda activate githubresume
conda deactivate githubresume

conda install pandoc
```

# Start dev server
source activate githubresume
mkdocs serve

# Deploy changes to github
source env/Scripts/activate
mkdocs gh-deploy

# Convert to PDF -- delete if pandoc works
source env/Scripts/activate
node topdf.node.js --src robin-deguzman.md


# Convert to resume
```
pandoc -s -o src/downloads/robindeguzman_resume.docx src/index.md src/experiences.md src/skills.md src/projects.md src/education.md
```

