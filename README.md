# get-sites-by-type

This cli script is used to get the names of World Heritage Convention sites related to music!
It also has the capability of returning sites by other categories as well as returning other fields!

## Installation

Ensure you have python installed!
https://www.python.org/downloads/

## Usage

```# Returns the names of music-related sites
python get-sites-by-type.py

# Returns the names of Cultural sites
python get-sites-by-type.py -v "Cultural"

# Returns the names of Mixed sites
python get-sites-by-type.py -v "mixed"

# Returns the inscribed dates of Cultural sites
python get-sites-by-type.py -c "date_inscribed" -v "cultural"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Future plans
- Add tests to ensure changes don't break functionality
- Migrate data to database instead of CSV
- Use web front-end instead of CLI
- Enhance the --help function with examples and a more robust description
- Packages used were decided on based on time and robustness instead of home-
  rolling a CSV parser and having to consider all edge cases; if this needs
  changed, consider making one from scratch


