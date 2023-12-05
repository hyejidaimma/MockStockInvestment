import numpy as np

class FlagPattern():
  def __init__(self):
    self._regression = Regression()
    self._high_datas = []
    self._low_datas = []
    self._compare_minimum = 2
    self._same_rate = 1.8

  def set_minimum(self, num):
    self._compare_minimum = num

  def set_same_rate(self, rate):
    self._same_rate = rate

  def pattern_match(self, high_data, low_data):

    print()
    print("highs_datas :", self._high_datas)
    print("lows_datas :", self._low_datas)
    print()
    print("------------------high----------------------")
    print()
    high_rate =  self._regression_match(self._high_datas, high_data)
    print("-------------------low----------------------")
    print()
    low_rate =  self._regression_match(self._low_datas, low_data)

    is_match, rate = self._matching_result(high_data, low_data, high_rate, low_rate )

    return is_match, rate

  def _regression_match(self, y_datas, cur_data):
    if self._compare_minimum <= len(y_datas):

      self._regression.init_parameter()
      self._regression.update_parameter(np.arange(len(y_datas)),y_datas)
      predict_data = self._regression.predict(len(y_datas))
      rate = self._error_rate_calculation(predict_data, cur_data)
      print()
      print("predict:", predict_data.numpy()[0], "| data:", cur_data, "| rate:", rate.numpy()[0])
      print()
      return rate
    else:
      return None

  def _matching_result(self, high_data, low_data, high_rate, low_rate):
    if (not high_rate) or (not low_rate):
      self._add_datas(high_data, low_data)
      return None, -1.0

    if self._same_rate < high_rate:
      self._init_datas(high_data, low_data)
      return True, high_rate
    elif (-1 * self._same_rate) > low_rate:
      self._init_datas(high_data, low_data)
      return False, low_rate
    else:
      self._add_datas(high_data, low_data)
      return None, -1.0

  def _add_datas(self, high_data, low_data):
    self._high_datas.append(high_data)
    self._low_datas.append(low_data)

  def _init_datas(self, high_data, low_data):
    self._high_datas.clear()
    self._low_datas.clear()
    #self._high_datas.append(high_data)
    #self._low_datas.append(low_data)

  def _error_rate_calculation(self, pre_data:float, cur_data:float):
    rate = (cur_data - pre_data) / pre_data * 100
    return rate
