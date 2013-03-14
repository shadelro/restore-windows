restore-window-placement
========================

Note: everything is hardcoded, so if you want this to work, you'll have to edit preset1.txt and preset2.txt with your sizing/placements and edit restore.scpt with AppleScript Editor to point to the directory where you've checked out the project.

There are currently two presets - one for single display and one for a single external monitor.

Example usage:

    # Restore preset 1
    osascript restore.scpt 1

    # Restore preset 2
    osascript restore.scpt 2

I've set up the following alias in my ~/.zshrc file:

    alias restore="osascript ~/Documents/restore/restore.scpt"

So that I can simply run:

    restore 1
    restore 2

