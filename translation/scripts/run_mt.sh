#!/bin/bash
# Environment:
# pyenv 3.11.0 + venv

export PYTHONPATH="~/Gemini/gem_venv/lib/python3.11/site-packages/"
echo "PYTHONPATH: " ${PYTHONPATH}
# Set the path to the Markdown file list
filelist="./filelist.txt"

# Set the path to the Python translation script
script="./gemini_trans_md.py"

# Set the output directory for translated files
output_dir="../ja"

# Check if the output directory exists, create it if not
if [ ! -d "$output_dir" ]; then
  mkdir -p "$output_dir"
fi

# Iterate over each file in the list
while read -r filepath; do
  echo "Translating "${filename}" ...."
  # Get the filename without the extension
  base_file=`basename ${filepath}`
  parent_dirpath=`echo ${filepath}|sed -E "s/\.\.\///g"` 
  #filename_wo_ext="${base_file%.*}"
  filename_wo_ext="${parent_dirpath%.*}"

  # Construct the input and output file paths
  input_file="${filepath}"
  output_file="${output_dir}/${parent_dirpath}_ja.md"

  echo "output file:"${output_file}

  # Run the translation script
  python "${script}" "${input_file}" "${output_file}"

  echo "Translated ${filepath} to ${output_file}"
done < "${filelist}"