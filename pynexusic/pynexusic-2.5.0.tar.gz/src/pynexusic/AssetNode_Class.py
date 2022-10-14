class AssetNode:
    def __init__(self, name: str, sysType: str = 'NEXUSIC'):
        assert sysType in ['NEXUSIC'], 'Unsupported system'

        self.name = name
        self.data = None
        self._parent = None
        self._children = []
        self.sysType = sysType

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    @property
    def parent(self):
        return self._parent

    @property
    def children(self) -> list:
        return self._children

    @property
    def isRoot(self) -> bool:
        return self.parent == None

    @property
    def isLeaf(self) -> bool:
        return len(self._children) == 0

    def addChild(self, assetNode) -> None:
        self._children.append(assetNode)
        assetNode._parent = self
        if len(self._children) == 0:
            self._isLeaf = True
        else:
            self._isLeaf = False

    def removeChild(self, assetNode) -> None:
        self._children.remove(assetNode)
        assetNode._parent = None
        if len(self._children) == 0:
            self._isLeaf = True
        else:
            self._isLeaf = False

    def childExist(self, assetNode):
        for child in self._children:
            if self.sysType == 'NEXUSIC':
                if child.data and assetNode.data and child.data['VN_ID'] == assetNode.data['VN_ID']:
                    return child
        return None
