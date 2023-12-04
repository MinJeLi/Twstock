import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class mechinL(object):
    def draw(history_price,history_volume):
        
        # Preparing data
        dates = [datetime.strptime(date, "%Y/%m/%d") for date in history_price.keys()]
        prices = [float(price) for price in history_price.values()]
        volumes = [int(volume.replace(",", "")) for volume in history_volume.values()]

        # Create figure and primary axis
        fig, ax1 = plt.subplots(figsize=(10, 5))

        # Plot price data on primary y-axis
        color = 'tab:blue'
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price', color=color)
        ax1.plot(dates, prices, color=color, marker='o', label='Price')
        ax1.tick_params(axis='y', labelcolor=color)

        # Create secondary y-axis for volume data
        ax2 = ax1.twinx()  
        color = 'tab:green'
        ax2.set_ylabel('Volume', color=color)
        ax2.plot(dates, volumes, color=color, marker='o', label='Volume')
        ax2.tick_params(axis='y', labelcolor=color)

        # Formatting x-axis
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        ax1.xaxis.set_major_locator(mdates.DayLocator())

        # Customization
        plt.title('Price and Volume History')
        fig.tight_layout() 
        plt.xticks(rotation=45)
        plt.show()
        
    def learning(history_of_price,history_of_volume):
        
        # Create DataFrame
        df = pd.DataFrame({'Price': history_of_price, 'Volume': history_of_volume})
        df['Price'] = df['Price'].astype(float)
        df['Volume'] = df['Volume'].str.replace(',', '').astype(int)
        
        # Prepare data for training
        X = df[['Volume']]  # Features
        y = df['Price']     # Target

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        # Initialize and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict and evaluate
        predictions = model.predict(X_test)
        print("Mean Squared Error:", mean_squared_error(y_test, predictions))
        
        # Predict values for the current volume
        df['Predicted_Price'] = model.predict(X)

        # Plotting the actual prices
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Volume'], df['Price'], color='blue', label='Actual Price')

        # Plotting the predicted prices
        plt.plot(df['Volume'], df['Predicted_Price'], color='red', label='Predicted Price')

        # Labelling
        plt.title('Volume vs Price')
        plt.xlabel('Volume')
        plt.ylabel('Price')
        plt.legend()

        # Show the plot
        plt.show()
                
                        