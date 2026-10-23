# Owner profile

| Setting | Value |
|---|---|
| Time zone | _TBD (e.g. America/Los_Angeles)_ |
| Email | not used for reminders (Gmail connected if needed) |
| Push | Claude app on phone — **primary and only channel for now** |
| Discord | not used (webhook script kept in case) |
| SMS | not used |

## Reminder defaults

- Lead time: 30 min before events, plus 10 min before if travel is needed.
- Daily briefing: _TBD time_ — today's schedule + any conflicts.
- Quiet hours: _TBD_

## Intake

The owner pastes ("dumps") schedules, screenshots, emails and notes into the
PA session. For each dump: extract every commitment into `schedule.md`, run
`check_conflicts.py`, report clashes, and schedule push reminders, logging them
in `reminders.md`. Ask only about things that can't be inferred (missing date,
time or duration).
