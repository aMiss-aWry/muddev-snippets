# Helpful commands that are not polished enough to be offered as PRs to the main upstream Evennia
# repo, but that I've found to be nice enough to have that it's worth putting out here.

import datetime
from commands.command import Command

class CmdRevise(Command):
    """
    Fix a typo in the room or on an object in the room. This is not meant to redo an
    entire description but amend minor mistakes.

    Please note that these edits do not extend to all similar items. If something is made
    repeatedly from the same prototype, and there's a typo in the prototype code, all
    objects will be made with the same recurring typo.

    These changes are logged and stored with your name.

    Usage:
       revise here <typo>=<correction>:
         ex. revise here teh=the
             revise here its=it's
       revise <target> <typo>=<correction>

    You can see recent typo fixes in the area with:
       revise here
    """

    key = "@revise"
    aliases = ["revise"]
    locks = "cmd:perm(Builder)"
    help_category = "Building"

    def list_recent_typos(self, item):
        if item.db.revisions:
            entry_msg = f"Edit history on [{item.key}]:\n"
            for old, new, fixer, timestamp in item.db.revisions:
                entry_msg += f"{timestamp} ({fixer}): {old} -> {new}\n"
            return entry_msg
        return f"No typos have been fixed on {item.key}."

    def func(self):
        caller = self.caller
        location = self.caller.location
        args = self.args.strip()

        if not args:
            caller.msg("Usage: revise <target> <typo>=<correction>")
            return
        
        # This part is gross.
        split_args_space = args.split(" ")
        target_name = split_args_space[0]
        target = caller.search(target_name)
        if not target:
            return
        args = args.replace(target_name, "", 1)
        args = args.strip()

        try:
            old_typo, new_fix = map(str.strip, args.split("=", 1))
        except:
            # Just listing existing fixes
            caller.msg(self.list_recent_typos(target))
            return

        if not target.db.desc:
            caller.msg("Nothing to revise.")
            return

        if old_typo and new_fix:
            if old_typo in target.db.desc:
                old_desc = target.db.desc
                new_desc = old_desc.replace(old_typo, new_fix, 1)
                if old_desc == new_desc:
                    caller.msg(f"No change detected.")
                    return
                target.db.desc = new_desc
                caller.msg(
                    f"You modify {target} so that |w[|n{old_typo}|w]|n becomes |w[|n{new_fix}|w]|n."
                )
                if not target.db.revisions:
                    target.db.revisions = []
                time_msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                target.db.revisions.append(
                    (old_typo, new_fix, f"{caller.key}#{caller.id}", time_msg)
                )
            else:
                caller.msg(
                    f"You can't find |w[|n{old_typo}|w]|n in {target}'s description in the database."
                )
        else:
            caller.msg(
                "You need to separate the typo from correction with an equals sign."
            )
