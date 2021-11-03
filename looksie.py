import webbrowser
from tkinter import *
import tkinter.messagebox


print('''
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
*==========██╗      ██████╗  ██████╗ ██╗  ██╗███████╗██╗███████╗=========*
*==========██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██╔════╝██║██╔════╝=========*
*==========██║     ██║ * ██║██║ * ██║█████╔╝ ███████╗██║█████╗  =========*
*==========██║     ██║   ██║██║   ██║██╔═██╗ ╚════██║██║██╔══╝  =========*
*==========███████╗╚██████╔╝╚██████╔╝██║  ██╗███████║██║███████╗=========*
*==========╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝=========*
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
''')

# Ask for what to search for
searchItem = input("What are we searching for today?" + "\n\n")

print("\n\n")

print('Opening search in brower tabs!')

### search socials and search engines

# Search Google
webbrowser.open_new_tab(f"https://google.com/search?q={searchItem}")
# Search DuckDuckGo
webbrowser.open_new_tab(f"https://duckduckgo.com/?q={searchItem}")
# Search Yahoo
webbrowser.open_new_tab(f"https://search.yahoo.com/search?p={searchItem}")
# Search YouTube
webbrowser.open_new_tab(f"https://youtube.com/results?search_query={searchItem}")
# Search Facebook
webbrowser.open_new_tab(f"https://facebook.com/search/top/?q={searchItem}")
# Search LinkedIn
webbrowser.open_new_tab(f"https://linkedin.com/search/results/all/?keywords={searchItem}")

### Ask if user would like to search shodan

shodanResponse = input("\n\nWould you like to search shodan.io? (y/n): ")

if shodanResponse == "Y" or shodanResponse == "y":
    print("Searching shodan.io... \n")
    webbrowser.open_new_tab(f"https://www.shodan.io/search?query={searchItem}")

    ### Display message to tell user that the results are complete

    # Close root tkinter window
    Tk().withdraw()
    # Display messagebox with info about results
    result=tkinter.messagebox.showinfo('Looksie','Results are shown in your web browser in the tabs.')

    quit()

elif shodanResponse == "N" or shodanResponse == "n":
    print("Not searching shodan.io")

    ### Display message to tell user that the results are complete

    # Close root tkinter window
    Tk().withdraw()
    # Display messagebox with info about results
    result=tkinter.messagebox.showinfo('Looksie','Results are shown in your web browser in the tabs.')

    quit()

else:
    print("Not a vaild option. Exiting.")

    quit()

