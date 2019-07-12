
# Dirty address parsing

My girlfriend had a work assignment to take an Excel spreadsheet of a single column of "dirty" addresses like this...

```
Business Name Here 123 Address Rd, CityTown, NJ 07302
```

... and separate those out into a new spreadsheet with headings like this ...

```
| NAME | ADDRESS | ADDRESS | CITY | STATE | ZIPCODE |
```

I wrote some Python to save her a week of work. There were *a lot* of addresses but I've just included a sample that's been pseudonymized.

Prep work involved saving the dirty address list as a CSV to more easily pull it into Python for cleaning. Then, after the script is run, opening the output CSV in Excel to copy over the cells into a full-blown `xlsx` file.

In case the parse went awry there's a column "RAWDATA" which has the original string.

Despite this bit of manual review, it saved her a ton of time.
