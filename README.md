restore-window-placement
========================

Note: everything is hardcoded, so if you want this to work, you'll have to edit preset1.txt and preset2.txt with your list of apps and sizing/placements, and if you want additional presets you'll have to add them to restore.scpt.

There are currently two presets - one for single display and one for a single external monitor.

Example usage:

    # Restore preset 1
    osascript restore.scpt 1

    # Restore preset 2
    osascript restore.scpt 2

I've set up the following alias in my ~/.zshrc file:

    alias restore="osascript ~/Documents/restore-window-placement/restore.scpt"

So that I can simply run:

    restore 1
    restore 2
