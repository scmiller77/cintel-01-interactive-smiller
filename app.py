import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app
ui.page_opts(title="Smiller's PyShiny App with Plots", fillable=True)

#create a sidebar with a slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

#Histogram
@render.plot(alt="A histogram")
def histogram():
    count_of_points: int = 450
    np.random.seed(19680801)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)

#Create Scatter Plot
@render.plot(alt="Scatter Plot")
def scatter_plot():
    count_of_points: int = 450
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(count_of_points)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)

    # Create scatter plot and axes
    fig, ax = plt.subplots()
    ax.scatter(x, random_data_array, color='red')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Scatter Plot')
