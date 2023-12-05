class MainFlow():
  def __init__(self) -> None:
    self.finance_manager = FinanceManager()
    self.flag_pattern = FlagPattern()
    self.decide = Decide()
    self.wallet_manager = WalletManager()
    self.result_printer = ResultPrinter()

    self.data_init()
    self.data_dict = {}

  def data_init(self):
    df = self.finance_manager.get_sise_years('041920',1)
    df = self.finance_manager.list_to_df(df)
    self.finance_manager.save_to_csv(df, 'stock_data.csv')

    self.flag_pattern.set_minimum(2)#선형회귀 시작 최소 데이터 개수
    self.flag_pattern.set_same_rate(2.0)#예측값과 현재값의 차이 임계값(매수/매도 결정)

    self.date_datas = self.finance_manager.get_datas("날짜")
    self.high_datas = self.finance_manager.get_datas("고가")
    self.low_datas = self.finance_manager.get_datas("저가")
    self.close_datas = self.finance_manager.get_datas("종가")
    self.open_datas = self.finance_manager.get_datas("시가")

  def compare_data(self, data1, data2):
    if data1 > data2:
      return data1, data2
    else:
      return data2, data1

  def run(self):
    for i in range(len(self.date_datas)):
      print("===================================================")
      print("data:", self.date_datas[i])

      #-----------------------------------------------------------
      high, low = self.compare_data(self.close_datas[i], self.open_datas[i])
      is_match, _ = self.flag_pattern.pattern_match(high, low)
      #is_match, _ = self.flag_pattern.pattern_match(self.high_datas[i], self.low_datas[i])
      money_percent, is_buy = self.decide.get_decide(self.close_datas[i], is_match)
      self.wallet_manager.market_watch(money_percent, is_buy, self.close_datas[i])
      self.result_printer.set_data(self.date_datas[i],is_buy,self.close_datas[i])
      #-----------------------------------------------------------

      self.wallet_manager.print_current_info()
      print()
      print("--금일 결정--")
      print("돈 퍼센트(%):",money_percent,"| 매도/매수:", is_buy)
      print()


    self.result_printer.plot_graph()
    print(self.wallet_manager.get_yield())


if __name__ == "__main__":
  main_flow = MainFlow()
  main_flow.run()
