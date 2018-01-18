pooh-bot
===
*A simple Discord bot that helps keep your server family friendly.*

![demo](demo.gif)

Reads messages from non-private channels and adds the `:pooh:` emoji as a reaction to any messages containing swear words. Also watches for edits, and adds/removes the reaction as necessary. Falls back to 💩 if `:pooh:` is unavailable as a server emoji.

### Commands

`!strict` - Toggles a strict mode. When strict mode is on, messages containing profanity are deleted with a warning to the author. This command is only available to admins.
