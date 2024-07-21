#!/bin/bash

# Set the path to the Markdown file list
filelist="./filelist.txt"

# Initialize word and line count variables
total_words=0
total_lines=0

# Iterate over each file in the list
while read -r filename; do
  # Get the filename without the extension
  #base_filename="${filename%.*}"

  # Count words and lines for the current file
  word_count=$(wc -w "$filename" | awk '{print $1}')
  line_count=$(wc -l "$filename" | awk '{print $1}')

  # Display individual file counts
  echo "$filename: $word_count words, $line_count lines"

  # Update total counts
  total_words=$((total_words + word_count))
  total_lines=$((total_lines + line_count))
done < "$filelist"

# Display total counts
echo "Total: $total_words words, $total_lines lines"
