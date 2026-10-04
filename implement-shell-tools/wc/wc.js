const fs = require("fs");
const path = require("path");

// Count lines, words and bytes in a file
function countFile(filename) {
    const data = fs.readFileSync(filename);

    // Convert the file to text for counting lines and words
    const text = data.toString("utf8");

    const lines = text.split("\n").length - 1;
    const words = text.trim().split(/\s+/).filter(Boolean).length;
    const bytes = data.length;

    return {
        lines,
        words,
        bytes
    };
}

// Expand simple wildcards such as sample-files/*
function expandFiles(filename) {
    if (!filename.includes("*") && !filename.includes("?")) {
        return [filename];
    }

    const directory = path.dirname(filename);
    const pattern = path.basename(filename);

    // Escape regex characters, then turn * and ? into regex equivalents
    const regexPattern = "^" +
        pattern
            .replace(/[.+^${}()|[\]\\]/g, "\\$&")
            .replace(/\*/g, ".*")
            .replace(/\?/g, ".") +
        "$";

    const regex = new RegExp(regexPattern);

    try {
        return fs.readdirSync(directory)
            .filter(file => regex.test(file))
            .map(file => path.join(directory, file));
    } catch (error) {
        return [];
    }
}

function main() {
    // Get command-line arguments
    let parts = process.argv.slice(2);

    // Remove "wc" if it was included
    if (parts[0] === "wc") {
        parts = parts.slice(1);
    }

    // Work out which flags were used
    const showLines = parts.includes("-l");
    const showWords = parts.includes("-w");
    const showBytes = parts.includes("-c");

    // If no flags were given, show all three
    let displayLines = showLines;
    let displayWords = showWords;
    let displayBytes = showBytes;

    if (!showLines && !showWords && !showBytes) {
        displayLines = true;
        displayWords = true;
        displayBytes = true;
    }

    // Remove flags so only filenames remain
    const files = parts.filter(part => {
        return !["-l", "-w", "-c"].includes(part);
    });

    // Expand wildcards
    const expandedFiles = [];

    for (const filename of files) {
        const matches = expandFiles(filename);

        if (matches.length > 0) {
            expandedFiles.push(...matches);
        } else {
            // Keep the original filename so we can show the error
            expandedFiles.push(filename);
        }
    }

    // Keep track of totals
    let totalLines = 0;
    let totalWords = 0;
    let totalBytes = 0;

    for (const filename of expandedFiles) {
        try {
            const {
                lines,
                words,
                bytes
            } = countFile(filename);

            const output = [];

            if (displayLines) {
                output.push(lines);
                totalLines += lines;
            }

            if (displayWords) {
                output.push(words);
                totalWords += words;
            }

            if (displayBytes) {
                output.push(bytes);
                totalBytes += bytes;
            }

            output.push(filename);

            console.log(output.join(" "));
        } catch (error) {
            if (error.code === "ENOENT") {
                console.error(`wc: ${filename}: No such file or directory`);
            } else {
                console.error(`wc: ${filename}: ${error.message}`);
            }
        }
    }

    // Print total when there is more than one file
    if (expandedFiles.length > 1) {
        const output = [];

        if (displayLines) {
            output.push(totalLines);
        }

        if (displayWords) {
            output.push(totalWords);
        }

        if (displayBytes) {
            output.push(totalBytes);
        }

        output.push("total");

        console.log(output.join(" "));
    }
}

main();
