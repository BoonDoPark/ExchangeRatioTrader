class ExchangeRatio:
    def __init__(self, result=None, cur_unit=None, cur_nm=None, ttb=None, tts=None, deal_bas_r=None, bkpr=None, yy_eeee_r=None, ten_dd_efee_r=None, kftc_deal_bas_r=None, kftc_bkpr=None):
        """
        :param result: 조회 결과
        :param cur_unit: 통화코드
        :param cur_nm: 국가/통화명
        :param ttb: 전신환(송금) 받으실때
        :param tts: 전신환(송금) 보내실때
        :param deal_bas_r: 매매 기준율
        :param bkpr: 장부가격
        :param yy_eeee_r: 년환가료율
        :param ten_dd_efee_r: 10일환가료율
        :param kftc_deal_bas_r: 서울외국환중개 매매기준율
        :param kftc_bkpr: 서울외국환중개 장부가격
        """
        self._result = result
        self._cur_unit = cur_unit
        self._cur_nm = cur_nm
        self._ttb = ttb
        self._tts = tts
        self._deal_bas_r = deal_bas_r
        self._bkpr = bkpr
        self._yy_eeee_r = yy_eeee_r
        self._ten_dd_efee_r = ten_dd_efee_r
        self._kftc_deal_bas_r = kftc_deal_bas_r
        self._kftc_bkpr = kftc_bkpr

    @property
    def result(self):
        return self._result

    @property
    def cur_unit(self):
        return self._cur_unit

    @property
    def cur_nm(self):
        return self._cur_nm

    @property
    def ttb(self):
        return self._ttb

    @property
    def tts(self):
        return self._tts

    @property
    def deal_bas_r(self):
        return self._deal_bas_r

    @property
    def bkpr(self):
        return self._bkpr

    @property
    def yy_eeee_r(self):
        return self._yy_eeee_r

    @property
    def ten_dd_efee_r(self):
        return self._ten_dd_efee_r

    @property
    def kftc_deal_bas_r(self):
        return self._kftc_deal_bas_r

    @property
    def kftc_bkpr(self):
        return self._kftc_bkpr
