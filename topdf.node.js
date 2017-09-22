const exec = require('child_process').exec
const markdownpdf = require("markdown-pdf")
const fs = require("fs")

exec('mkdocs2pandoc > robin-deguzman.pd', function (err, stdout, stderr) {
    if (!err) {
        markdownpdf().from('robin-deguzman.pd').to('robin-deguzman.pdf')
    } else {
        console.log(err)
    }
})
