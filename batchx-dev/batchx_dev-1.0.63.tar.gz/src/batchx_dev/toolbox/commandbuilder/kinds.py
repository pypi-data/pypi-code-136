from ..parsers import Input, Manifest


class CommandKindMixin:

    # writer functions
    def get_cmd(self, input: Input, sort=True) -> list[str]:
        """
        Generate command array.

        Args:
            input (Input): Input object (encodes an input json)
            sort (bool, optional): Whether or not to sort the element of the command alphabetically.
                                    If set to True, the order in which the commands were added to the CommandBuilder is
                                    maintained when generating the final command. Defaults to True.

        Returns:
            list[str]: Array of command parts.
        """

        input = self.check_constraints(input, self.manifest)
        input = self.do_actions(input, self.manifest)

        tool_cmd = [s for s in str(self.tool).split() if len(s) > 0]

        kval_cmds, kval_keys = self._get_keyvalue_cmd(input)
        flag_cmds, flag_keys = self._get_flag_cmd(input)
        args_cmds, args_keys = self._get_argument_cmd(input)
        cmds = kval_cmds + flag_cmds + args_cmds

        if sort:
            keys = kval_keys + flag_keys + args_keys
            d = {k: c for k, c in zip(keys, cmds)}
            cmds = [d.get(k, None) for k in self.commands]
            cmds = [c for c in cmds if c is not None]

        cmds = [e for c in cmds for e in c if len(e) > 0]

        return tool_cmd + cmds

    def _get_keyvalue_cmd(self, input: Input, force=False):
        cmds = []
        keys = []
        for key in self.kinds["keyval"]:
            v = getattr(input, key, None)
            if v is not None or force:

                if isinstance(v, list):
                    part = [self.commands[key], *v]
                else:
                    part = [self.commands[key], v]

                part = ["{e}".format(e=e) for e in part]
                part = [e for e in part if len(e) > 0]

                cmds.append(part)
                keys.append(key)
        return cmds, keys

    def _get_flag_cmd(self, input: Input, force=False):
        cmds = []
        keys = []
        for key in self.kinds["flag"]:
            if getattr(input, key, False) or force:
                part = [self.commands[key]]

                part = ["{e}".format(e=e) for e in part]
                part = [e for e in part if len(e) > 0]
                cmds.append(part)
                keys.append(key)
        return cmds, keys

    def _get_argument_cmd(self, input: Input, force=False):
        cmds = []
        keys = []
        for key in self.kinds["argument"]:
            if getattr(input, key, None) is not None or force:
                v = getattr(input, key, None)

                if isinstance(v, list):
                    part = [*v]
                else:
                    part = [v]

                part = ["{e}".format(e=e) for e in part]
                part = [e for e in part if len(e) > 0]
                cmds.append(part)
                keys.append(key)
        return cmds, keys

    # assignment
    def set_kind(self, kind: str = "keyval", key: str | None = None):
        if key is None:
            key = self.active_key

        # check if this key was already assigned to a kind
        for keys_from_a_specific_kind in self.kinds.values():
            if key in keys_from_a_specific_kind:
                keys_from_a_specific_kind.remove(key)

        # assign this key to a kind
        if self.kinds.get(kind, None) is not None:
            self.kinds[kind].add(key)
        else:
            self.kinds[kind] = set([key])

        self.active_key = key
        return self

    # alias
    def add_kind(self, kind: str = "keyval", key: str | None = None):
        # alias
        return self.set_kind(kind=kind, key=key)
