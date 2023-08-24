from IPython.display import HTML, display
import pandas as pd
import tabulate	
def ShowDF(DF,col=''):
    DF=pd.DataFrame(DF)
    if col=='':
        col=list(DF.columns)
    display(HTML(tabulate.tabulate(DF[col], headers= col,tablefmt='html')))
