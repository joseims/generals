#!/bin/bash
mkdir -p /tmp/copy
/
if [ $1 = '-c' ]
then
    rm -fr /tmp/copy/copied_structure
    cp -r $source /tmp/copy/copied_structure
    filename=$(basename $source)
    echo $filename > /tmp/copy/filename
    echo "File $filename was copied"
elif [ $1 = '-p' ]
then
    source=$source"/"$(cat /tmp/copy/filename)
    cp /tmp/copy/copied_structure $source
        echo "File $(cat /tmp/copy/filename) was pasted"
else
    echo "Oops, something unexpected happened"
fi
