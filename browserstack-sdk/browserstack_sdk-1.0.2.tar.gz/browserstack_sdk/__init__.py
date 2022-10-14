# coding: UTF-8
import sys
bstack111_opy_ = sys.version_info [0] == 2
bstack1l1l1_opy_ = 2048
bstack1ll11_opy_ = 7
def bstack111l_opy_ (bstack1_opy_):
    global bstack1ll1l_opy_
    bstack11lll_opy_ = ord (bstack1_opy_ [-1])
    bstack11l1_opy_ = bstack1_opy_ [:-1]
    bstack1ll_opy_ = bstack11lll_opy_ % len (bstack11l1_opy_)
    bstackl_opy_ = bstack11l1_opy_ [:bstack1ll_opy_] + bstack11l1_opy_ [bstack1ll_opy_:]
    if bstack111_opy_:
        bstack11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1_opy_ - (bstack1ll1_opy_ + bstack11lll_opy_) % bstack1ll11_opy_) for bstack1ll1_opy_, char in enumerate (bstackl_opy_)])
    else:
        bstack11_opy_ = str () .join ([chr (ord (char) - bstack1l1l1_opy_ - (bstack1ll1_opy_ + bstack11lll_opy_) % bstack1ll11_opy_) for bstack1ll1_opy_, char in enumerate (bstackl_opy_)])
    return eval (bstack11_opy_)
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
from packaging import version
from browserstack.local import Local
bstack1l1l_opy_ = {
	bstack111l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࢋ"): bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࠨࢌ"),
  bstack111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨࢍ"): bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡱࡥࡺࠩࢎ"),
  bstack111l_opy_ (u"ࠧࡰࡵࠪ࢏"): bstack111l_opy_ (u"ࠨࡱࡶࠫ࢐"),
  bstack111l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬ࢑"): bstack111l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ࢒"),
  bstack111l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ࢓"): bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡠࡹ࠶ࡧࠬ࢔"),
  bstack111l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ࢕"): bstack111l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࠨ࢖"),
  bstack111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫࢗ"): bstack111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࠨ࢘"),
  bstack111l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ࢙"): bstack111l_opy_ (u"ࠫࡳࡧ࡭ࡦ࢚ࠩ"),
  bstack111l_opy_ (u"ࠬࡪࡥࡣࡷࡪ࢛ࠫ"): bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡥࡣࡷࡪࠫ࢜"),
  bstack111l_opy_ (u"ࠧࡤࡱࡱࡷࡴࡲࡥࡍࡱࡪࡷࠬ࢝"): bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡷࡴࡲࡥࠨ࢞"),
  bstack111l_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࠧ࢟"): bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࠧࢠ"),
  bstack111l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰࡐࡴ࡭ࡳࠨࢡ"): bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡐࡴ࡭ࡳࠨࢢ"),
  bstack111l_opy_ (u"࠭ࡶࡪࡦࡨࡳࠬࢣ"): bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡶࡪࡦࡨࡳࠬࢤ"),
  bstack111l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡏࡳ࡬ࡹࠧࢥ"): bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡏࡳ࡬ࡹࠧࢦ"),
  bstack111l_opy_ (u"ࠪࡸࡪࡲࡥ࡮ࡧࡷࡶࡾࡒ࡯ࡨࡵࠪࢧ"): bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡲࡥ࡮ࡧࡷࡶࡾࡒ࡯ࡨࡵࠪࢨ"),
  bstack111l_opy_ (u"ࠬ࡭ࡥࡰࡎࡲࡧࡦࡺࡩࡰࡰࠪࢩ"): bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡭ࡥࡰࡎࡲࡧࡦࡺࡩࡰࡰࠪࢪ"),
  bstack111l_opy_ (u"ࠧࡵ࡫ࡰࡩࡿࡵ࡮ࡦࠩࢫ"): bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵ࡫ࡰࡩࡿࡵ࡮ࡦࠩࢬ"),
  bstack111l_opy_ (u"ࠩࡵࡩࡸࡵ࡬ࡶࡶ࡬ࡳࡳ࠭ࢭ"): bstack111l_opy_ (u"ࠪࡶࡪࡹ࡯࡭ࡷࡷ࡭ࡴࡴࠧࢮ"),
  bstack111l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ࢯ"): bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧࢰ"),
  bstack111l_opy_ (u"࠭࡭ࡢࡵ࡮ࡇࡴࡳ࡭ࡢࡰࡧࡷࠬࢱ"): bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡭ࡢࡵ࡮ࡇࡴࡳ࡭ࡢࡰࡧࡷࠬࢲ"),
  bstack111l_opy_ (u"ࠨ࡫ࡧࡰࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ࢳ"): bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡫ࡧࡰࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ࢴ"),
  bstack111l_opy_ (u"ࠪࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪࠪࢵ"): bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪࠪࢶ"),
  bstack111l_opy_ (u"ࠬࡹࡥ࡯ࡦࡎࡩࡾࡹࠧࢷ"): bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹࡥ࡯ࡦࡎࡩࡾࡹࠧࢸ"),
  bstack111l_opy_ (u"ࠧࡢࡷࡷࡳ࡜ࡧࡩࡵࠩࢹ"): bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡷࡷࡳ࡜ࡧࡩࡵࠩࢺ"),
  bstack111l_opy_ (u"ࠩ࡫ࡳࡸࡺࡳࠨࢻ"): bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡫ࡳࡸࡺࡳࠨࢼ"),
  bstack111l_opy_ (u"ࠫࡧ࡬ࡣࡢࡥ࡫ࡩࠬࢽ"): bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧ࡬ࡣࡢࡥ࡫ࡩࠬࢾ"),
  bstack111l_opy_ (u"࠭ࡷࡴࡎࡲࡧࡦࡲࡓࡶࡲࡳࡳࡷࡺࠧࢿ"): bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡷࡴࡎࡲࡧࡦࡲࡓࡶࡲࡳࡳࡷࡺࠧࣀ"),
  bstack111l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡅࡲࡶࡸࡘࡥࡴࡶࡵ࡭ࡨࡺࡩࡰࡰࡶࠫࣁ"): bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦ࡬ࡷࡦࡨ࡬ࡦࡅࡲࡶࡸࡘࡥࡴࡶࡵ࡭ࡨࡺࡩࡰࡰࡶࠫࣂ"),
  bstack111l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧࣃ"): bstack111l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫࣄ"),
  bstack111l_opy_ (u"ࠬࡸࡥࡢ࡮ࡐࡳࡧ࡯࡬ࡦࠩࣅ"): bstack111l_opy_ (u"࠭ࡲࡦࡣ࡯ࡣࡲࡵࡢࡪ࡮ࡨࠫࣆ"),
  bstack111l_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡖࡦࡴࡶ࡭ࡴࡴࠧࣇ"): bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳ࡭ࡺࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨࣈ"),
  bstack111l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡑࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭ࣉ"): bstack111l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧ࣊"),
  bstack111l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡒࡪࡺࡷࡰࡴ࡮ࠫ࣋"): bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡻࡳࡵࡱࡰࡒࡪࡺࡷࡰࡴ࡮ࠫ࣌"),
  bstack111l_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡐࡳࡱࡩ࡭ࡱ࡫ࠧ࣍"): bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡮ࡦࡶࡺࡳࡷࡱࡐࡳࡱࡩ࡭ࡱ࡫ࠧ࣎"),
  bstack111l_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹ࣏ࠧ"): bstack111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࡵ࣐ࠪ"),
  bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏ࣑ࠬ"): bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏ࣒ࠬ"),
  bstack111l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩ࣓ࠬ"): bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡹ࡯ࡶࡴࡦࡩࠬࣔ"),
}
bstack1l1_opy_ = [
  bstack111l_opy_ (u"ࠧࡰࡵࠪࣕ"),
  bstack111l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫࣖ"),
  bstack111l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫࣗ"),
  bstack111l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨࣘ"),
  bstack111l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨࣙ"),
  bstack111l_opy_ (u"ࠬࡸࡥࡢ࡮ࡐࡳࡧ࡯࡬ࡦࠩࣚ"),
  bstack111l_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ࣛ"),
]
bstack1l_opy_ = {
  bstack111l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪࣜ"): bstack111l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬࣝ"),
  bstack111l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫࣞ"): [bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬࣟ"), bstack111l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ࣠")],
  bstack111l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ࣡"): bstack111l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࣢"),
  bstack111l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࣣࠫ"): bstack111l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨࣤ"),
  bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧࣥ"): [bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࣦࠫ"), bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪࣧ")],
  bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ࣨ"): bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨࣩ"),
  bstack111l_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫ࣪"): bstack111l_opy_ (u"ࠨࡴࡨࡥࡱࡥ࡭ࡰࡤ࡬ࡰࡪ࠭࣫"),
  bstack111l_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ࣬"): [bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡴࡵ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰ࣭ࠪ"), bstack111l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲ࣮ࠬ")],
  bstack111l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶ࣯ࠫ"): [bstack111l_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹࡹࣰࠧ"), bstack111l_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡓࡴ࡮ࡆࡩࡷࡺࣱࠧ")]
}
bstack1lll1_opy_ = {
  bstack111l_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࣲࠧ"): [bstack111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࡵࠪࣳ"), bstack111l_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡖࡷࡱࡉࡥࡳࡶࠪࣴ")]
}
bstack1lll_opy_ = [
  bstack111l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪࣵ"),
  bstack111l_opy_ (u"ࠬࡶࡡࡨࡧࡏࡳࡦࡪࡓࡵࡴࡤࡸࡪ࡭ࡹࠨࣶ"),
  bstack111l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬࣷ"),
  bstack111l_opy_ (u"ࠧࡴࡧࡷ࡛࡮ࡴࡤࡰࡹࡕࡩࡨࡺࠧࣸ"),
  bstack111l_opy_ (u"ࠨࡶ࡬ࡱࡪࡵࡵࡵࡵࣹࠪ"),
  bstack111l_opy_ (u"ࠩࡶࡸࡷ࡯ࡣࡵࡈ࡬ࡰࡪࡏ࡮ࡵࡧࡵࡥࡨࡺࡡࡣ࡫࡯࡭ࡹࡿࣺࠧ"),
  bstack111l_opy_ (u"ࠪࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡖࡲࡰ࡯ࡳࡸࡇ࡫ࡨࡢࡸ࡬ࡳࡷ࠭ࣻ")
]
bstack1l1ll_opy_ = [
  bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࣼ"),
  bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࣽ"),
  bstack111l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࣾ"),
  bstack111l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧࣿ"),
  bstack111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫऀ"),
  bstack111l_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫँ"),
  bstack111l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ं"),
  bstack111l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨः"),
  bstack111l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨऄ"),
]
bstack1l11l_opy_ = [
  bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪअ"),
  bstack111l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭आ"),
]
bstack11ll1_opy_ = bstack111l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡺࡨ࠴࡮ࡵࡣࠩइ")
bstack1l11_opy_ = bstack111l_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠬई")
bstack1l111_opy_ = {
  bstack111l_opy_ (u"ࠪࡧࡷ࡯ࡴࡪࡥࡤࡰࠬउ"): 50,
  bstack111l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪऊ"): 40,
  bstack111l_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭ऋ"): 30,
  bstack111l_opy_ (u"࠭ࡩ࡯ࡨࡲࠫऌ"): 20,
  bstack111l_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ऍ"): 10
}
DEFAULT_LOG_LEVEL = bstack1l111_opy_[bstack111l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ऎ")]
bstack11l_opy_ = bstack111l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨए")
bstack1111_opy_ = bstack111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨऐ")
bstack11l1l_opy_ = bstack111l_opy_ (u"ࠫࡵࡧࡢࡰࡶ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࠩऑ")
bstack1llll_opy_ = [bstack111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ऒ"), bstack111l_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ओ")]
bstack11ll_opy_ = [bstack111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪऔ"), bstack111l_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪक")]
bstack111l1ll_opy_ = bstack111l_opy_ (u"ࠩࡖࡩࡹࡺࡩ࡯ࡩࠣࡹࡵࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠮ࠣࡹࡸ࡯࡮ࡨࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠿ࠦࡻࡾࠩख")
bstack1lllll_opy_ = bstack111l_opy_ (u"ࠪࡇࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡳࡦࡶࡸࡴࠦ࠭ग")
bstack1lll11_opy_ = bstack111l_opy_ (u"ࠫࡕࡧࡲࡴࡧࡧࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂ࠭घ")
bstack1ll11l1_opy_ = bstack111l_opy_ (u"࡛ࠬࡳࡪࡰࡪࠤ࡭ࡻࡢࠡࡷࡵࡰ࠿ࠦࡻࡾࠩङ")
bstack11l1l1l_opy_ = bstack111l_opy_ (u"࠭ࡓࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࡿࢂ࠭च")
bstack111lll_opy_ = bstack111l_opy_ (u"ࠧࡓࡧࡦࡩ࡮ࡼࡥࡥࠢ࡬ࡲࡹ࡫ࡲࡳࡷࡳࡸ࠱ࠦࡥࡹ࡫ࡷ࡭ࡳ࡭ࠧछ")
bstack1111l1l_opy_ = bstack111l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡶࡩࡱ࡫࡮ࡪࡷࡰࠤࡹࡵࠠࡳࡷࡱࠤࡹ࡫ࡳࡵࡵ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࡥ࠭ज")
bstack1lll11l_opy_ = bstack111l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡶࡴࡨ࡯ࡵࠢࡤࡲࡩࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࡭࡫ࡥࡶࡦࡸࡹࠡࡲࡤࡧࡰࡧࡧࡦࡵࠣࡸࡴࠦࡲࡶࡰࠣࡶࡴࡨ࡯ࡵࠢࡷࡩࡸࡺࡳ࠯ࠢࡣࡴ࡮ࡶࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡴࡲࡦࡴࡺࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢࡵࡳࡧࡵࡴࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠰ࡷࡪࡲࡥ࡯࡫ࡸࡱࡱ࡯ࡢࡳࡣࡵࡽࡥ࠭झ")
bstack11ll11l_opy_ = bstack111l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡷࡵࡢࡰࡶ࠯ࠤࡵࡧࡢࡰࡶࠣࡥࡳࡪࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࡮࡬ࡦࡷࡧࡲࡺࠢࡳࡥࡨࡱࡡࡨࡧࡶࠤࡹࡵࠠࡳࡷࡱࠤࡷࡵࡢࡰࡶࠣࡸࡪࡹࡴࡴࠢ࡬ࡲࠥࡶࡡࡳࡣ࡯ࡰࡪࡲ࠮ࠡࡢࡳ࡭ࡵࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡳࡱࡥࡳࡹ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠡࡴࡲࡦࡴࡺࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠯ࡳࡥࡧࡵࡴࠡࡴࡲࡦࡴࡺࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠯ࡶࡩࡱ࡫࡮ࡪࡷࡰࡰ࡮ࡨࡲࡢࡴࡼࡤࠬञ")
bstack111ll11_opy_ = bstack111l_opy_ (u"ࠫࡍࡧ࡮ࡥ࡮࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤ࡮ࡲࡷࡪ࠭ट")
bstack11ll111_opy_ = bstack111l_opy_ (u"ࠬࡇ࡬࡭ࠢࡧࡳࡳ࡫ࠡࠨठ")
bstack1l1l1l_opy_ = bstack111l_opy_ (u"࠭ࡃࡰࡰࡩ࡭࡬ࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸࠥࡧࡴࠡࠤࡾࢁࠧ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡦࡰࡺࡪࡥࠡࡣࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮࡭ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࡵ࠱ࠫड")
bstack1l1l1l1_opy_ = bstack111l_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡣࡳࡧࡧࡩࡳࡺࡩࡢ࡮ࡶࠤࡳࡵࡴࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡦࡪࡤࠡࡶ࡫ࡩࡲࠦࡩ࡯ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬ࡩ࡭ࡧࠣࡥࡸࠦࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤࠣࡥࡳࡪࠠࠣࡣࡦࡧࡪࡹࡳࡌࡧࡼࠦࠥࡵࡲࠡࡵࡨࡸࠥࡺࡨࡦ࡯ࠣࡥࡸࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷࠤࡻࡧࡲࡪࡣࡥࡰࡪࡹ࠺ࠡࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠥࠤࡦࡴࡤࠡࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠧ࠭ढ")
bstack1l1111_opy_ = bstack111l_opy_ (u"ࠨࡏࡤࡰ࡫ࡵࡲ࡮ࡧࡧࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡫࡯࡬ࡦ࠼ࠥࡿࢂࠨࠧण")
bstack1llll1l1_opy_ = bstack111l_opy_ (u"ࠩࡈࡲࡨࡵࡵ࡯ࡶࡨࡶࡪࡪࠠࡦࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡵࡱࠢ࠰ࠤࢀࢃࠧत")
bstack1lllllll_opy_ = bstack111l_opy_ (u"ࠪࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡑࡵࡣࡢ࡮ࠪथ")
bstack11l1l1_opy_ = bstack111l_opy_ (u"ࠫࡘࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡒ࡯ࡤࡣ࡯ࠫद")
bstack1l1111l_opy_ = bstack111l_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡑࡵࡣࡢ࡮ࠣ࡭ࡸࠦ࡮ࡰࡹࠣࡶࡺࡴ࡮ࡪࡰࡪࠥࠬध")
bstack1l1ll11_opy_ = bstack111l_opy_ (u"࠭ࡃࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡶࡸࡦࡸࡴࠡࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱࡀࠠࡼࡿࠪन")
bstack1l11111_opy_ = bstack111l_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡯࡮ࡨࠢ࡯ࡳࡨࡧ࡬ࠡࡤ࡬ࡲࡦࡸࡹࠡࡹ࡬ࡸ࡭ࠦ࡯ࡱࡶ࡬ࡳࡳࡹ࠺ࠡࡽࢀࠫऩ")
bstack111ll_opy_ = bstack111l_opy_ (u"ࠨࡗࡳࡨࡦࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠿ࠦࡻࡾࠩप")
bstack1lll1l11_opy_ = bstack111l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡻࡰࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷࠥࢁࡽࠨफ")
bstack1llllll1_opy_ = bstack111l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡴࡷࡵࡶࡪࡦࡨࠤࡦࡴࠠࡢࡲࡳࡶࡴࡶࡲࡪࡣࡷࡩࠥࡌࡗࠡࠪࡵࡳࡧࡵࡴ࠰ࡲࡤࡦࡴࡺࠩࠡ࡫ࡱࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡫࡯࡬ࡦ࠮ࠣࡷࡰ࡯ࡰࠡࡶ࡫ࡩࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠡ࡭ࡨࡽࠥ࡯࡮ࠡࡥࡲࡲ࡫࡯ࡧࠡ࡫ࡩࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡹࡩ࡮ࡲ࡯ࡩࠥࡶࡹࡵࡪࡲࡲࠥࡹࡣࡳ࡫ࡳࡸࠥࡽࡩࡵࡪࡲࡹࡹࠦࡡ࡯ࡻࠣࡊ࡜࠴ࠧब")
bstack1ll111l_opy_ = bstack111l_opy_ (u"ࠫࡘ࡫ࡴࡵ࡫ࡱ࡫ࠥ࡮ࡴࡵࡲࡓࡶࡴࡾࡹ࠰ࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡱࡱࠤࡨࡻࡲࡳࡧࡱࡸࡱࡿࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠣࡺࡪࡸࡳࡪࡱࡱࠤࡴ࡬ࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࠫࡿࢂ࠯ࠬࠡࡲ࡯ࡩࡦࡹࡥࠡࡷࡳ࡫ࡷࡧࡤࡦࠢࡷࡳ࡙ࠥࡥ࡭ࡧࡱ࡭ࡺࡳ࠾࠾࠶࠱࠴࠳࠶ࠠࡰࡴࠣࡶࡪ࡬ࡥࡳࠢࡷࡳࠥ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡷࡸࡹ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡤࡰࡥࡶ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠰ࡴࡸࡲ࠲ࡺࡥࡴࡶࡶ࠱ࡧ࡫ࡨࡪࡰࡧ࠱ࡵࡸ࡯ࡹࡻࠦࡴࡾࡺࡨࡰࡰࠣࡪࡴࡸࠠࡢࠢࡺࡳࡷࡱࡡࡳࡱࡸࡲࡩ࠴ࠧभ")
__version__ = bstack111l_opy_ (u"ࠬ࠷࠮࠱࠰࠵ࠫम")
bstack1ll1lll_opy_ = None
bstack1lll1111_opy_ = {}
bstack1111ll_opy_ = None
bstack1lll1ll1_opy_ = None
bstack1llll111_opy_ = None
bstack1llll1_opy_ = -1
bstack11l111l_opy_ = DEFAULT_LOG_LEVEL
bstack1lll11ll_opy_ = 1
bstack11ll1l_opy_ = False
bstack1111l1_opy_ = bstack111l_opy_ (u"࠭ࠧय")
bstack11l1lll_opy_ = None
bstack11111l_opy_ = None
bstack11l111_opy_ = None
bstack1llll1ll_opy_ = None
bstack11lll1l_opy_ = None
bstack111llll_opy_ = None
bstack111l1l1_opy_ = None
bstack1lll111_opy_ = None
bstack1l1ll1l_opy_ = None
logger = logging.getLogger(__name__)
def bstack1ll1l1_opy_():
  global bstack1lll1111_opy_
  global bstack11l111l_opy_
  if bstack111l_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩर") in bstack1lll1111_opy_:
    bstack11l111l_opy_ = bstack1l111_opy_[bstack1lll1111_opy_[bstack111l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪऱ")]]
  logging.basicConfig(level=bstack11l111l_opy_,
                      format=bstack111l_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧल"),
                      datefmt=bstack111l_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬळ"))
def bstack111l11l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1lll11l1_opy_():
  bstack1ll1111_opy_ = bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧऴ")
  bstack1111lll_opy_ = os.path.abspath(bstack1ll1111_opy_)
  if not os.path.exists(bstack1111lll_opy_):
    bstack1ll1111_opy_ = bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡧ࡭࡭ࠩव")
    bstack1111lll_opy_ = os.path.abspath(bstack1ll1111_opy_)
    if not os.path.exists(bstack1111lll_opy_):
      bstack1lll1lll_opy_(
        bstack1l1l1l_opy_.format(os.getcwd()))
  with open(bstack1111lll_opy_, bstack111l_opy_ (u"࠭ࡲࠨश")) as stream:
    try:
      config = yaml.safe_load(stream)
      return config
    except yaml.YAMLError as exc:
      bstack1lll1lll_opy_(bstack1l1111_opy_.format(str(exc)))
def bstack1l11ll1_opy_(config):
  bstack111l111_opy_ = config.keys()
  bstack11111_opy_ = []
  if bstack111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪष") in config:
    bstack11111_opy_ = config[bstack111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫस")]
  for bstack1l1l1ll_opy_, bstack11llll_opy_ in bstack1l1l_opy_.items():
    if bstack11llll_opy_ in bstack111l111_opy_:
      config[bstack1l1l1ll_opy_] = config[bstack11llll_opy_]
      del config[bstack11llll_opy_]
  for bstack1l1l1ll_opy_, bstack11llll_opy_ in bstack1l_opy_.items():
    for platform in bstack11111_opy_:
      if isinstance(bstack11llll_opy_, list):
        for bstack1lll1ll_opy_ in bstack11llll_opy_:
          if bstack1lll1ll_opy_ in platform:
            platform[bstack1l1l1ll_opy_] = platform[bstack1lll1ll_opy_]
            del platform[bstack1lll1ll_opy_]
            break
      elif bstack11llll_opy_ in platform:
        platform[bstack1l1l1ll_opy_] = platform[bstack11llll_opy_]
        del platform[bstack11llll_opy_]
  for bstack1l1l1ll_opy_, bstack11llll_opy_ in bstack1lll1_opy_.items():
    for bstack1lll1ll_opy_ in bstack11llll_opy_:
      if bstack1lll1ll_opy_ in bstack111l111_opy_:
        config[bstack1l1l1ll_opy_] = config[bstack1lll1ll_opy_]
        del config[bstack1lll1ll_opy_]
  for bstack1lll1ll_opy_ in list(config):
    for bstack11l1ll_opy_ in bstack1l11l_opy_:
      if bstack1lll1ll_opy_.lower() == bstack11l1ll_opy_.lower():
        config[bstack11l1ll_opy_] = config[bstack1lll1ll_opy_]
        del config[bstack1lll1ll_opy_]
  return config
def bstack1l11ll_opy_(config):
  if bstack111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬह") in config and config[bstack111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ऺ")] not in bstack11ll_opy_:
    return config[bstack111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧऻ")]
  elif bstack111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨ़") in os.environ:
    return os.environ[bstack111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩऽ")]
  else:
    return None
def bstack1l1llll_opy_(config):
  if bstack111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪा") in config:
    return config[bstack111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫि")]
  elif bstack111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠬी") in os.environ:
    return os.environ[bstack111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡐࡄࡑࡊ࠭ु")]
  else:
    return None
def bstack1ll1l1l_opy_(config):
  if bstack111l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ू") in config and config[bstack111l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧृ")] not in bstack1llll_opy_:
    return config[bstack111l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨॄ")]
  elif bstack111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨॅ") in os.environ:
    return os.environ[bstack111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩॆ")]
  else:
    return None
def bstack1ll1lll1_opy_(config):
  if not bstack1ll1l1l_opy_(config) or not bstack1l11ll_opy_(config):
    return True
  else:
    return False
def bstack11l1111_opy_(config):
  if bstack111l11l_opy_() < version.parse(bstack111l_opy_ (u"ࠩ࠶࠲࠹࠴࠰ࠨे")):
    return False
  if bstack111l11l_opy_() >= version.parse(bstack111l_opy_ (u"ࠪ࠸࠳࠷࠮࠶ࠩै")):
    return True
  if bstack111l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫॉ") in config and config[bstack111l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬॊ")] == False:
    return False
  else:
    return True
def bstack11l11l1_opy_(config, index = 0):
  bstack11ll1ll_opy_ = {}
  if bstack111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩो") in config:
    for bstack11l11ll_opy_ in config[bstack111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪौ")][index]:
      if bstack11l11ll_opy_ in bstack1l1ll_opy_ + bstack1lll_opy_ + [bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ्࠭"), bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪॎ")]:
        continue
      bstack11ll1ll_opy_[bstack11l11ll_opy_] = config[bstack111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ॏ")][index][bstack11l11ll_opy_]
  for key in config:
    if key in bstack1l1ll_opy_ + bstack1lll_opy_ + [bstack111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧॐ")]:
      continue
    bstack11ll1ll_opy_[key] = config[key]
  return bstack11ll1ll_opy_
def bstack1lllll1_opy_(config):
  bstack111l1_opy_ = {}
  for key in bstack1lll_opy_:
    if key in config:
      bstack111l1_opy_[key] = config[key]
  return bstack111l1_opy_
def bstack1l11lll_opy_(bstack11ll1ll_opy_, bstack111l1_opy_):
  bstack1111l11_opy_ = {}
  for key in bstack11ll1ll_opy_.keys():
    if key in bstack1l1l_opy_:
      bstack1111l11_opy_[bstack1l1l_opy_[key]] = bstack11ll1ll_opy_[key]
    else:
      bstack1111l11_opy_[key] = bstack11ll1ll_opy_[key]
  for key in bstack111l1_opy_:
    if key in bstack1l1l_opy_:
      bstack1111l11_opy_[bstack1l1l_opy_[key]] = bstack111l1_opy_[key]
    else:
      bstack1111l11_opy_[key] = bstack111l1_opy_[key]
  return bstack1111l11_opy_
def bstack1l111l_opy_(config, index = 0):
  caps = {}
  bstack111l1_opy_ = bstack1lllll1_opy_(config)
  if bstack111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ॑") in config:
    if bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨ॒ࠫ") in config[bstack111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ॓")][index]:
      caps[bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭॔")] = config[bstack111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬॕ")][index][bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨॖ")]
    if bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬॗ") in config[bstack111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨक़")][index]:
      caps[bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧख़")] = str(config[bstack111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪग़")][index][bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩज़")])
    bstack11lll1_opy_ = {}
    for bstack11l11l_opy_ in bstack1lll_opy_:
      if bstack11l11l_opy_ in config[bstack111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬड़")][index]:
        bstack11lll1_opy_[bstack11l11l_opy_] = config[bstack111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ढ़")][index][bstack11l11l_opy_]
        del(config[bstack111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧफ़")][index][bstack11l11l_opy_])
    bstack111l1_opy_.update(bstack11lll1_opy_)
  bstack11ll1ll_opy_ = bstack11l11l1_opy_(config, index)
  if bstack11l1111_opy_(config):
    bstack11ll1ll_opy_[bstack111l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬय़")] = True
    caps.update(bstack111l1_opy_)
    caps[bstack111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧॠ")] = bstack11ll1ll_opy_
  else:
    bstack11ll1ll_opy_[bstack111l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧॡ")] = False
    caps.update(bstack1l11lll_opy_(bstack11ll1ll_opy_, bstack111l1_opy_))
    if bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ॢ") in caps:
      caps[bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪॣ")] = caps[bstack111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ।")]
      del(caps[bstack111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ॥")])
    if bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭०") in caps:
      caps[bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ१")] = caps[bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ२")]
      del(caps[bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ३")])
  return caps
def bstack1ll1ll_opy_():
  if bstack111l11l_opy_() <= version.parse(bstack111l_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ४")):
    return bstack1l11_opy_
  return bstack11ll1_opy_
def bstack11ll1l1_opy_(options):
  return hasattr(options, bstack111l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫ५"))
def bstack1ll1ll1_opy_(caps):
  browser = bstack111l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ६")
  if bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ७") in caps:
    browser = caps[bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ८")]
  elif bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ९") in caps:
    browser = caps[bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ॰")]
  browser = str(browser).lower()
  if browser == bstack111l_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩॱ") or browser == bstack111l_opy_ (u"ࠪ࡭ࡵࡧࡤࠨॲ"):
    browser = bstack111l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫॳ")
  if browser == bstack111l_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭ॴ"):
    browser = bstack111l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ॵ")
  if browser not in [bstack111l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧॶ"), bstack111l_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭ॷ"), bstack111l_opy_ (u"ࠩ࡬ࡩࠬॸ"), bstack111l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪॹ"), bstack111l_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬॺ")]:
    return None
  package = bstack111l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧॻ").format(browser)
  name = bstack111l_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧॼ")
  browser_options = getattr(__import__(package, fromlist=[name]), name)
  options = browser_options()
  for bstack1lll1ll_opy_ in caps.keys():
    options.set_capability(bstack1lll1ll_opy_, caps[bstack1lll1ll_opy_])
  return options
def bstack1lllll11_opy_(options, bstack11ll11_opy_):
  if not bstack11ll1l1_opy_(options):
    return
  for bstack1lll1ll_opy_ in bstack11ll11_opy_.keys():
    options.set_capability(bstack1lll1ll_opy_, bstack11ll11_opy_[bstack1lll1ll_opy_])
  if bstack111l_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ॽ") in options._caps:
    if options._caps[bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ॾ")] and options._caps[bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧॿ")].lower() != bstack111l_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫঀ"):
      del options._caps[bstack111l_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪঁ")]
def bstack111lll1_opy_(proxy_config):
  if bstack111l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩং") in proxy_config:
    proxy_config[bstack111l_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨঃ")] = proxy_config[bstack111l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ঄")]
    del(proxy_config[bstack111l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬঅ")])
  if bstack111l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬআ") in proxy_config and proxy_config[bstack111l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ই")].lower() != bstack111l_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫঈ"):
    proxy_config[bstack111l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨউ")] = bstack111l_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭ঊ")
  if bstack111l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬঋ") in proxy_config:
    proxy_config[bstack111l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫঌ")] = bstack111l_opy_ (u"ࠩࡳࡥࡨ࠭঍")
  return proxy_config
def bstack1llll11l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ঎") in config:
    return proxy
  config[bstack111l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪএ")] = bstack111lll1_opy_(config[bstack111l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫঐ")])
  if proxy == None:
    proxy = Proxy(config[bstack111l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ঑")])
  return proxy
def bstack11l1l11_opy_(self):
  global bstack1lll1111_opy_
  global bstack1lll111_opy_
  if bstack111l_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ঒") in bstack1lll1111_opy_ and bstack1ll1ll_opy_().startswith(bstack111l_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࠩও")):
    return bstack1lll1111_opy_[bstack111l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬঔ")]
  elif bstack111l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧক") in bstack1lll1111_opy_ and bstack1ll1ll_opy_().startswith(bstack111l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭খ")):
    return bstack1lll1111_opy_[bstack111l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩগ")]
  else:
    return bstack1lll111_opy_(self)
def bstack1ll11l_opy_():
  if bstack111l11l_opy_() < version.parse(bstack111l_opy_ (u"࠭࠴࠯࠲࠱࠴ࠬঘ")):
    logger.warning(bstack1ll111l_opy_.format(bstack111l11l_opy_()))
    return
  global bstack1lll111_opy_
  from selenium.webdriver.remote.remote_connection import RemoteConnection
  bstack1lll111_opy_ = RemoteConnection._get_proxy_url
  RemoteConnection._get_proxy_url = bstack11l1l11_opy_
def bstack11lll11_opy_(config):
  if bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫঙ") in config:
    if str(config[bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬচ")]).lower() == bstack111l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧছ"):
      return True
    else:
      return False
  elif bstack111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࠨজ") in os.environ:
    if str(os.environ[bstack111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࠩঝ")]).lower() == bstack111l_opy_ (u"ࠬࡺࡲࡶࡧࠪঞ"):
      return True
    else:
      return False
  else:
    return False
def bstack111111_opy_(config):
  if bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪট") in config:
    return config[bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫঠ")]
  if bstack111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧড") in config:
    return config[bstack111l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨঢ")]
  return {}
def bstack1l11l1_opy_(caps, bstack1lll1l1_opy_):
  if bstack111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫণ") in caps:
    caps[bstack111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬত")][bstack111l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫথ")] = True
    if bstack111l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨদ") in bstack1lll1l1_opy_:
      caps[bstack111l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨধ")][bstack111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪন")] = bstack1lll1l1_opy_[bstack111l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ঩")]
    elif bstack111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬপ") in os.environ:
      caps[bstack111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬফ")][bstack111l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧব")] = os.environ[bstack111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨভ")]
  else:
    caps[bstack111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬম")] = True
    if bstack111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪয") in bstack1lll1l1_opy_:
      caps[bstack111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪর")] = bstack1lll1l1_opy_[bstack111l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ঱")]
    elif bstack111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ল") in os.environ:
      caps[bstack111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭঳")] = os.environ[bstack111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ঴")]
def bstack1l111l1_opy_():
  global bstack1lll1111_opy_
  if bstack11lll11_opy_(bstack1lll1111_opy_):
    bstack1lll1l1_opy_ = bstack111111_opy_(bstack1lll1111_opy_)
    bstack1ll111_opy_(bstack1l11ll_opy_(bstack1lll1111_opy_), bstack1lll1l1_opy_)
def bstack1ll111_opy_(key, bstack1lll1l1_opy_):
  global bstack1ll1lll_opy_
  logger.info(bstack1lllllll_opy_)
  try:
    bstack1ll1lll_opy_ = Local()
    bstack1llll1l_opy_ = {bstack111l_opy_ (u"ࠧ࡬ࡧࡼࠫ঵"): key}
    bstack1llll1l_opy_.update(bstack1lll1l1_opy_)
    logger.debug(bstack1l11111_opy_.format(str(bstack1llll1l_opy_)))
    bstack1ll1lll_opy_.start(**bstack1llll1l_opy_)
    if bstack1ll1lll_opy_.isRunning():
      logger.info(bstack1l1111l_opy_)
  except Exception as e:
    bstack1lll1lll_opy_(bstack1l1ll11_opy_.format(str(e)))
def bstack1l1l111_opy_():
  global bstack1ll1lll_opy_
  if bstack1ll1lll_opy_.isRunning():
    logger.info(bstack11l1l1_opy_)
    bstack1ll1lll_opy_.stop()
  bstack1ll1lll_opy_ = None
def bstack1l1lll_opy_():
  logger.info(bstack111ll11_opy_)
  global bstack1ll1lll_opy_
  if bstack1ll1lll_opy_:
    bstack1l1l111_opy_()
  logger.info(bstack11ll111_opy_)
def bstack11lllll_opy_(self, *args):
  logger.error(bstack111lll_opy_)
  bstack1l1lll_opy_()
def bstack1lll1lll_opy_(err):
  logger.critical(bstack1llll1l1_opy_.format(str(err)))
  atexit.unregister(bstack1l1lll_opy_)
  sys.exit(1)
def bstack111l11_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  atexit.unregister(bstack1l1lll_opy_)
  sys.exit(1)
def bstack1111l_opy_():
  global bstack1lll1111_opy_
  bstack1lll1111_opy_ = bstack1lll11l1_opy_()
  bstack1lll1111_opy_ = bstack1l11ll1_opy_(bstack1lll1111_opy_)
  if bstack1ll1lll1_opy_(bstack1lll1111_opy_):
    bstack1lll1lll_opy_(bstack1l1l1l1_opy_)
  bstack1lll1111_opy_[bstack111l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪশ")] = bstack1ll1l1l_opy_(bstack1lll1111_opy_)
  bstack1lll1111_opy_[bstack111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬষ")] = bstack1l11ll_opy_(bstack1lll1111_opy_)
  if bstack1l1llll_opy_(bstack1lll1111_opy_):
    bstack1lll1111_opy_[bstack111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭স")] = bstack1l1llll_opy_(bstack1lll1111_opy_)
  bstack111111l_opy_()
def bstack111111l_opy_():
  global bstack1lll1111_opy_
  global bstack1lll11ll_opy_
  bstack111ll1l_opy_ = 1
  if bstack111l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫহ") in bstack1lll1111_opy_:
    bstack111ll1l_opy_ = bstack1lll1111_opy_[bstack111l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ঺")]
  bstack11111ll_opy_ = 0
  if bstack111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ঻") in bstack1lll1111_opy_:
    bstack11111ll_opy_ = len(bstack1lll1111_opy_[bstack111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ়ࠪ")])
  bstack1lll11ll_opy_ = int(bstack111ll1l_opy_) * int(bstack11111ll_opy_)
def bstack11llll1_opy_(self):
  return
def bstack1l1ll1_opy_(self):
  return
def bstack1l111ll_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack1llllll_opy_(self, command_executor,
        desired_capabilities=None, browser_profile=None, proxy=None,
        keep_alive=True, file_detector=None, options=None):
  global bstack1lll1111_opy_
  global bstack1111ll_opy_
  global bstack1llll1_opy_
  global bstack1llll111_opy_
  global bstack11ll1l_opy_
  global bstack1111l1_opy_
  global bstack11l1lll_opy_
  bstack1lll1111_opy_[bstack111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪঽ")] = str(bstack1111l1_opy_) + str(__version__)
  command_executor = bstack1ll1ll_opy_()
  logger.debug(bstack1ll11l1_opy_.format(command_executor))
  proxy = bstack1llll11l_opy_(bstack1lll1111_opy_, proxy)
  bstack1lll1l_opy_ = 0 if bstack1llll1_opy_ < 0 else bstack1llll1_opy_
  if bstack11ll1l_opy_ is True:
    bstack1lll1l_opy_ = int(threading.current_thread().getName())
  bstack11ll11_opy_ = bstack1l111l_opy_(bstack1lll1111_opy_, bstack1lll1l_opy_)
  logger.debug(bstack1lll11_opy_.format(str(bstack11ll11_opy_)))
  if bstack11lll11_opy_(bstack1lll1111_opy_):
    bstack1lll1l1_opy_ = bstack111111_opy_(bstack1lll1111_opy_)
    bstack1l11l1_opy_(bstack11ll11_opy_, bstack1lll1l1_opy_)
  if options:
    bstack1lllll11_opy_(options, bstack11ll11_opy_)
  if desired_capabilities:
    if bstack111l11l_opy_() >= version.parse(bstack111l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨা")):
      desired_capabilities = {}
    else:
      desired_capabilities.update(bstack11ll11_opy_)
  if not options:
    options = bstack1ll1ll1_opy_(bstack11ll11_opy_)
  if (
      not options and not desired_capabilities
  ) or (
      bstack111l11l_opy_() < version.parse(bstack111l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩি")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11ll11_opy_)
  logger.info(bstack1lllll_opy_)
  if bstack111l11l_opy_() >= version.parse(bstack111l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪী")):
    bstack11l1lll_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities, options=options,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  elif bstack111l11l_opy_() >= version.parse(bstack111l_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬু")):
    bstack11l1lll_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11l1lll_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive)
  bstack1111ll_opy_ = self.session_id
  if bstack111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩূ") in bstack1lll1111_opy_ and bstack111l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬৃ") in bstack1lll1111_opy_[bstack111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৄ")][bstack1lll1l_opy_]:
    bstack1llll111_opy_ = bstack1lll1111_opy_[bstack111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৅")][bstack1lll1l_opy_][bstack111l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ৆")]
  logger.debug(bstack11l1l1l_opy_.format(bstack1111ll_opy_))
def bstack1ll1l11_opy_(self, test):
  global bstack1lll1111_opy_
  global bstack1111ll_opy_
  global bstack1lll1ll1_opy_
  global bstack1llll111_opy_
  global bstack11111l_opy_
  if bstack1111ll_opy_:
    try:
      data = {}
      bstack1l11l11_opy_ = None
      if test:
        bstack1l11l11_opy_ = str(test.data)
      if bstack1l11l11_opy_ and not bstack1llll111_opy_:
        data[bstack111l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩে")] = bstack1l11l11_opy_
      if bstack1lll1ll1_opy_:
        if bstack1lll1ll1_opy_.status == bstack111l_opy_ (u"ࠬࡖࡁࡔࡕࠪৈ"):
          data[bstack111l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭৉")] = bstack111l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ৊")
        elif bstack1lll1ll1_opy_.status == bstack111l_opy_ (u"ࠨࡈࡄࡍࡑ࠭ো"):
          data[bstack111l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩৌ")] = bstack111l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦ্ࠪ")
          if bstack1lll1ll1_opy_.message:
            data[bstack111l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫৎ")] = str(bstack1lll1ll1_opy_.message)
      user = bstack1lll1111_opy_[bstack111l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ৏")]
      key = bstack1lll1111_opy_[bstack111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ৐")]
      url = bstack111l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠳ࢀࢃ࠮࡫ࡵࡲࡲࠬ৑").format(user, key, bstack1111ll_opy_)
      headers = {
        bstack111l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧ৒"): bstack111l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ৓"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1lll1l11_opy_.format(str(e)))
  bstack11111l_opy_(self, test)
def bstack1111ll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l111_opy_
  bstack11l111_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1lll1ll1_opy_
  bstack1lll1ll1_opy_ = self._test
def bstack1111111_opy_(outs_dir, options, tests_root_name, stats, copied_artifacts, outputfile=None):
  from pabot import pabot
  outputfile = outputfile or options.get(bstack111l_opy_ (u"ࠥࡳࡺࡺࡰࡶࡶࠥ৔"), bstack111l_opy_ (u"ࠦࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠣ৕"))
  output_path = os.path.abspath(
    os.path.join(options.get(bstack111l_opy_ (u"ࠧࡵࡵࡵࡲࡸࡸࡩ࡯ࡲࠣ৖"), bstack111l_opy_ (u"ࠨ࠮ࠣৗ")), outputfile)
  )
  files = sorted(pabot.glob(os.path.join(pabot._glob_escape(outs_dir), bstack111l_opy_ (u"ࠢࠫ࠰ࡻࡱࡱࠨ৘"))))
  if not files:
    pabot._write(bstack111l_opy_ (u"ࠨ࡙ࡄࡖࡓࡀࠠࡏࡱࠣࡳࡺࡺࡰࡶࡶࠣࡪ࡮ࡲࡥࡴࠢ࡬ࡲࠥࠨࠥࡴࠤࠪ৙") % outs_dir, pabot.Color.YELLOW)
    return bstack111l_opy_ (u"ࠤࠥ৚")
  def invalid_xml_callback():
    global _ABNORMAL_EXIT_HAPPENED
    _ABNORMAL_EXIT_HAPPENED = True
  resu = pabot.merge(
    files, options, tests_root_name, copied_artifacts, invalid_xml_callback
  )
  pabot._update_stats(resu, stats)
  resu.save(output_path)
  return output_path
def bstack111ll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  from pabot import pabot
  from robot import __version__ as ROBOT_VERSION
  from robot import rebot
  if bstack111l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢ৛") in options:
    del options[bstack111l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣড়")]
  if ROBOT_VERSION < bstack111l_opy_ (u"ࠧ࠺࠮࠱ࠤঢ়"):
    stats = {
      bstack111l_opy_ (u"ࠨࡣࡳ࡫ࡷ࡭ࡨࡧ࡬ࠣ৞"): {bstack111l_opy_ (u"ࠢࡵࡱࡷࡥࡱࠨয়"): 0, bstack111l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣৠ"): 0, bstack111l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤৡ"): 0},
      bstack111l_opy_ (u"ࠥࡥࡱࡲࠢৢ"): {bstack111l_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࠥৣ"): 0, bstack111l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ৤"): 0, bstack111l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ৥"): 0},
    }
  else:
    stats = {
      bstack111l_opy_ (u"ࠢࡵࡱࡷࡥࡱࠨ০"): 0,
      bstack111l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ১"): 0,
      bstack111l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ২"): 0,
      bstack111l_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠦ৩"): 0,
    }
  if pabot_args[bstack111l_opy_ (u"ࠦࡇ࡙ࡔࡂࡅࡎࡣࡕࡇࡒࡂࡎࡏࡉࡑࡥࡒࡖࡐࠥ৪")]:
    outputs = []
    for index, _ in enumerate(pabot_args[bstack111l_opy_ (u"ࠧࡈࡓࡕࡃࡆࡏࡤࡖࡁࡓࡃࡏࡐࡊࡒ࡟ࡓࡗࡑࠦ৫")]):
      copied_artifacts = pabot._copy_output_artifacts(
        options, pabot_args[bstack111l_opy_ (u"ࠨࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠤ৬")], pabot_args[bstack111l_opy_ (u"ࠢࡢࡴࡷ࡭࡫ࡧࡣࡵࡵ࡬ࡲࡸࡻࡢࡧࡱ࡯ࡨࡪࡸࡳࠣ৭")]
      )
      outputs += [
        bstack1111111_opy_(
          os.path.join(outs_dir, str(index)+ bstack111l_opy_ (u"ࠣ࠱ࠥ৮")),
          options,
          tests_root_name,
          stats,
          copied_artifacts,
          outputfile=os.path.join(bstack111l_opy_ (u"ࠤࡳࡥࡧࡵࡴࡠࡴࡨࡷࡺࡲࡴࡴࠤ৯"), bstack111l_opy_ (u"ࠥࡳࡺࡺࡰࡶࡶࠨࡷ࠳ࡾ࡭࡭ࠤৰ") % index),
        )
      ]
    if bstack111l_opy_ (u"ࠦࡴࡻࡴࡱࡷࡷࠦৱ") not in options:
      options[bstack111l_opy_ (u"ࠧࡵࡵࡵࡲࡸࡸࠧ৲")] = bstack111l_opy_ (u"ࠨ࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠥ৳")
    pabot._write_stats(stats)
    return rebot(*outputs, **pabot._options_for_rebot(options, start_time_string, pabot._now()))
  else:
    return pabot._report_results(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1lll111l_opy_(self, ff_profile_dir):
  global bstack1llll1ll_opy_
  if not ff_profile_dir:
    return None
  return bstack1llll1ll_opy_(self, ff_profile_dir)
def bstack11l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global bstack1lll1111_opy_
  bstack1ll1llll_opy_ = []
  if bstack111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৴") in bstack1lll1111_opy_:
    bstack1ll1llll_opy_ = bstack1lll1111_opy_[bstack111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৵")]
  bstack11111l1_opy_ = len(suite_group) * len(pabot_args[bstack111l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡪ࡮ࡲࡥࡴࠤ৶")] or [(bstack111l_opy_ (u"ࠥࠦ৷"), None)]) * len(bstack1ll1llll_opy_)
  pabot_args[bstack111l_opy_ (u"ࠦࡇ࡙ࡔࡂࡅࡎࡣࡕࡇࡒࡂࡎࡏࡉࡑࡥࡒࡖࡐࠥ৸")] = []
  for q in range(bstack11111l1_opy_):
    pabot_args[bstack111l_opy_ (u"ࠧࡈࡓࡕࡃࡆࡏࡤࡖࡁࡓࡃࡏࡐࡊࡒ࡟ࡓࡗࡑࠦ৹")].append(str(q))
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࠢ৺")],
      pabot_args[bstack111l_opy_ (u"ࠢࡷࡧࡵࡦࡴࡹࡥࠣ৻")],
      argfile,
      pabot_args.get(bstack111l_opy_ (u"ࠣࡪ࡬ࡺࡪࠨৼ")),
      pabot_args[bstack111l_opy_ (u"ࠤࡳࡶࡴࡩࡥࡴࡵࡨࡷࠧ৽")],
      platform[0]
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111l_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࡫࡯࡬ࡦࡵࠥ৾")] or [(bstack111l_opy_ (u"ࠦࠧ৿"), None)]
    for platform in enumerate(bstack1ll1llll_opy_)
  ]
def bstack1l1lll1_opy_(self, datasources, outs_dir, options,
  execution_item, command, verbose, argfile,
  hive=None, processes=0,platform_index=0):
  global bstack111llll_opy_
  self.platform_index = platform_index
  bstack111llll_opy_(self, datasources, outs_dir, options,
    execution_item, command, verbose, argfile, hive, processes)
def bstack1l11l1l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack111l1l1_opy_
  if not bstack111l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ਀") in item.options:
    item.options[bstack111l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨਁ")] = []
  for v in item.options[bstack111l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩਂ")]:
    if bstack111l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧਃ") in v:
      item.options[bstack111l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ਄")].remove(v)
  item.options[bstack111l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬਅ")].insert(0, bstack111l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚࠽ࡿࢂ࠭ਆ").format(item.platform_index))
  return bstack111l1l1_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11lll1l_opy_
  command[0] = command[0].replace(bstack111l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫਇ"), bstack111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪਈ"), 1)
  return bstack11lll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1l1l11_opy_(bstack1lll1l1l_opy_):
  global bstack1111l1_opy_
  bstack1111l1_opy_ = bstack1lll1l1l_opy_
  logger.info(bstack111l1ll_opy_.format(bstack1111l1_opy_.split(bstack111l_opy_ (u"ࠧ࠮ࠩਉ"))[0]))
  global bstack11l1lll_opy_
  global bstack11111l_opy_
  global bstack11l111_opy_
  global bstack1llll1ll_opy_
  global bstack11lll1l_opy_
  global bstack111llll_opy_
  global bstack111l1l1_opy_
  global bstack1l1ll1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
  except Exception as e:
    bstack111l11_opy_(e, bstack1111l1l_opy_)
  Service.start = bstack11llll1_opy_
  Service.stop = bstack1l1ll1_opy_
  webdriver.Remote.__init__ = bstack1llllll_opy_
  WebDriver.close = bstack1l111ll_opy_
  if (bstack111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧਊ") in str(bstack1lll1l1l_opy_).lower() or bstack111l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ਋") in str(bstack1lll1l1l_opy_).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
    except Exception as e:
      bstack111l11_opy_(e, bstack1lll11l_opy_)
    Output.end_test = bstack1ll1l11_opy_
    TestStatus.__init__ = bstack1111ll1_opy_
    WebDriverCreator._get_ff_profile = bstack1lll111l_opy_
  if (bstack111l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ਌") in str(bstack1lll1l1l_opy_).lower()):
    try:
      from pabot.pabot import QueueItem
      from pabot import pabot
    except Exception as e:
      bstack111l11_opy_(e, bstack11ll11l_opy_)
    QueueItem.__init__ = bstack1l1lll1_opy_
    pabot._create_items = bstack11l11_opy_
    pabot._run = bstack1ll11ll_opy_
    pabot._create_command_for_execution = bstack1l11l1l_opy_
    pabot._report_results = bstack111ll1_opy_
def bstack111l1l_opy_(bstack11l1ll1_opy_, index):
  bstack1l1l11_opy_(bstack11l_opy_)
  exec(open(bstack11l1ll1_opy_).read())
def bstack1lllll1l_opy_():
  global bstack1lll1111_opy_
  if bool(bstack1lll1111_opy_):
    return
  bstack1111l_opy_()
  bstack1ll1l1_opy_()
  atexit.register(bstack1l1lll_opy_)
  signal.signal(signal.SIGINT, bstack11lllll_opy_)
  signal.signal(signal.SIGTERM, bstack11lllll_opy_)
def run_on_browserstack(args):
  if sys.argv[1] == bstack111l_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧ਍")  or sys.argv[1] == bstack111l_opy_ (u"ࠬ࠳ࡶࠨ਎"):
    print(bstack111l_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ࠭ਏ").format(__version__))
    return
  bstack1lllll1l_opy_()
  global bstack1lll1111_opy_
  global bstack1lll11ll_opy_
  global bstack11ll1l_opy_
  global bstack1llll1_opy_
  bstack1llll11_opy_ = bstack111l_opy_ (u"ࠧࠨਐ")
  if args[1] == bstack111l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ਑") or args[1] == bstack111l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ਒"):
    bstack1llll11_opy_ = bstack111l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪਓ")
    args = args[2:]
  elif args[1] == bstack111l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪਔ"):
    bstack1llll11_opy_ = bstack111l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫਕ")
    args = args[2:]
  elif args[1] == bstack111l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬਖ"):
    bstack1llll11_opy_ = bstack111l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ਗ")
    args = args[2:]
  elif args[1] == bstack111l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩਘ"):
    bstack1llll11_opy_ = bstack111l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪਙ")
    args = args[2:]
  else:
    if not bstack111l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ਚ") in bstack1lll1111_opy_ or str(bstack1lll1111_opy_[bstack111l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧਛ")]).lower() in [bstack111l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬਜ"), bstack111l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧਝ")]:
      bstack1llll11_opy_ = bstack111l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧਞ")
      args = args[1:]
    elif str(bstack1lll1111_opy_[bstack111l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫਟ")]).lower() == bstack111l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨਠ"):
      bstack1llll11_opy_ = bstack111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩਡ")
      args = args[1:]
    elif str(bstack1lll1111_opy_[bstack111l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧਢ")]).lower() == bstack111l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫਣ"):
      bstack1llll11_opy_ = bstack111l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬਤ")
      args = args[1:]
    else:
      bstack1lll1lll_opy_(bstack1llllll1_opy_)
  global bstack11l1lll_opy_
  global bstack11111l_opy_
  global bstack11l111_opy_
  global bstack1llll1ll_opy_
  global bstack11lll1l_opy_
  global bstack111llll_opy_
  global bstack111l1l1_opy_
  global bstack1l1ll1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
  except Exception as e:
    bstack111l11_opy_(e, bstack1111l1l_opy_)
  bstack11l1lll_opy_ = webdriver.Remote.__init__
  bstack1l1ll1l_opy_ = WebDriver.close
  if (bstack1llll11_opy_ in [bstack111l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ਥ"), bstack111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧਦ"), bstack111l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪਧ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
    except Exception as e:
      bstack111l11_opy_(e, bstack1lll11l_opy_)
    bstack11111l_opy_ = Output.end_test
    bstack11l111_opy_ = TestStatus.__init__
    bstack1llll1ll_opy_ = WebDriverCreator._get_ff_profile
  if (bstack1llll11_opy_ in [bstack111l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩਨ"), bstack111l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ਩")]):
    try:
      from pabot.pabot import QueueItem
      from pabot import pabot
    except Exception as e:
      bstack111l11_opy_(e, bstack11ll11l_opy_)
    bstack11lll1l_opy_ = pabot._run
    bstack111llll_opy_ = QueueItem.__init__
    bstack111l1l1_opy_ = pabot._create_command_for_execution
  if bstack1llll11_opy_ == bstack111l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬਪ"):
    bstack1l111l1_opy_()
    if bstack111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਫ") in bstack1lll1111_opy_:
      bstack11ll1l_opy_ = True
      bstack1l1l11l_opy_ = []
      for index, platform in enumerate(bstack1lll1111_opy_[bstack111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਬ")]):
        bstack1l1l11l_opy_.append(threading.Thread(name=str(index),
                                      target=bstack111l1l_opy_, args=(args[0], index)))
      for t in bstack1l1l11l_opy_:
        t.start()
      for t in bstack1l1l11l_opy_:
        t.join()
    else:
      bstack1l1l11_opy_(bstack11l_opy_)
      exec(open(args[0]).read())
  elif bstack1llll11_opy_ == bstack111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧਭ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack111l11_opy_(e, bstack1lll11l_opy_)
    bstack1l111l1_opy_()
    bstack1l1l11_opy_(bstack1111_opy_)
    run_cli(args)
  elif bstack1llll11_opy_ == bstack111l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨਮ"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack111l11_opy_(e, bstack11ll11l_opy_)
    bstack1l111l1_opy_()
    bstack1l1l11_opy_(bstack11l1l_opy_)
    if bstack111l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨਯ") in args:
      i = args.index(bstack111l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩਰ"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1lll11ll_opy_))
    args.insert(0, str(bstack111l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ਱")))
    pabot.main(args)
  elif bstack1llll11_opy_ == bstack111l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧਲ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack111l11_opy_(e, bstack1lll11l_opy_)
    for a in args:
      if bstack111l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭ਲ਼") in a:
        bstack1llll1_opy_ = int(a.split(bstack111l_opy_ (u"ࠨ࠼ࠪ਴"))[1])
    bstack1l1l11_opy_(bstack11l1l_opy_)
    run_cli(args)
  else:
    bstack1lll1lll_opy_(bstack1llllll1_opy_)