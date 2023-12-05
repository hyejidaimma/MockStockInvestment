class Wallet:
    def __init__(self):
        self.balance = 10000000
        self.initial_balance = 10000000
        self.stocks_held = 0

    def get_initial_money(self):
        return self.initial_balance

    def get_money(self):
        return self.balance

    def add_money(self, money):
        if money >= 0:
            self.balance += money
        else:
            print("입금 금액은 음수가 될 수 없습니다.")

    def spend_money(self, money):
        if money >= 0:
            if self.balance >= money:
                self.balance -= money
            else:
                print("잔액이 부족합니다.")
        else:
            print("지출 금액은 음수가 될 수 없습니다.")
    def get_stocks_held(self):
        return self.stocks_held
    def add_stocks_held(self,stocks):
        self.stocks_held += stocks
    def spend_stocks_held(self,stocks):
        self.stocks_held -= stocks

class WalletManager:
    def __init__(self):
        self.wallet = Wallet()

    def market_watch(self, percent, decision, close):
        if decision is True:
            result = self._buy(percent, close)
            return result
        elif decision is False:
            result = self._sell(percent, close)
            return result
        elif decision is None:
            pass

    def print_current_info(self):
        print("---현재 자산--")
        print("보유 주식 수:", {self.wallet.get_stocks_held()}, "현재 자산 :", {self.wallet.get_money()})

    def get_yield(self):
        initial = self.wallet.get_initial_money()
        now = self.wallet.get_money()
        yield_percentage = ((now - initial) / initial) * 100
        return round(yield_percentage, 1)
    def _buy(self, percent, close):
        print(f"initial assets : {self.wallet.get_money()}")
        buy_amount = int(self.wallet.get_money() * percent / 100)
        num_of_stocks = buy_amount // close
        spend_assets = buy_amount - (buy_amount % close)
        self.wallet.spend_money(spend_assets)
        self.wallet.add_stocks_held(num_of_stocks)
        print(f" 매수 예정 금액 : {buy_amount} 실제 매수 금액: {spend_assets} 원, 보유 주식 수: {self.wallet.get_stocks_held()}, 현재 자산 : {self.wallet.get_money()}")
        return buy_amount

    def _sell(self, percent, close):
        print(f"initial assets : {self.wallet.get_money()}")
        num_of_stocks_to_sell = int(self.wallet.get_stocks_held() * percent / 100 )
        sell_amount = num_of_stocks_to_sell * close

        self.wallet.spend_stocks_held(num_of_stocks_to_sell)
        self.wallet.add_money(sell_amount)

        print(f"매도 예정 금액 : {sell_amount} won, 매도 주식 수량 : {num_of_stocks_to_sell}, "
              f"보유 주식 수: {self.wallet.get_stocks_held()}, 현재 자산: {self.wallet.get_money()}")
        return sell_amount

if __name__ == "__main__":
    wallet_manager = WalletManager()
    #매수 예시
    percent_to_buy = 100
    close_price_to_buy = 26450
    wallet_manager.market_watch(percent_to_buy, True, close_price_to_buy)
    #매도 예시
    percent_to_sell = 100
    close_price_to_sell = 45450
    wallet_manager.market_watch(percent_to_sell, False, close_price_to_sell)

    percent_to_sell = 100
    close_price_to_sell = 30000
    wallet_manager.market_watch(percent_to_sell, False, close_price_to_sell)
    #수익률 출력 예시
    print(wallet_manager.get_yield())
