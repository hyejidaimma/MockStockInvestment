import pandas as pd
import matplotlib.pyplot as plt

class ResultPrinter:
    def __init__(self):
        self.date = []
        self.decision = []
        self.close = []
        self.result = {}

    def set_data(self, date, decision, close):
        self.date.append(date)
        self.decision.append(decision)
        self.close.append(close)
        self.result = dict(zip(tuple(self.date), tuple(self.decision)))

        print("--지금까지 매수/매도 결정 리스트--")
        for k, v in self.result.items():
            if v != None:
                print(k, ":", v)
        print()

    def get_result(self):
        return self.result

    def save_to_csv(self, filename):

        df = pd.DataFrame(list(self.result.items()), columns=['Date', 'Decision'])
        df.to_csv(filename, index=False)
        print(f"Result saved to {filename}")

    def load_from_csv(self, filename):
        df = pd.read_csv(filename)
        self.result = dict(zip(df['Date'], df['Decision']))
        print(f"Result loaded from {filename}")

    def plot_graph(self):
        # CSV로 저장
        self.save_to_csv('result.csv')
        plt.figure(figsize=(30, 10))
        x_values = self.date
        y_values_close = self.close
        colors = []

        # Assigning colors based on decision values
        for value in self.decision:
            if value is True:
                colors.append('red')
            elif value is False:
                colors.append('blue')
            else:
                colors.append('gray')  # or any color for 'Pass'

        plt.plot(x_values, y_values_close, label='Close', color='black', marker='o', linestyle='-', linewidth=1)

        for i, color in enumerate(colors):
            if color != 'gray':  # Only plot if not 'Pass'
                plt.scatter(x_values[i], y_values_close[i], c=color, marker='s', label='Decision', s=100)

        for i, value in enumerate(self.decision):
            if value is True:
                plt.text(x_values[i], y_values_close[i], 'BUY', color='red', ha='center', va='bottom')
            elif value is False:
                plt.text(x_values[i], y_values_close[i], 'SELL', color='blue', ha='center', va='top')

        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.title('Close and Decision Over Time')
        plt.show()
# 예시 사용
if __name__ == "__main__":
    # 예시 데이터
    date_list = ['20230101', '20230102', '20230103', '20230104', '20230105', '20230106']
    decision_list = [True, False, None, None, True,False]  # Adding None for Pass
    close_list = [100, 120, 90, 70, 60, 120]

    # ResultPrinter 인스턴스 생성
    result_printer = ResultPrinter()
    for i in range(len(date_list)):
        result_printer.set_data(date_list[i],decision_list[i],close_list[i])

    # 결과 출력
    print("Result:", result_printer.get_result())

    # CSV로 저장
    result_printer.save_to_csv('result.csv')

    # CSV 불러오기
    result_printer.load_from_csv('result.csv')

    # 그래프 그리기
    result_printer.plot_graph()
