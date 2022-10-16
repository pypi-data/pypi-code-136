import json
import logging
from abc import ABCMeta
from datetime import datetime
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import List

import pytz
from twisted.internet.defer import DeferredList
from twisted.internet.defer import inlineCallbacks
from twisted.internet.task import LoopingCall
from vortex.DeferUtil import deferToThreadWrapWithLogger
from vortex.DeferUtil import nonConcurrentMethod
from vortex.DeferUtil import vortexLogFailure
from vortex.Payload import Payload
from vortex.PayloadEndpoint import PayloadEndpoint
from vortex.PayloadEnvelope import PayloadEnvelope
from vortex.TupleSelector import TupleSelector
from vortex.VortexFactory import VortexFactory
from vortex.VortexUtil import debounceCall
from vortex.storage.TupleStorageSqlite import TupleStorageBatchSaveArguments
from vortex.storage.TupleStorageSqlite import TupleStorageSqlite

from peek_abstract_chunked_index.private.tuples.ACIEncodedChunkTupleABC import (
    ACIEncodedChunkTupleABC,
)
from peek_abstract_chunked_index.private.tuples.ACIUpdateDateTupleABC import (
    ACIUpdateDateTupleABC,
)
from peek_plugin_base.LoopingCallUtil import peekCatchErrbackWithLogger
from peek_plugin_base.PeekVortexUtil import peekServerName

ChunkedIndexChunkLoadRpcMethodType = Callable[
    [list[str]], List[ACIEncodedChunkTupleABC]
]

ChunkedIndexDeltaRpcMethodType = Callable[[bytes], bytes]


class ACICacheControllerABC(metaclass=ABCMeta):
    """Chunked Index Cache Controller

    The Chunked Index cache controller stores all the chunks in memory,
    allowing fast access from the mobile and desktop devices.

    """

    _LOAD_CHUNK_SIZE = 24
    _LOAD_CHUNK_PARALLELISM = 6

    _SNAPSHOT_PERIOD_SECONDS = 60 * 60  # 1 hour
    _CACHE_CHECK_PERIOD_SECONDS = 6 * 60 * 60  # 6 hours

    _OFFLINE_INDEX_BUILD_SECONDS = 5 * 60  # 5 minutes

    # The number of tuples to put in one payload
    _OFFLINE_INDEX_CHUNK_SIZE = 20000

    _ChunkedTuple: ACIEncodedChunkTupleABC = None
    _UpdateDateTupleABC: ACIUpdateDateTupleABC = None
    _chunkLoadRpcMethod: ChunkedIndexChunkLoadRpcMethodType = None
    _chunkIndexDeltaRpcMethod: ChunkedIndexDeltaRpcMethodType = None
    _updateFromServerFilt: Dict = None
    _logger: logging.Logger = None

    def __init__(self, clientId: str, pluginDataDir: Path):
        assert self._ChunkedTuple, "_ChunkedTuple is None"
        assert self._chunkLoadRpcMethod, "_chunkLoadRpcMethod is None"
        assert self._updateFromServerFilt, "_updateFromDeviceFilt is None"
        assert self._logger, "_logger is None"

        self._clientId = clientId
        self._pluginDataDir = pluginDataDir
        self._webAppHandler = None

        #: This stores the cache of chunkedIndex data for the clients
        self._cache: Dict[str, ACIEncodedChunkTupleABC] = {}

        self._endpoint = PayloadEndpoint(
            self._updateFromServerFilt, self._processChunkedIndexPayload
        )

        self._tupleStorage = TupleStorageSqlite(
            databaseDirectory=self._pluginDataDir,
            databaseName=self._ChunkedTuple.__name__,
        )

        self._indexTuple = self._UpdateDateTupleABC()
        self._initialLoadComplete = False

        self._appDownloadSnapshotLoopingCall = None
        self._cacheIntegrityCheckLoopingCall = None

        # Used for indexes that take list of [chunkKey,dateTime] tuples
        self._offlineUpdateDateByChunkKeyPayloads = []

        # Used for loaders that take the whole index tuple
        self._offlineUpdateDateTuplePayload = []

        # If the vortex goes online, check the cache.
        # Before this line of code, the vortex is already online.
        (
            VortexFactory.subscribeToVortexStatusChange(peekServerName)
            .filter(lambda online: online is True)
            .subscribe(on_next=self._checkCache)
        )

    @staticmethod
    def appDownloadPluginDirRelativeDir() -> str:
        return "app_download"

    @classmethod
    def appDownloadFileName(cls):
        return f"{cls._ChunkedTuple.__name__.lower()}_for_app_download.sqlite"

    def setCacheHandler(self, handler):
        self._webAppHandler = handler

    @inlineCallbacks
    def start(self):

        if not (yield self._tupleStorage.isOpen()):
            yield self._tupleStorage.open()

        yield self.reloadCache()
        self._initialLoadComplete = True

        yield self._snapshotToSqliteForAppDownload()
        self._startAppSnapshotLoopingCall()

        self._startCacheIntegrityCheckLoopingCall()

    def _startAppSnapshotLoopingCall(self):
        self._appDownloadSnapshotLoopingCall = LoopingCall(
            peekCatchErrbackWithLogger(self._logger)(
                self._snapshotToSqliteForAppDownload
            )
        )
        d = self._appDownloadSnapshotLoopingCall.start(
            self._SNAPSHOT_PERIOD_SECONDS, now=False
        )
        d.addErrback(vortexLogFailure, self._logger)

    def _startCacheIntegrityCheckLoopingCall(self):
        self._cacheIntegrityCheckLoopingCall = LoopingCall(
            peekCatchErrbackWithLogger(self._logger)(self._checkCache)
        )
        d = self._cacheIntegrityCheckLoopingCall.start(
            self._CACHE_CHECK_PERIOD_SECONDS, now=False
        )
        d.addErrback(vortexLogFailure, self._logger)

    def shutdown(self):
        self._endpoint.shutdown()
        self._endpoint = None

        self._cache = {}
        if self._appDownloadSnapshotLoopingCall:
            self._appDownloadSnapshotLoopingCall.stop()
            self._appDownloadSnapshotLoopingCall = None

    @inlineCallbacks
    def _loadStartupCache(self):
        try:
            encodedChunkTuples = (
                yield self._tupleStorage.loadTuplesAndAggregateAllTuples(
                    batchSize=250
                )
            )
            self._cache = {
                e.ckiChunkKey: e
                for e in encodedChunkTuples
                if isinstance(e, self._ChunkedTuple)
            }

        except Exception as e:
            self._logger.error(
                "The startup state db is broken, Deleting it, %s", str(e)
            )
            yield self._tupleStorage.truncateStorage()

        yield self._updateIndexTuple()

    @inlineCallbacks
    def _storeChunkTuples(
        self, encodedChunkTuples: List[ACIEncodedChunkTupleABC]
    ):
        data = []
        for e in encodedChunkTuples:
            encodedTuple = yield Payload(tuples=[e]).toEncodedPayloadDefer()
            data.append(
                TupleStorageBatchSaveArguments(
                    tupleSelector=e.ckiChunkKey, encodedPayload=encodedTuple
                )
            )

        yield self._tupleStorage.batchSaveTuplesEncoded(data)

    @inlineCallbacks
    @nonConcurrentMethod
    def _snapshotToSqliteForAppDownload(self) -> Path:
        startTime = datetime.now(pytz.utc)

        db = TupleStorageSqlite(
            databaseDirectory=self._pluginDataDir,
            databaseName=(
                self._ChunkedTuple.__name__.lower() + "_for_app_download.tmp"
            ),
        )
        dbPath = db.databasePath

        yield db.open()
        yield db.truncateStorage()

        indexDict = {}
        data = []
        for e in self._cache.values():
            indexDict[e.ckiChunkKey] = e.ckiLastUpdate
            data.append(
                TupleStorageBatchSaveArguments(
                    tupleSelector=e.ckiChunkKey, encodedPayload=e.ckiEncodedData
                )
            )

        yield db.batchSaveTuplesEncoded(data)

        indexTuple = self._UpdateDateTupleABC()
        indexTuple.ckiSetUpdateDateByChunkKey(indexDict)

        ts = TupleSelector(self._UpdateDateTupleABC.tupleName(), {})
        yield db.saveTuples(ts, [self._indexTuple])

        yield db.close()
        del db

        # Move the new DB into place
        finalName = (
            self._pluginDataDir
            / self.appDownloadPluginDirRelativeDir()
            / self.appDownloadFileName()
        )
        finalName.unlink(missing_ok=True)
        dbPath.rename(finalName)

        self._logger.info(
            "Completed creating new app database for download in %s, path %s",
            datetime.now(pytz.utc) - startTime,
            finalName,
        )

        return finalName

    @inlineCallbacks
    def reloadCache(self):
        self._cache = {}

        startTime = datetime.now(pytz.utc)
        yield self._loadStartupCache()
        yield self._checkCache()

        self._logger.info(
            "Reload Cache Completed %s", datetime.now(pytz.utc) - startTime
        )

    @inlineCallbacks
    @nonConcurrentMethod
    def _checkCache(self, *args):
        startTime = datetime.now(pytz.utc)

        # Make sure the cache is up to date (it should be)
        yield self._updateIndexTuple()

        # Find out what we need to reload
        deltaIndexPayload = yield self._chunkIndexDeltaRpcMethod(
            (yield Payload(tuples=[self._indexTuple]).toEncodedPayloadDefer())
        )
        deltaIndex = (
            yield Payload().fromEncodedPayloadDefer(deltaIndexPayload)
        ).tuples[0]

        # Make node of the actions required, and delete the deletes
        # from the cache
        chunkKeysToLoad = []
        chunkKeysToDelete = []
        # Delete all the deltas we need to
        for chunkKey, lastUpdate in deltaIndex.ckiUpdateDateByChunkKey.items():
            if lastUpdate is None:
                del self._cache[chunkKey]
                chunkKeysToDelete.append(chunkKey)

            else:
                chunkKeysToLoad.append(chunkKey)

        chunkKeysKept = list(self._cache)
        chunkKeysUnchanged = list(set(self._cache) - set(chunkKeysToLoad))
        yield self._updateIndexTuple()

        # Delete the removed indexes from the cache
        if chunkKeysToDelete:
            yield self._tupleStorage.batchDeleteTuples(chunkKeysToDelete)

        # Notify any memory resident models of our initial chunk keys

        for i in range(0, len(chunkKeysKept), self._LOAD_CHUNK_SIZE):
            notifyStartTime = datetime.now(pytz.utc)
            yield self._notifyOfChunkKeysUpdated(
                chunkKeysKept[i : i + self._LOAD_CHUNK_SIZE]
            )
            self._logger.info(
                "Notifying handlers of chunks loaded from cache, %s to %s, "
                "%s, took %s",
                i,
                i + self._LOAD_CHUNK_SIZE,
                len(chunkKeysKept),
                datetime.now(pytz.utc) - notifyStartTime,
            )

        self._logger.info(
            "Completed loading index in %s,"
            " %s deleted, %s unchanged, %s to load",
            datetime.now(pytz.utc) - startTime,
            len(chunkKeysToDelete),
            len(chunkKeysUnchanged),
            len(chunkKeysToLoad),
        )

        # Start loading the detlas
        chunkStartTime = datetime.now(pytz.utc)
        yield DeferredList(
            [
                self._reloadCacheThread(chunkKeysToLoad, index)
                for index in range(self._LOAD_CHUNK_PARALLELISM)
            ],
            fireOnOneErrback=True,
        )

        self._logger.info(
            "Completed loading chunks in %s, total cache load time was %s",
            datetime.now(pytz.utc) - chunkStartTime,
            datetime.now(pytz.utc) - startTime,
        )

    @inlineCallbacks
    def _reloadCacheThread(self, chunkKeysToLoad: list[str], threadIndex: int):

        offset = self._LOAD_CHUNK_SIZE * threadIndex
        while True:
            chunkKeysChunk = chunkKeysToLoad[
                offset : offset + self._LOAD_CHUNK_SIZE
            ]
            if not chunkKeysChunk:
                break

            startDate = datetime.now(pytz.utc)
            self._logger.info(
                "Loading %s to %s" % (offset, offset + len(chunkKeysChunk))
            )

            payloadJsonStr = yield self._chunkLoadRpcMethod(chunkKeysChunk)

            if not payloadJsonStr:
                break

            encodedChunkTuples: List[
                ACIEncodedChunkTupleABC
            ] = yield deferToThreadWrapWithLogger(self._logger)(
                self._payloadFromJsonStrBlocking
            )(
                payloadJsonStr
            )

            if not encodedChunkTuples:
                break

            yield self._loadDataIntoCache(encodedChunkTuples)

            self._logger.info(
                "Loaded %s to %s, in %s",
                offset,
                offset + self._LOAD_CHUNK_SIZE,
                datetime.now(pytz.utc) - startDate,
            )

            offset += self._LOAD_CHUNK_SIZE * self._LOAD_CHUNK_PARALLELISM

    def _payloadFromJsonStrBlocking(
        self, payloadJsonStr
    ) -> list[ACIEncodedChunkTupleABC]:

        return Payload().fromJsonDict(json.loads(payloadJsonStr)).tuples

    @inlineCallbacks
    def _processChunkedIndexPayload(
        self, payloadEnvelope: PayloadEnvelope, **kwargs
    ):
        # noinspection PyTypeChecker
        chunkedIndexTuples: List[ACIEncodedChunkTupleABC] = payloadEnvelope.data
        yield self._loadDataIntoCache(chunkedIndexTuples)

    @inlineCallbacks
    def _loadDataIntoCache(
        self, encodedChunkTuples: List[ACIEncodedChunkTupleABC]
    ):

        chunkKeysUpdated: List[str] = []
        deletedCount = 0
        updatedCount = 0

        for t in encodedChunkTuples:
            if not t.ckiHasEncodedData:
                if t.ckiChunkKey in self._cache:
                    deletedCount += 1
                    del self._cache[t.ckiChunkKey]
                    chunkKeysUpdated.append(t.ckiChunkKey)
                continue

            if (
                not t.ckiChunkKey in self._cache
                or self._cache[t.ckiChunkKey].ckiLastUpdate != t.ckiLastUpdate
            ):
                updatedCount += 1
                self._cache[t.ckiChunkKey] = t
                chunkKeysUpdated.append(t.ckiChunkKey)

        yield self._updateIndexTuple()
        yield self._storeChunkTuples(encodedChunkTuples)

        self._logger.debug(
            "Received %s updates from server"
            ", %s had changed"
            ", %s were deleted",
            len(encodedChunkTuples),
            updatedCount,
            deletedCount,
        )

        yield self._notifyOfChunkKeysUpdated(chunkKeysUpdated)

    def _updateIndexTuple(self):
        self._indexTuple.ckiSetUpdateDateByChunkKey(
            {g.ckiChunkKey: g.ckiLastUpdate for g in self._cache.values()}
        )

        d = deferToThreadWrapWithLogger(self._logger)(
            self._updateIndexTupleBlocking
        )(str(self._updateFromServerFilt))
        d.addErrback(vortexLogFailure, self._logger)

    @debounceCall(5 * 60)
    def _updateIndexTupleBlocking(self, _):
        # The _ argument is to make sure calls to debounce work for each index
        startTime = datetime.now(pytz.utc)

        tuples = [
            [i[0], i[1]]
            for i in self._indexTuple.ckiUpdateDateByChunkKey.items()
        ]
        sorted(tuples, key=lambda i: i[0])

        encodedPayloads = []
        for i in range(0, len(tuples), self._OFFLINE_INDEX_CHUNK_SIZE):
            encodedPayloads.append(
                Payload(
                    tuples=tuples[i : i + self._OFFLINE_INDEX_CHUNK_SIZE]
                ).toEncodedPayload()
            )

        self._offlineUpdateDateByChunkKeyPayloads = encodedPayloads

        self._offlineUpdateDateTuplePayload = Payload(
            tuples=[self._indexTuple]
        ).toEncodedPayload()

        self._logger.debug(
            "Completed building offline index, %s groups, %s chunks, in %s",
            len(encodedPayloads),
            len(self._indexTuple.ckiUpdateDateByChunkKey),
            datetime.now(pytz.utc) - startTime,
        )

    @inlineCallbacks
    def _notifyOfChunkKeysUpdated(self, chunkKeys: List[Any]):
        yield self._webAppHandler.notifyOfUpdate(chunkKeys)

    def encodedChunk(self, chunkKey) -> ACIEncodedChunkTupleABC:
        return self._cache.get(chunkKey)

    def encodedChunkKeys(self) -> List[int]:
        # Wrapping this in a list is expensive
        return self._cache.keys()

    def encodedChunkLastUpdateByKey(self):
        return self._indexTuple.ckiUpdateDateByChunkKey

    def offlineUpdateDateByChunkKeyPayload(self, index):
        return self._offlineUpdateDateByChunkKeyPayloads[int(index)]

    def offlineUpdateDateTuplePayload(self):
        return self._offlineUpdateDateTuplePayload
