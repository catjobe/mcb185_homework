gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v "[^zoniacr]" | grep -E ".{4,}"
