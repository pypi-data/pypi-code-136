"""
Base code for db join
"""
import collections
import collections.abc
import dotted
import itertools


MARKER = object()


#
# internal helpers
#
class AccrualItem:
    __slots__ = ('obj', 'key', 'field', 'replaces')
    def __init__(self, obj, key, field, replaces=False):
        assert key is not None, 'Accrual key is invalid'
        self.obj = obj
        self.key = key
        self.field = field
        self.replaces = replaces
    def __hash__(self):
        return hash((self.key, self.field, self.replaces))
    def __eq__(self, other):
        return self.key == other.key and self.field == other.field and \
            self.replaces == other.replaces


class AtLeastOnceError(LookupError):
    pass


def atleastonce(iterable):
    """
    If iterable yields nothing, throw AtLeastOnceError
    """
    iterable = iter(iterable)
    try:
        yield next(iterable)
    except StopIteration:
        raise AtLeastOnceError
    yield from iterable


#
# base join wrapper
#
class Join:
    """
    For each obj in `iterable`, load datastore objs on matching dotted field patterns
    This could potentially expand multiple times per obj since we may wish to join
    against a previous join
    Given:
        Entity<Key A>({'stuff': <Key B>})
        Entity<Key B>({'hello': <Key C>})
        Entity<Key C>({'foo': 'bar'})
    And:
        join(client, iterable, ('*', '*.*',))
    This would join B on A and then C on B on A:
        Entity<Key A>({'stuff': Entity<Key B>({'hello': Entity<Key C>('foo': 'bar')})})

    Scoping:
        You can scope a field pattern using the ':' operator.  For example, say you
        only wish to join against keys that match a particular kind hierachy, such as
        User:Source:*.*

    Chaining:
        You chain a field pattern to a different field pattern with reference to obj
        that was fetched, eg. `owner->profile`. This will fetch owner and then descend to
        join on owner's profile

    Replacing:
        You can replace an obj with respect to a field by using the `!` operator, eg.
        `!link`.  This  will replace obj with whatever was fetched via link

    Expanding:
        You can recursively chain a field, eg. `+stuff->+more`.  This is equivalent to:
            stuff->more
            stuff->stuff->more
            stuff->stuff->more->more
            ...
    """
    GROUPSIZE = None

    def __init__(self, cache=None, *, groupsize=None, max_accrualsize=None):
        self._cache = cache
        self._groupsize = groupsize
        self._max_accrualsize = max_accrualsize

    @property
    def groupsize(self):
        r = self._groupsize or self.GROUPSIZE
        assert r, 'GROUPSIZE must be set'
        return r

    @property
    def max_accrualsize(self):
        return self._max_accrualsize or 5*self.groupsize

    @property
    def cachesize(self):
        return 5 * self.groupsize

    @property
    def cache(self):
        return self._cache or self.new_cache()

    def new_cache(self, maxsize=None):
        from .cache import LRUCache
        return LRUCache(maxsize or self.cachesize)

    def getter(self, obj, field):
        return dotted.get(obj, field)

    def setter(self, obj, field, val):
        return dotted.update(obj, field, val)

    def is_key(self, obj):
        """
        True if obj is a key
        """
        raise NotImplementedError

    def obj2key(self, obj):
        """
        Returns primary key from db entity obj
        """
        raise NotImplementedError

    def _obj2key(self, obj):
        """
        Internal call to ensure we have a 'key' even if obj doesn't explicitly have one
        """
        key = self.obj2key(obj)
        if key is not None:
            return key
        return id(obj)

    def is_expandable(self, obj, scopes):
        """
        An expandable obj must be a key OR a db entity (with a key)
        It may optionally be constrained by `scopes`
        """
        raise NotImplementedError

    def get_multi(self, client, keys, **kwargs):
        raise NotImplementedError

    def __call__(self, client, iterable, pats, *, cache=None, **kwargs):
        cache = cache or self.cache
        getter = self.getter
        setter = self.setter
        get_multi = self.get_multi
        is_key = self.is_key
        is_expandable = self.is_expandable
        max_accrualsize = self.max_accrualsize
        groupsize = kwargs.pop('groupsize', None) or self.groupsize
        limit = kwargs.pop('limit', None)
        _filter = kwargs.pop('filter', None)

        if not pats:
            pats = ()
        elif isinstance(pats, str):
            pats = (pats,)

        # FIXME: parsing is kinda dumb; probably should haved pyparse do this work
        def _parse(pat):
            chain = pat.split('->')
            parsed = []
            for c in chain:
                *scopes, pat = c.split(':')
                d = {
                    'pat': pat,
                    'scopes': scopes,
                    'mode': None,
                }
                if len(pat) > 1:
                    if pat[0] == '!' and pat[1] != '!':
                        d['pat'] = pat[1:]
                        d['mode'] = 'replaces'
                    elif pat[0] == '+' and pat[1] != '+':
                        d['pat'] = pat[1:]
                        d['mode'] = 'rchains'
                parsed.append(d)
            return parsed

        # preparse all pats in a 'chain' of dicts
        chains = (_parse(pat) for pat in pats)
        chains = [chain for chain in chains if chain]

        # if chained operation is replacing, then fold value up a level in chain
        # this is fine except for very top of chain which requires replace_map`
        def _fold(obj, field, iterable):
            try:
                item, val = next(iterable)
            except StopIteration:
                return
            if item.replaces:
                setter(obj, field, val)
            else:
                yield item, val
            yield from iterable

        def _expand_chain(obj, chain):
            if not chain:
                return

            working = chain[0]
            _pat = working['pat']
            scopes = working['scopes']
            replaces = working['mode'] == 'replaces'
            rchains = working['mode'] == 'rchains'

            fields = dotted.expand(obj, _pat) if dotted.is_pattern(_pat) else (_pat,)
            for field in fields:
                val = getter(obj, field)
                if not is_expandable(val, scopes):
                    continue
                if not is_key(val):
                    if rchains:
                        yield from _expand_chain(val, chain)
                    yield from _fold(obj, field, _expand_chain(val, chain[1:]))
                    continue

                # otherwise we've got a key
                # look in cache
                _val = cache.get(val, MARKER)
                if _val is None:                # negative cache hit
                    continue
                if _val is MARKER:              # not in cache?
                    yield AccrualItem(obj, self._obj2key(obj), field, replaces), val
                    continue

                # we're in cache; so stash val and see if there's more chaining work
                setter(obj, field, _val)
                if rchains:
                    yield from _expand_chain(_val, chain)
                yield from _fold(obj, field, _expand_chain(_val, chain[1:]))

        def _expand(obj):
            for chain in chains:
                yield from _expand_chain(obj, chain)

        def _map(obj, accrual):
            try:
                count = 0
                for item,val in atleastonce(_expand(obj)):
                    items = accrual[val]
                    if item not in items:
                        items.add(item)
                        count += 1
            except AtLeastOnceError:
                return False, 0
            return True, count

        def _reduce(accrual, replace_map):
            count = 0
            _groupsize =  min(limit or groupsize, groupsize)
            keys = list(itertools.islice(accrual, _groupsize))
            found = {o.key:o for o in get_multi(client, keys, **kwargs)}
            cache.update(found)
            cache.update((k,None) for k in keys - found.keys())
            for key in keys:
                items = accrual.pop(key)
                count += len(items)
                if key not in found:
                    continue
                val = found[key]
                for item in items:
                    if item.replaces:
                        replace_map[item.key] = val
                    else:
                        setter(item.obj, item.field, val)
            return count

        def _replace(obj, replace_map):
            key = self._obj2key(obj)
            if key not in replace_map:
                return obj
            seen = set()
            while key not in seen:
                seen.add(key)
                obj = replace_map.get(key, obj)
                key = self._obj2key(obj)
            for key in seen:
                replace_map[key] = obj
            return obj

        # basic algorithm
        #   1. enqueue an obj from iterable
        #   2. gather keys from fields specified enqueued [could be transitive via chain]
        #   3. if nothing gathered from obj, then it's _done_ processing so yield up
        #      if there's no more work for objs enqueued ahead of it
        #   4. get_multi on all keys once we've gathered enough of them
        #   5. write the fetched data back to the accrued fields
        #   6. rinse & repeat until everything is processed
        q = collections.deque()
        iterable = iter(iterable)
        accrual = collections.defaultdict(set)
        accrued = 0
        replace_map = {}
        while True:
            _groupsize =  min(limit or groupsize, groupsize)

            obj = next(iterable, MARKER)
            if obj is not MARKER:
                obj = _replace(obj, replace_map)
                _, count = _map(obj, accrual)
                accrued += count
                q.append(obj)
            elif not q:
                return

            # force early reduce if accrual is too large or reached end of iterable
            if obj is MARKER or len(accrual) >= _groupsize or accrued >= max_accrualsize:
                accrued -= _reduce(accrual, replace_map)
            else:
                continue

            # attempt to yield up objects that are done
            # but we may have more processing
            more = False
            consumed = 0
            for obj in q:
                obj = _replace(obj, replace_map)
                mapped, count = _map(obj, accrual)
                accrued += count
                more = more or mapped
                if not more:
                    consumed += 1
                    if _filter and not _filter(obj):
                        continue
                    yield obj
                    if limit is not None:
                        limit -= 1
                        if limit <= 0:
                            return
                elif len(accrual) >= _groupsize or accrued >= max_accrualsize:
                    break

            # clear stuff that was yielded
            for _ in range(consumed):
                q.popleft()

            # if q is empty, it's safe to clear replace_map
            # FIXME: clearing replace_map is a big hammer because transitive replaces
            #        are cleared as well. we could count replace mappings and only
            #        clear those with count == 1.
            # FIXME: replace_map could potentially grow 1:1 with iterable size if `q`
            #        never gets a chance to empty. we could to force `q` to empty
            #        if replace_map is too large. OR come up with a better algorithm
            #        to deal with top-level replaces.
            if not q:
                replace_map.clear()
