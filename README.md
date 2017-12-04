# Start dev server
source env/Scripts/activate
mkdocs serve

# Deploy changes to github
source env/Scripts/activate
mkdocs gh-deploy

# Convert to PDF
source env/Scripts/activate
node topdf.node.js --src robin-deguzman.md


