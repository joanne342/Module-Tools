const fs = require("fs");

const parts = process.argv.slice(2);

let option = null;
let files = [];

if (parts[0] === "-n" || parts[0] === "-b") {
    option = parts[0];
    files = parts.slice(1);
} else {
    files = parts;
}

if (files.length === 0) {
    console.log("cat: missing file operand");
    process.exit();
}

let lineNumber = 1;

for (const filename of files) {
    if (!fs.existsSync(filename)) {
        console.log(`cat: ${filename}: No such file or directory`);
        continue;
    }

    const content = fs.readFileSync(filename, "utf8");
    const lines = content.split(/\r?\n/);

    if (lines[lines.length - 1] === "") {
        lines.pop();
    }

    for (const line of lines) {
        if (option === "-n") {
            console.log(`${String(lineNumber).padStart(6)}\t${line}`);
            lineNumber++;
        } else if (option === "-b") {
            if (line !== "") {
                console.log(`${String(lineNumber).padStart(6)}\t${line}`);
                lineNumber++;
            } else {
                console.log();
            }
        } else {
            console.log(line);
        }
    }
}

