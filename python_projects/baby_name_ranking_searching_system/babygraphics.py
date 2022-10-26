"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_interval = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    x_coordinate = x_interval*year_index+GRAPH_MARGIN_SIZE
    return x_coordinate


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    y_interval = (height-2*GRAPH_MARGIN_SIZE)/MAX_RANK
    if int(rank) > MAX_RANK:
        y_coordinate = height-GRAPH_MARGIN_SIZE
    else:

        y_coordinate = y_interval*int(rank)+GRAPH_MARGIN_SIZE
    return y_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    x1 = get_x_coordinate(CANVAS_WIDTH, 0)
    y1 = 0
    for i in range(len(lookup_names)):
        for j in range(len(YEARS)):
            year_rank = name_data[lookup_names[i]]  # year_rank looks like {'1900':'10'}
            if j == 0:  # first data
                if str(YEARS[j]) in year_rank:
                    y1 = get_y_coordinate(CANVAS_HEIGHT, year_rank[str(YEARS[j])])  # YEARS[j]:int
                    canvas.create_text(x1+TEXT_DX, y1, text=f'{lookup_names[i]} {year_rank[str(YEARS[j])]}',
                                       anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                else:
                    y1 = get_y_coordinate(CANVAS_HEIGHT, MAX_RANK+1)
                    canvas.create_text(x1+TEXT_DX, y1, text=f'{lookup_names[i]} *', anchor=tkinter.SW,
                                       fill=COLORS[i % len(COLORS)])

            else:
                x2 = get_x_coordinate(CANVAS_WIDTH, j)
                if str(YEARS[j]) in year_rank:
                    y2 = get_y_coordinate(CANVAS_HEIGHT, year_rank[str(YEARS[j])])
                    canvas.create_text(x2+TEXT_DX, y2, text=f'{lookup_names[i]} {year_rank[str(YEARS[j])]}',
                                       anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                else:
                    y2 = get_y_coordinate(CANVAS_HEIGHT, MAX_RANK+1)
                    canvas.create_text(x2+TEXT_DX, y2, text=f'{lookup_names[i]} *', anchor=tkinter.SW,
                                       fill=COLORS[i % len(COLORS)])
                canvas.create_line(x1, y1, x2, y2, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                x1, y1 = x2, y2
        x1 = get_x_coordinate(CANVAS_WIDTH, 0)
        y1 = 0


""


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
