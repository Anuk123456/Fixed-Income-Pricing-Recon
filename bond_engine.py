import numpy as np


class Bond:

  def __init__(
      self,
      face_value: float,
      coupon_rate: float,
      maturity_years: float,
      frequency: int = 2,
  ):
    self.face_value = face_value
    self.coupon_rate = coupon_rate
    self.maturity_years = maturity_years
    self.frequency = frequency
    self.periods = int(maturity_years * frequency)
    self.coupon_payment = (face_value * coupon_rate) / frequency

  def get_cash_flows(self):
    cfs = [self.coupon_payment] * self.periods
    cfs[-1] += self.face_value
    times = [i / self.frequency for i in range(1, self.periods + 1)]
    return times, cfs

  def price(self, ytm: float) -> float:
    times, cfs = self.get_cash_flows()
    pv = sum(
        cf / (1 + ytm / self.frequency) ** (t * self.frequency)
        for t, cf in zip(times, cfs)
    )
    return pv

  def macaulay_duration(self, ytm: float) -> float:
    times, cfs = self.get_cash_flows()
    p = self.price(ytm)
    weighted_pv = sum(
        t
        * (cf / (1 + ytm / self.frequency) ** (t * self.frequency))
        for t, cf in zip(times, cfs)
    )
    return weighted_pv / p

  def modified_duration(self, ytm: float) -> float:
    mac_d = self.macaulay_duration(ytm)
    return mac_d / (1 + ytm / self.frequency)

  def dv01(self, ytm: float) -> float:
    bp = 0.0001
    p_up = self.price(ytm + bp)
    p_down = self.price(ytm - bp)
    return abs(p_down - p_up) / 2