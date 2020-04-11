print("hello world")


year = [2010, 2020]
pop = [3.12, 3.50]

# Import matplotlib.pyplot as plt
# import matplotlib.pyplot as pt


# Make a line plot: year on the x-axis, pop on the y-axis
#pt.plot(year,pop)


# Display the plot with plt.show()
# pt.show()



# import matplotlib.pyplot as plt

# plt.scatter(year, pop)
# plt.show()


import matplotlib.pyplot as plt

help(plt.hist)

values = [0,.6,1.4,1.6,2.2,2.5,2.6,3.2]

plt.hist(values, 3)

plt.show()
