# Start dev server
source env/Scripts/activate
mkdocs serve

# Convert to PDF
source env/Scripts/activate
node topdf --src robin-deguzman.md


