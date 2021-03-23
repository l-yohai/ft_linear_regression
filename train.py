import pandas as pd
import matplotlib.pyplot as plt
import sys
import math


class LinearRegression:

    def __init__(self):
        self.learning_rate = 0.1
        self.epochs = 500
        self.theta_0 = 0.0
        self.theta_1 = 0.0
        self.tmp_theta_0 = 0.0
        self.tmp_theta_1 = 0.0
        self.x = pd.DataFrame()
        self.y = pd.DataFrame()
        self.price = pd.DataFrame()
        self.km = pd.DataFrame()

    def error_exit(self, msg):
        sys.exit('Error: {}'.format(msg))

    def load(self):
        data_frame = pd.read_csv('data.csv', sep=',')
        self.price = data_frame.columns[1]
        self.km = data_frame.columns[0]
        self.x = self.normalize(data_frame[self.km])
        self.y = self.normalize(data_frame[self.price])
        return data_frame

    def normalize(self, x):
        return (x - min(x)) / (max(x) - min(x))

    def estimatePrice(self):
        return self.tmp_theta_0 + self.tmp_theta_1 * self.x

    def update(self):
        self.tmp_theta_0 = self.tmp_theta_0 - self.learning_rate * \
            (self.estimatePrice() - self.y).sum() / len(self.x)
        self.tmp_theta_1 = self.tmp_theta_1 - self.learning_rate * \
            (self.estimatePrice() - self.y).dot(self.x).sum() / len(self.x)

    def unnormalize(self, price, km):
        normalized_price = max(price) - min(price)
        normalized_km = max(km) - min(km)
        return [
            min(price) + normalized_price * (self.tmp_theta_0 -
                                             self.tmp_theta_1 * min(km) / normalized_km),
            self.tmp_theta_1 * normalized_price / normalized_km
        ]

    def cost(self):
        return ((self.tmp_theta_1 * self.x + self.tmp_theta_0 - self.y) ** 2).sum() / len(self.x)

    def drawFrame(self, data_frame):
        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        axes = plt.gca()
        self.xdata, ydata = data_frame[self.km], [0] * len(data_frame)
        self.line, = axes.plot(self.xdata, ydata, 'r-')
        self.line.set_xdata(self.xdata)
        plt.scatter(data_frame[self.km], data_frame[self.price])
        plt.ylabel(self.price)
        plt.xlabel(self.km)
        plt.title(self.price + ' = f(' + self.km + ')')

    def updateAndDrawLine(self, epoch):
        self.line.set_ydata(self.alpha[1] * self.xdata + self.alpha[0])
        plt.title('Epoch {}'.format(str(epoch)))
        plt.draw()
        plt.pause(1e-17)

    def drawCosts(self, epochs, costs):
        plt.subplot(122)
        plt.ylabel('Cost')
        plt.xlabel('Epochs')
        plt.title('Cost = f(epoch)')
        plt.plot(epochs, costs)
        plt.show()

    def train(self):
        data_frame = self.load()
        epochs, costs = [i for i in range(self.epochs)], []

        self.drawFrame(data_frame)

        for e in range(self.epochs):
            self.update()
            self.alpha = self.unnormalize(
                data_frame[self.price], data_frame[self.km])
            costs.append(self.cost())
            self.updateAndDrawLine(e)

        self.theta_0 = self.tmp_theta_0
        self.theta_1 = self.tmp_theta_1
        self.drawCosts(epochs, costs)

        try:
            with open('output.txt', "w+") as f:
                f.write('{}\n{}\n'.format(self.alpha[0], self.alpha[1]))
        except:
            self.error_exit('Wrong file')


if __name__ == '__main__':
    model = LinearRegression()
    model.train()
