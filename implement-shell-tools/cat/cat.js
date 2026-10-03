const fs = require("fs");
const path = require("path");

const parts = process.argv.slice(2);

let option = null;
let pattern;

if (parts.length >= 1 && (parts[0] === "-n" || parts[0] === "-b")) {
    option = parts[0];
    pattern = parts[1];
} else {
    pattern = parts[0];
}

if (!pattern) {
    console.log("cat: missing file operand");
    process.exit();
}

const directory = path.dirname(pattern);
const filenamePattern = path.basename(pattern);

let files;

if (filenamePattern.includes("*")) {
    const [before, after] = filenamePattern.split("*");

    files = fs.readdirSync(directory)
        .filter(file => file.startsWith(before) && file.endsWith(after))
        .map(file => path.join(directory, file))
        .sort();
} else {
    const fullPath = path.join(directory, filenamePattern);

    if (!fs.existsSync(fullPath)) {
        console.log(`cat: ${pattern}: No such file or directory`);
        process.exit();
    }

    files = [fullPath];
}

let lineNumber = 1;

for (const filename of files) {
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

