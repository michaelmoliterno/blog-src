Title: Scraping and Searching for Undervalued Movie Stars
Date: 2015-02-01 11:08
Category: blog
Tags: python, web scraping, beauitifulsoup, linear regression, plotly
Author: Michael Moliterno
Summary: Using the popular Beautiful Soup python package for web scraping, we pull down data on thousands of movies and look for actors, directors, and writers that have significantly impacted box office revenues during their careers. 

### Scraping Data from Box Office Mojo
[Box Office Mojo](http://www.boxofficemojo.com/) is a website that tracks box office revenue in a systematic, algorithmic way and is widely used within the movie industry as a source of data [source](https://en.wikipedia.org/wiki/Box_Office_Mojo).  

See my [GitHub repo for this project](https://github.com/michaelmoliterno/metis-projects/tree/master/luther) to check out the code that scrapes data for every movie released in the last 25 years (~15,000 titles). [luther_utils.py](https://github.com/michaelmoliterno/metis-projects/blob/master/luther/luther_utils.py) has all of the scraping functions, and [BoxOfficeMojoScrape.ipynb](http://nbviewer.ipython.org/github/michaelmoliterno/metis-projects/blob/master/luther/BoxOfficeMojoScrape.ipynb) shows how the functions are called. 


### Building the Models
Further detail will be added to this post about how features were selected and models were created, but if you want you can check out [MovieAnalysis.ipynb](http://nbviewer.ipython.org/github/michaelmoliterno/metis-projects/blob/master/luther/MovieAnalysis.ipynb) to get an idea of the analysis.  

### Giving plotly a Go with Movie Data

##### plotly
I was recently introduced to an online data visualization tool called [plotly](https://plot.ly/).  Chris Parmer (the Chief Product Officer of Plotly) showed me how, with just a few lines of code you can turn a matplotlib figure (efficient, but not the most striking figures you've ever seen) into an online, interactive, and editable graph. There are option for exporting the graphs you create and modify to python (among others); but even easier, you can embedding them in html (which is how the examples below are being served to you).  d3.js is still going to give you more control to build what you need, but plotly streamlines the process of building good-looking, interactive plots in minutes.  

Check out plotly's [getting started with python](https://plot.ly/python/getting-started/) and [matplotlib/plotly documentation](https://plot.ly/matplotlib/) pages for implementation details.  The documentation is great, but just to show you how simple it is: once you have plotly installed, it's literally two line of code to send a plot up to plotly for editing. 

```python
fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='file_name_for_plotly')
```

##### Observations

One of the key features that stood out to me was the very clear seasonal boost that box office revenues receive during the summer and holiday seasons.  Based on this observation, I encoded movies released May-July as 'summer' and November-December as 'holiday'. These two features turned out to be highly significant and drastically improved the performance of the models. 

<div>
    <a href="https://plot.ly/~mmoliterno/22/" target="_blank" title="Average Monthly Box Offices Revenues (1990-2014)" style="display: block; text-align: center;"><img src="https://plot.ly/~mmoliterno/22.png" alt="Average Monthly Box Offices Revenues (1990-2014)" style="max-width: 100%;width: 659px;"  width="659" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="mmoliterno:22" src="https://plot.ly/embed.js" async></script>
</div>


Once I accounted for budget, theaters in release, season, ans genre, I looked for actors, directors, and writers that significantly moved the needle up (or down) for their movies' box office revenues.  I used a sequential backward elimination methodology (in a self-rolled function) to eliminate features that were not significant until I was left with only significant features.  

Summarized below is a visualization of those significantly good (or bad) performers.  The multiplier is just like it sounds -- a multiplier on gross box office revenue.  So Will Smith's ~2.1 value means that in that data set we used, his presence accounts for a more than doubling of revenue.  But didn't we already know that?

<div>
    <a href="https://plot.ly/~mmoliterno/80/" target="_blank" title="Significant Revenue Multiplers for Hollywood Actors, Directors, and Writers" style="display: block; text-align: center;"><img src="https://plot.ly/~mmoliterno/80.png" alt="Significant Revenue Multiplers for Hollywood Actors, Directors, and Writers" style="max-width: 100%;width: 1179px;"  width="1179" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="mmoliterno:80" src="https://plot.ly/embed.js" async></script>
