import tensorflow as tf
import numpy as np

# fit model with loss function for our polynomial then implement model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, input_shape=(1,), activation='selu'),
    tf.keras.layers.Dense(1, activation='linear')])

model.compile(optimizer='Adam', loss='mse')

# generate training data to our function

x_train = np.array([])
y_train = np.array([])

for i in range(10000):
    x = np.random.uniform(0, 10)
    y = 9*x + 3*x**2 + 8*x**3+2*x**4 + 2
    print(x, y)
    x_train = np.append(x_train, x)
    y_train = np.append(y_train, y)


model.fit(x_train, y_train, epochs=5000)
# Testing our model with one or few points
print(model.predict(np.array([[7.57]])))
#Idea for testing out
#for o in range(100)
#something= np.random.uniform(0,10)
# def polynomial(huvisagch):
    #functional = 9*huvisagch + 3*huvisagch**2 + 8*huvisagch**3+2*huvisagch**4 + 2
# if i wrote my model as function then performing map 
#z=list(map(model.predict(),something))
#t=list(map(polynomial,something))
#MSE=np.square(np.substract(z,t)).mean()

