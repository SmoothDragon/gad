# gad

## Super Alpha status! Use at your own risk!

**gad** v. to roam about restlessly.

gad is a utility for file management. Remove duplications, recognize files you have already decided to delete, etc.

gad is designed to be similar in usage to git.


# Progam flow
Start by initializing `gad init`. If you are already have a `.gad` directory as a parent, this will do nothing.

`gad status` shows the accumulation of file manipulation commands.
* How many files are in the database.
* How many file hashes are of deleted files.
* How many untracked files there are.

`gad scan` will scan the entire `.gad` directory from its root and update the database.

`gad add <filename>` will queue the given file(s) to be added to the database.
`gad add <dir>` will queue all files in the directory to be added to the database.
`gad add` will hash a file and record its location in a database.

`gad rm -m "This file sucks." <filename>` will queue the given file(s) for deletion and record their hashes in the database. The message is optional, but nice to know for future reference.
`gad rm` will mark the file has as "unwanted" in the database. Makes removal of duplicats safer.

`gad ignore <pattern>` will add a specific filename pattern to ignore.

`gad autoclean` will:
* Queue files that match previous removal for deletion.
* Queue duplicate files for deletion. If order is not specified in config, then `gad` will show there is a conflict and not delete any duplicate.


`gad commit` will execute queued commands.
`gad commit` will execute the series of commands.

