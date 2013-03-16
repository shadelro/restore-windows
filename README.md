restore-window-placement
========================

This project now supports saving and restoring window placement and sizing. The remember.scpt script will memorize the window sizing and placement for each app that you have running. (Note, however, that currently only one window per app is supported.) When restoring, the restore.scpt will skip over any applications in your saved arrangement that are not running.

In order for this script to work, you'll need to go to System Preferences, Keyboard Shortcuts, and make sure each entry for 'Switch to Desktop \<n\>' is checked.

Example usage:

    # Save preset 'single'
    osascript remember.scpt single

    # Restore preset 'single'
    osascript restore.scpt single

I've set up the following aliases in my ~/.zshrc file:

    alias restore="osascript ~/Documents/restore-window-placement/restore.scpt"
    alias remember="osascript ~/Documents/restore-window-placement/remember.scpt"

So that I can simply run:

    remember single
    restore single
