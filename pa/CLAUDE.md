# Personal Assistant (PA) mode

This folder turns the repo into the owner's personal-assistant workspace. When a
session is asked to act as "PA", work from these files:

- `profile.md` — time zone, notification channels, preferences. Read first.
- `schedule.md` — known commitments. Keep it sorted; run `check_conflicts.py`
  after every change and tell the owner about any clash or tight gap.
- `reminders.md` — every scheduled reminder (with its scheduled-task id) so it
  can be cancelled or moved when plans change.

## Notifying the owner

Pick the channel(s) listed in `profile.md`, most urgent first:

1. **Claude app push** — scheduled tasks created with
   `create_new_session_on_fire=true` and `notifications: {push: true}`.
2. **Email** — Gmail connector `send_message` to the owner's address.
3. **Discord** — `./notify_discord.sh "message"` (needs `DISCORD_WEBHOOK_URL`
   set as an environment secret, never committed).

Reminder messages: one line, lead with the action and time,
e.g. "Leave now: dentist 3:00pm, 20 min drive".

## Butler (digital asset management)

Asset-management requests go to the owner's "Butler" session via
`send_message`. It runs on the owner's computer through Remote Control, so it is
only reachable while that computer is on; if it is offline, say so and keep the
request in `reminders.md` to resend later.

## Rules

- Never commit secrets (webhook URLs, phone numbers beyond what the owner put in
  `profile.md`).
- Confirm before sending anything to someone other than the owner.
